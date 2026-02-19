# 网站维护与更新手册 (USAGE.md)

本文档旨在帮助你维护和更新 **AiChatX Tools** 网站。

## 1. 日常更新流程

如果你修改了任何文件（例如修改了 HTML、修复了工具 Bug 或添加了新页面），请按照以下步骤将更改推送到 GitHub 并自动部署上线。

### 步骤 1：检查修改状态
打开终端（Terminal），输入：
```powershell
git status
```
这将列出所有你修改过的文件（红色显示）。

### 步骤 2：添加修改到暂存区
```powershell
git add .
```
注意最后的 `.` 代表当前目录下所有文件。

### 步骤 3：提交修改说明
```powershell
git commit -m "简短描述你的修改内容"
```
例如：`git commit -m "fix: 修复房贷计算器bug"` 或 `git commit -m "update: 修改首页文字"`。

### 步骤 4：推送到 GitHub
```powershell
git push
```
推送成功后，Vercel 会自动检测更新并重新部署。通常几分钟后访问 `aichatx.com.cn` 就能看到效果。

---

## 2. 批量修改工具页面

如果你需要对所有工具页面进行统一修改（例如更改页脚、添加新的统计代码等），可以使用项目根目录下的脚本。

### Python 脚本
我们编写了几个辅助脚本，可以直接运行：

*   `check_tools.py`: 检查所有工具页面结构是否完整。
    ```powershell
    python check_tools.py
    ```
*   `inject_adsense.py`: 批量检查并注入 AdSense 代码（如果未来 AdSense 代码变了，可以修改此脚本后运行）。
*   `replace_brand.py`: 批量替换品牌名称（如将 JustHTMLs 替换为 AiChatX Tools）。

---

## 3. 常见问题排查

### 网站打不开或 404
*   检查 GitHub 仓库中是否有 `index.html`。
*   登录 Vercel 后台查看 Deployment Logs（部署日志），看是否有构建错误。

### 广告不显示
*   AdSense 审核通常需要几天时间。
*   确保 `ads.txt` 文件可以通过 `https://www.aichatx.com.cn/ads.txt` 访问。
*   检查浏览器是否开启了广告拦截插件。

### 提交代码时报错
如果 `git push` 失败，提示冲突（conflict）：
1.  先拉取最新代码：`git pull`
2.  如果有冲突文件，手动打开解决冲突。
3.  再次执行 `git add .`, `git commit`, `git push`。

---

## 4. 目录结构说明

*   `/tools/`: 存放所有工具的目录，每个工具一个子文件夹。
*   `index.html`: 网站首页。
*   `ads.txt`: AdSense 授权文件。
*   `sitemap.xml`: 网站地图（SEO用）。
*   `CNAME`: 自定义域名配置文件（主要用于 GitHub Pages，Vercel 会忽略）。
