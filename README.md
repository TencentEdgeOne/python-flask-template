# Python Cloud Functions - Flask | EdgeOne Pages

A demonstration website based on Next.js + Tailwind CSS, showcasing how to deploy Flask web applications as serverless functions on EdgeOne Pages.

## 🚀 Features

- **Flask Framework**: The most popular Python micro web framework
- **Decorator Routing**: Familiar `@app.route()` syntax
- **Blueprint Support**: Organize your code with Flask blueprints
- **Modern UI**: Black background with white text theme
- **Real-time API Demo**: Test the Flask function directly from the webpage

## 🛠️ Tech Stack

### Frontend
- **Next.js 15** - React full-stack framework
- **React 19** - User interface library
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS 4** - Utility-first CSS framework

### Backend
- **Flask** - Python micro web framework
- **Cloud Functions** - EdgeOne Pages serverless functions

## 📁 Project Structure

```
python-flask-template/
├── src/                    # Next.js frontend
├── cloud-functions/        # Python cloud functions
│   ├── api/
│   │   └── [[default]].py # Flask application
│   └── requirements.txt   # Python dependencies
├── public/                # Static assets
└── package.json          # Project configuration
```

## 🚀 Quick Start

### Requirements

- Node.js 18+ 
- Python 3.9+
- EdgeOne CLI

### Install Dependencies

```bash
npm install
```

### Development Mode

```bash
edgeone pages dev
```

Visit [http://localhost:8088](http://localhost:8088) to view the application.

## 🎯 API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /api/ | Root endpoint |
| GET | /api/health | Health check |
| GET | /api/info | Function information |
| GET | /api/time | Current server time |
| GET/POST | /api/echo | Echo request info |
| POST | /api/json | Handle JSON body |
| GET | /api/users/:id | Get user by ID |
| POST | /api/users | Create new user |
| GET | /api/search | Search with query params |

## 📚 Documentation

- **Flask Documentation**: [https://flask.palletsprojects.com](https://flask.palletsprojects.com)
- **EdgeOne Pages Docs**: [https://pages.edgeone.ai/document/python](https://pages.edgeone.ai/document/python)

## Deploy

[![Deploy with EdgeOne Pages](https://cdnstatic.tencentcs.com/edgeone/pages/deploy.svg)](https://edgeone.ai/pages/new?from=github&template=python-flask-template)

## 📄 License

This project is licensed under the MIT License.
