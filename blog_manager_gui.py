import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import subprocess
import threading
import os
import json
import webbrowser
import sys

# 导入 deploy_new_blog 模块，以便调用其中的 deploy_new_blog 函数
# 注意: 确保 deploy_new_blog.py 和 generate_blog_post.py 在同一目录下
from deploy_new_blog import deploy_new_blog

# 定义脚本和数据文件路径
SCRIPT_DIR = os.path.dirname(__file__)
# DEPLOY_SCRIPT = os.path.join(SCRIPT_DIR, "deploy_new_blog.py") # GUI直接调用函数，不再需要通过subprocess运行脚本
GENERATED_BLOGS_JSON = os.path.join(SCRIPT_DIR, "generated_blogs.json")
WEBSITE_DOMAIN = "https://www.aichatx.com.cn" # 您的网站域名

class BlogManagerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AI ChatX 博客管理工具")
        self.geometry("800x700") # 增加高度以容纳更多内容

        # ... (GUI 布局代码保持不变) ...

    def redirect_stdout(self):
        """将标准输出重定向到日志文本区域"""
        self.log_text.configure(state='normal')
        self.log_text.delete(1.0, tk.END) # 清空日志
        self.log_text.configure(state='disabled')
        
        self._original_stdout = sys.stdout # 保存原始stdout
        self._original_stderr = sys.stderr # 保存原始stderr
        sys.stdout = self
        sys.stderr = self

    def write(self, message):
        """用于重定向 stdout/stderr 的 write 方法"""
        self.log_text.configure(state='normal')
        self.log_text.insert(tk.END, message + "\n") # 确保每条消息换行
        self.log_text.see(tk.END) # 自动滚动到最新内容
        self.log_text.configure(state='disabled')
        self.update_idletasks() # 强制Tkinter更新界面

    def flush(self):
        """write 方法需要 flush 方法，但在这里可以空实现"""
        pass

    def start_deploy_thread(self):
        """在单独线程中运行部署，避免GUI冻结"""
        self.deploy_button.config(state=tk.DISABLED)
        self.check_blogs_button.config(state=tk.DISABLED)
        
        # 清空日志区域并启用写入
        self.log_text.configure(state='normal')
        self.log_text.delete(1.0, tk.END) 
        self.log_text.configure(state='disabled')

        num_articles_str = self.num_articles_entry.get()
        try:
            num_articles = int(num_articles_str)
            if num_articles <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("输入错误", "请输入一个有效的正整数作为生成文章的数量。")
            self.deploy_button.config(state=tk.NORMAL)
            self.check_blogs_button.config(state=tk.NORMAL)
            return

        # 启动新线程来执行部署逻辑
        thread = threading.Thread(target=self._run_deploy_logic, args=(num_articles,))
        thread.daemon = True # 设置为守护线程，主程序退出时自动终止
        thread.start()

    def _run_deploy_logic(self, num_articles):
        """直接调用 deploy_new_blog 函数，并传入 GUI 的 write 方法作为回调"""
        try:
            deploy_new_blog(num_articles, log_callback=self.write) # 调用 deploy_new_blog 函数
        except SystemExit as e:
            self.write(f"脚本执行终止: {e}")
        except Exception as e:
            self.write(f"执行脚本时发生意外错误: {e}")
        finally:
            self.deploy_button.config(state=tk.NORMAL)
            self.check_blogs_button.config(state=tk.NORMAL)
            self.check_published_blogs() # 部署完成后自动刷新博客列表

    def check_published_blogs(self):
        """显示已发布的博客文章列表及其 Google Search Console 链接"""
        # 清空现有列表
        for widget in self.blog_inner_frame.winfo_children():
            widget.destroy()

        self.write("\n--- 正在加载已发布博客列表 ---")
        if not os.path.exists(GENERATED_BLOGS_JSON):
            ttk.Label(self.blog_inner_frame, text="尚未发布任何博客文章。").pack(pady=5)
            self.write("generated_blogs.json 文件不存在，没有已发布博客。")
            return

        try:
            with open(GENERATED_BLOGS_JSON, "r", encoding="utf-8") as f:
                blogs = json.load(f)
            
            if not blogs:
                ttk.Label(self.blog_inner_frame, text="generated_blogs.json 文件为空，尚未发布任何博客文章。").pack(pady=5)
                self.write("generated_blogs.json 文件为空。")
                return

            self.write(f"已加载 {len(blogs)} 篇博客文章。")
            # 按照日期倒序排列，最新文章显示在最前面
            blogs.sort(key=lambda x: x.get('date', ''), reverse=True)

            for i, blog in enumerate(blogs):
                blog_frame = ttk.Frame(self.blog_inner_frame, relief=tk.GROOVE, borderwidth=1, padding=5)
                blog_frame.pack(fill=tk.X, pady=2, padx=2)

                title_label = ttk.Label(blog_frame, text=f"标题: {blog.get('title', '未知标题')}")
                title_label.pack(anchor=tk.W)

                date_label = ttk.Label(blog_frame, text=f"日期: {blog.get('date', '未知日期')}")
                date_label.pack(anchor=tk.W)
                
                slug = blog.get('slug', '')
                if slug:
                    blog_url = f"{WEBSITE_DOMAIN}/blog/{slug}"
                    url_label = ttk.Label(blog_frame, text=f"URL: {blog_url}", foreground="blue", cursor="hand2")
                    url_label.pack(anchor=tk.W)
                    url_label.bind("<Button-1>", lambda e, url=blog_url: webbrowser.open_new(url))

                    # Google Search Console URL 检查工具链接
                    gsc_url = f"https://search.google.com/search-console/inspect?resource_id={WEBSITE_DOMAIN}&url={blog_url}"
                    gsc_button = ttk.Button(blog_frame, text="在 GSC 中检查索引", command=lambda url=gsc_url: webbrowser.open_new(url))
                    gsc_button.pack(anchor=tk.W, pady=2)
                else:
                    ttk.Label(blog_frame, text="URL: N/A").pack(anchor=tk.W)

        except json.JSONDecodeError:
            ttk.Label(self.blog_inner_frame, text="generated_blogs.json 文件格式错误，请检查。").pack(pady=5)
            self.write("错误: generated_blogs.json 文件格式错误。")
        except Exception as e:
            ttk.Label(self.blog_inner_frame, text=f"加载博客列表时发生错误: {e}").pack(pady=5)
            self.write(f"加载博客列表时发生错误: {e}")
        finally:
            self.blog_list_canvas.update_idletasks()
            self.blog_list_canvas.config(scrollregion=self.blog_list_canvas.bbox("all"))

if __name__ == "__main__":
    app = BlogManagerGUI()
    app.mainloop().pack(pady=5)
                print("generated_blogs.json 文件为空。")
                return

            print(f"已加载 {len(blogs)} 篇博客文章。")
            for i, blog in enumerate(blogs):
                blog_frame = ttk.Frame(self.blog_inner_frame, relief=tk.GROOVE, borderwidth=1, padding=5)
                blog_frame.pack(fill=tk.X, pady=2, padx=2)

                title_label = ttk.Label(blog_frame, text=f"标题: {blog.get('title', '未知标题')}")
                title_label.pack(anchor=tk.W)

                date_label = ttk.Label(blog_frame, text=f"日期: {blog.get('date', '未知日期')}")
                date_label.pack(anchor=tk.W)
                
                slug = blog.get('slug', '')
                if slug:
                    blog_url = f"{WEBSITE_DOMAIN}/blog/{slug}"
                    url_label = ttk.Label(blog_frame, text=f"URL: {blog_url}", foreground="blue", cursor="hand2")
                    url_label.pack(anchor=tk.W)
                    url_label.bind("<Button-1>", lambda e, url=blog_url: webbrowser.open_new(url))

                    # Google Search Console URL 检查工具链接
                    # 请替换 your-domain.com 为您的实际域名
                    # GSC URL 检查工具的URL结构可能需要根据实际情况调整
                    gsc_url = f"https://search.google.com/search-console/inspect?resource_id={WEBSITE_DOMAIN}&url={blog_url}"
                    gsc_button = ttk.Button(blog_frame, text="在 GSC 中检查索引", command=lambda url=gsc_url: webbrowser.open_new(url))
                    gsc_button.pack(anchor=tk.W, pady=2)
                else:
                    ttk.Label(blog_frame, text="URL: N/A").pack(anchor=tk.W)

        except json.JSONDecodeError:
            ttk.Label(self.blog_inner_frame, text="generated_blogs.json 文件格式错误，请检查。").pack(pady=5)
            print("错误: generated_blogs.json 文件格式错误。")
        except Exception as e:
            ttk.Label(self.blog_inner_frame, text=f"加载博客列表时发生错误: {e}").pack(pady=5)
            print(f"加载博客列表时发生错误: {e}")
        finally:
            self.blog_list_canvas.update_idletasks()
            self.blog_list_canvas.config(scrollregion=self.blog_list_canvas.bbox("all"))

if __name__ == "__main__":
    app = BlogManagerGUI()
    app.mainloop()