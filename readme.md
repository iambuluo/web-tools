# JustHTMLs

<div align="center">

![JustHTMLs Logo](https://img.shields.io/badge/JustHTMLs-HTML%20Tools-6366f1?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![GitHub Stars](https://img.shields.io/github/stars/justhtmls/justhtmls.com?style=for-the-badge)

**开源 HTML 工具集 - 轻量、隐私、无需安装**

[在线体验](https://justhtmls.com/) | [贡献指南](CONTRIBUTING.html) | [提交工具](https://github.com/justhtmls/justhtmls.com/issues/new?template=tool-submission.md)

</div>

---

## 项目简介

JustHTMLs 是一个开源的 HTML 工具集平台，汇集各种轻量级的在线工具。所有工具均为单文件 HTML，无需安装，打开即用，数据在浏览器本地处理，保护您的隐私。

致力于打造最完整的中文 HTML 工具集合。

### 特点

- **单文件设计** - 所有工具都是独立的 HTML 文件，内联 CSS 和 JavaScript
- **无需构建** - 不使用 React/JSX，直接从浏览器打开
- **隐私优先** - 数据在本地处理，不发送到服务器
- **CDN 依赖** - 第三方库从 CDN 加载，无需 npm
- **开源免费** - MIT 许可证，欢迎贡献

---

## 工具分类

| 分类 | 描述 | 工具数量 |
|------|------|----------|
| 格式转换 | 各种文件和数据格式之间的转换工具 | - |
| 开发者工具 | 面向开发者的实用工具集合 | - |
| 文本处理 | 文本编辑、格式化和处理工具 | - |
| 图片处理 | 图片编辑、转换和优化工具 | - |
| 实用工具 | 日常生活中的实用小工具 | - |

---

## 快速开始

### 在线使用

直接访问 [JustHTMLs 网站](https://justhtmls.com/) 即可使用所有工具。

### 本地运行

```bash
# 克隆仓库
git clone https://github.com/justhtmls/html-tools.git
cd html-tools

# 使用任意静态服务器运行
python -m http.server 8000
# 或
npx serve .
```

然后在浏览器中访问 `http://localhost:8000`

---

## 贡献工具

我们欢迎社区贡献！提交新工具的流程非常简单：

### 方式一：通过 GitHub Issues（推荐）

1. 创建你的工具（单文件 HTML）
2. [创建工具提交 Issue](https://github.com/justhtmls/html-toolsissues/new?template=tool-submission.md)
3. 填写工具信息并粘贴代码
4. 等待审核通过后合并

### 方式二：Pull Request

1. Fork justhtmls/html-tools 仓库
2. 在 `tools/` 目录下创建你的工具文件夹
3. 按规范创建工具文件
4. 更新 `index.json` 索引
5. 提交 Pull Request

### 工具规范

每个工具必须包含：

```
tools/
  └── your-tool/
      ├── index.html    # 工具详情页（介绍页面）
      └── app.html      # 工具实体页（实际运行的工具）
```

**设计原则：**

- 单文件 HTML，内联 CSS/JS
- 不使用 React 或需要构建的技术
- 从 CDN 加载第三方库
- 保持精简（建议 500 行以内）
- 数据本地处理，保护隐私

详细内容请查看 [贡献指南](CONTRIBUTING.html)。

---

## 项目结构

```
justhtmls.com/
├── index.html              # 主站门户首页
├── index.json              # 工具索引文件
├── CONTRIBUTING.html       # 贡献指南
├── README.md               # 项目说明
├── tools/                  # 工具目录
│   └── tool-name/         # 单个工具文件夹
│       ├── index.html     # 工具详情页
│       └── app.html       # 工具实体页
└── .github/
    └── ISSUE_TEMPLATE/    # GitHub Issue 模板
        ├── tool-submission.md
        └── bug-report.md
```

---

## 开发路线图

- [x] 基础网站框架
- [x] 工具索引系统
- [x] 搜索和过滤功能
- [x] 工具提交流程
- [ ] 用户系统（收藏、历史记录）
- [ ] 工具评分和评论
- [ ] 私人工具侧载功能
- [ ] 移动端优化

---

## 技术栈

- **纯 HTML/CSS/JavaScript** - 无构建步骤
- **GitHub Pages** - 静态托管
- **GitHub Issues** - 工具提交流程

---

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 鸣谢

- 所有贡献者 - 感谢你们的贡献！

---

<div align="center">

**如果这个项目对你有帮助，请给它一个 Star ⭐**

</div>
