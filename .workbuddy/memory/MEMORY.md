# 项目记忆 - aichatx.com.cn 工具网站

## 项目基本信息
- **网站地址**: https://www.aichatx.com.cn
- **仓库**: https://github.com/iambuluo/web-tools.git (分支: main)
- **部署方式**: GitHub + Vercel 自动部署
- **本地目录**: D:/小程序/web-tools_aichatx.com.cn

## 广告配置
- **广告平台**: Monetag（已放弃 AdSense 审核）
- **广告形式**: Multitag (all-in-one) - 推荐，收益最高且对SEO影响最小
- **广告代码**: `<script src="https://quge5.com/88/tag.min.js" data-zone="229646" async data-cfasync="false"></script>`
- **插入位置**: 所有 HTML 页面 `<meta charset="UTF-8">` 之后
- **覆盖范围**: 首页、about、contact、privacy、terms、tools-rank、全部 tools/*/index.html、全部 blog/*.html

## Git 推送配置
- **代理**: 127.0.0.1:7897 (Clash/V2Ray，需开启)
- **配置命令**: `git config http.proxy "http://127.0.0.1:7897"`
- **注意**: 推送前需确保代理软件已启动

## SEO 优化历史
- 2026-03-30: 增强 About 页面至1500字，删除3个非AI低质量博客，更新 robots.txt 和 sitemap.xml
- 2026-04-14: 优化首页 meta title/description/keywords，添加 og/twitter 标签

## 网站结构
- `tools/` - 250+ 工具页面（每个工具独立目录含 index.html）
- `blog/` - AI 实战教程博客文章
- `about.html`, `contact.html`, `privacy.html`, `terms.html` - 必要信息页
- `tools-rank.html` - 工具排行榜页
