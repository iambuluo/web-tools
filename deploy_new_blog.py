import subprocess
import sys
import os
import datetime
import time
import random

# 定义脚本路径
GENERATE_BLOG_SCRIPT = os.path.join(os.path.dirname(__file__), "generate_blog_post.py")

def run_command(command, cwd=None, log_callback=None):
    """运行 shell 命令并捕获输出"""
    if log_callback is None:
        log_callback = print # 默认打印到控制台

    try:
        process = subprocess.Popen(command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1, shell=True)
        
        # 实时读取并显示输出
        for line in process.stdout:
            log_callback(line.strip())
        
        # 读取剩余的 stderr
        stderr_output = process.stderr.read()
        if stderr_output:
            log_callback(f"错误信息:\n{stderr_output.strip()}")

        process.wait() # 等待进程结束

        if process.returncode != 0:
            log_callback(f"命令执行失败，退出码: {process.returncode}")
            raise subprocess.CalledProcessError(process.returncode, command, stderr=stderr_output)

        return "Command executed successfully."
    except subprocess.CalledProcessError as e:
        log_callback(f"命令执行失败: {e}")
        sys.exit(1)
    except FileNotFoundError:
        log_callback(f"错误: 命令未找到。请确保命令已安装并配置在 PATH 中。")
        sys.exit(1)

def deploy_new_blog(num_articles_to_generate=1, log_callback=None):
    if log_callback is None:
        log_callback = print # 默认打印到控制台

    log_callback(f"\n--- 开始生成 {num_articles_to_generate} 篇博客文章 ---")
    # 运行 generate_blog_post.py 脚本
    run_command([sys.executable, GENERATE_BLOG_SCRIPT, str(num_articles_to_generate)], log_callback=log_callback)

    log_callback("\n--- 自动暂存所有更改 ---")
    run_command(["git", "add", "."], log_callback=log_callback)

    log_callback("\n--- 自动提交更改 ---")
    # 生成一个包含当前日期和时间的提交信息
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    commit_message = f"feat: auto generate {num_articles_to_generate} blog posts ({timestamp})"
    run_command(["git", "commit", "-m", commit_message], log_callback=log_callback)

    log_callback("\n--- 推送到远程仓库，触发 Vercel 部署 ---")
    run_command(["git", "push"], log_callback=log_callback)

    log_callback("\n--- 部署完成！请检查您的网站。 ---")
    log_callback("**提示:** Vercel 部署可能需要一些时间，请稍后访问您的网站确认。")

if __name__ == "__main__":
    # 解析命令行参数，获取要生成的文章数量
    num_articles = 1 # 默认生成 1 篇
    if len(sys.argv) > 1:
        try:
            num_articles = int(sys.argv[1])
            if num_articles <= 0:
                raise ValueError
        except ValueError:
            print("用法: python deploy_new_blog.py [要生成的文章数量 (正整数)]")
            sys.exit(1)

    # 实现随机时间等待 (在9点-18点之间模拟随机性)
    current_hour = datetime.datetime.now().hour
    if 9 <= current_hour < 18:
        wait_time_seconds = random.randint(0, 300) # 随机等待 0-5 分钟
        print(f"在 {current_hour} 点到 18 点之间，模拟随机等待 {wait_time_seconds} 秒...\n")
        time.sleep(wait_time_seconds)

    deploy_new_blog(num_articles, log_callback=print)