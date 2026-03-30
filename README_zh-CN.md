# Python 云函数 - Flask | EdgeOne Pages

基于 Next.js + Tailwind CSS 的演示网站，展示如何在 EdgeOne Pages 上将 Flask Web 应用部署为无服务器函数。

## 🚀 特性

- **Flask 框架**：最流行的 Python 微型 Web 框架
- **装饰器路由**：熟悉的 `@app.route()` 语法
- **蓝图支持**：使用 Flask 蓝图组织代码
- **现代化 UI**：采用黑底白字主题
- **实时 API 演示**：直接在网页上测试 Flask 函数

## 🛠️ 技术栈

### 前端
- **Next.js 15** - React 全栈框架
- **React 19** - 用户界面库
- **TypeScript** - 类型安全的 JavaScript
- **Tailwind CSS 4** - 实用优先的 CSS 框架

### 后端
- **Flask** - Python 微型 Web 框架
- **Cloud Functions** - EdgeOne Pages 无服务器函数

## 📁 项目结构

```
python-flask-template/
├── src/                    # Next.js 前端
├── cloud-functions/        # Python 云函数
│   ├── api/
│   │   └── [[default]].py # Flask 应用
│   └── requirements.txt   # Python 依赖
├── public/                # 静态资源
└── package.json          # 项目配置
```

## 🚀 快速开始

### 环境要求

- Node.js 18+ 
- Python 3.9+
- EdgeOne CLI

### 安装依赖

```bash
npm install
```

### 开发模式

```bash
edgeone pages dev
```

访问 [http://localhost:8088](http://localhost:8088) 查看应用。

## 🎯 API 端点

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | /api/ | 根端点 |
| GET | /api/health | 健康检查 |
| GET | /api/info | 函数信息 |
| GET | /api/time | 当前服务器时间 |
| GET/POST | /api/echo | 回显请求信息 |
| POST | /api/json | 处理 JSON 请求体 |
| GET | /api/users/:id | 根据 ID 获取用户 |
| POST | /api/users | 创建新用户 |
| GET | /api/search | 带查询参数搜索 |

## 📚 文档入口

- **Flask 文档**：[https://flask.palletsprojects.com](https://flask.palletsprojects.com)
- **EdgeOne Pages 文档**：[https://pages.edgeone.ai/document/python](https://pages.edgeone.ai/document/python)

## 部署

[![Deploy with EdgeOne Pages](https://cdnstatic.tencentcs.com/edgeone/pages/deploy.svg)](https://console.cloud.tencent.com/edgeone/pages/new?from=github&template=python-flask-template)

## 📄 许可证

本项目采用 MIT 许可证。
