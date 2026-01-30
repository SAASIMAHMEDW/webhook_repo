# About

A real-time GitHub webhook receiver built with Flask and MongoDB. This application:

- Captures GitHub events (Push, Pull Request, Merge) via webhooks
- Stores events in MongoDB
- Displays them on a live-updating dashboard
- Polls for new events every 15 seconds

# Tech Stack

## Backend

- Python 3.12+
- Flask (with Blueprints)
- Flask-PyMongo
- python-dotenv
- Gunicorn (production server)

## Database

- MongoDB (Atlas or Local)

## Frontend

- HTML5
- CSS3 (custom dark theme)
- Vanilla JavaScript (polling every 15 seconds)

## DevOps & Tools

- Docker
- Docker Compose
- ngrok (webhook tunneling)
- UV (Python package manager)

## External Services

- GitHub Webhooks
- MongoDB Atlas (optional)

# Tech Stack

## Backend

- Python 3.12+
- Flask (with Blueprints)
- Flask-PyMongo
- python-dotenv
- Gunicorn (production server)

## Database

- MongoDB (Atlas or Local)

## Frontend

- HTML5
- CSS3 (custom dark theme)
- Vanilla JavaScript (polling every 15 seconds)

## DevOps & Tools

- Docker
- Docker Compose
- ngrok (webhook tunneling)
- UV (Python package manager)

## External Services

- GitHub Webhooks
- MongoDB Atlas (optional)

# How to Run

## Prerequisites

- Python 3.13+ installed
- MongoDB (local or Atlas account)
- GitHub account (for webhook testing)
- ngrok account (for local webhook tunneling)

## Method 1: Local Development with UV (Recommended)

1. Clone and navigate:

   ```bash
   git clone https://github.com/SAASIMAHMEDW/webhook_action_receiver_repo.git
   cd webhook_action_receiver_repo
   ```

2. Install dependencies with UV:

   ```bash
   uv pip install -r requirements.txt
   ```

3. Create `.env` file:

   ```env
   MONGO_URI=mongodb://localhost:27017/github_webhooks
   SECRET_KEY=your-secret-key-here
   FLASK_ENV=development
   FLASK_DEBUG=True
   ```

4. Run the application:

   ```bash
   python run.py
   ```

5. Access:
   - Dashboard: http://localhost:5000
   - API: http://localhost:5000/api/events

## Method 2: Local Development with Virtual Environment

1. Create virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate:

   ```bash
   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create `.env` file (same as Method 1)

5. Run:
   ```bash
   python run.py
   ```

## Method 3: Docker (Single Container)

1. Build image:

   ```bash
   docker build -t webhook-app .
   ```

2. Run with Atlas:

   ```bash
   docker run -d -p 5000:5000 -e SECRET_KEY=super_secret -e MONGO_URI="xxx" --name webhook-app webhook-app
   ```

## Method 4: Docker Compose (Recommended for Full Stack)

Create `.env.docker`:

```env
# MongoDB Configuration
MONGO_URI=xxx

# Flask Configuration
SECRET_KEY=super-secret

# Flask Environment
FLASK_ENV=production
FLASK_DEBUG=False
```

### Option A: MongoDB Atlas only

```bash
docker-compose --profile atlas up -d --build
```

App runs on: http://localhost:5000

### Option B: Local MongoDB + Backend

```bash
docker-compose --profile local up -d --build
```

- App runs on: http://localhost:5001
- MongoDB on: mongodb://localhost:27017

### Stop services:

```bash
docker-compose --profile atlas down
docker-compose --profile local down
```

# Prerequisites / Setup Before Running

## 1. Create GitHub Repository (action-repo)

- Go to GitHub and create a new repository
- Name it `webhook-action-repo` (or any name)
- Make it public or private
- Clone it locally:

```bash
git clone https://github.com/SAASIMAHMEDW/webhook-action-repo.git
cd webhook-action-repo
```

## 2. Install ngrok

**Windows:**

```bash
choco install ngrok
```

**macOS:**

```bash
brew install ngrok
```

Or download from [ngrok.com/download](https://ngrok.com/download)

Sign up and configure authtoken:

```bash
ngrok config add-authtoken YOUR_AUTHTOKEN
```

## 3. Start ngrok Tunnel

```bash
ngrok http 5000
```

Copy the HTTPS URL (e.g., `https://abc123.ngrok-free.app`)

## 4. Configure GitHub Webhook

- Go to your `webhook-action-repo` on GitHub
- Settings → Webhooks → Add webhook
- **Payload URL:** `https://your-ngrok-url.ngrok-free.app/webhook/receiver`
- **Content type:** `application/json`
- **Which events:** Select "Let me select individual events"
- Check: **Pushes** and **Pull requests**
- Add webhook

## 5. Test Webhook

Make a commit and push:

```bash
echo "test" > test.txt
git add .
git commit -m "Test webhook"
git push origin main
```

Check your dashboard for the event.

# Environment Variables

Create a `.env` file in the project root:

| Variable    | Description                   | Example                                                  |
| ----------- | ----------------------------- | -------------------------------------------------------- |
| MONGO_URI   | MongoDB connection string     | `mongodb://localhost:27017/github_webhooks` or Atlas URL |
| SECRET_KEY  | Flask secret key for sessions | `b96e87df-0ff4-41e3-9118-47fcc622829f`                   |
| FLASK_ENV   | Flask environment mode        | `development` or `production`                            |
| FLASK_DEBUG | Enable debug mode             | `True` or `False`                                        |

## Local Development `.env`

```env
MONGO_URI=mongodb://localhost:27017/github_webhooks
SECRET_KEY=dev-secret-key
FLASK_ENV=development
FLASK_DEBUG=True
```

## Production `.env` or `.env.docker`

```env
MONGO_URI=mongodb+srv://user:pass@cluster.mongodb.net/github_webhooks?retryWrites=true&w=majority
SECRET_KEY=super-secret-production-key
FLASK_ENV=production
FLASK_DEBUG=False
```

# Conclusion

This project showcases a fully functional webhook-based event processing system. It captures GitHub activities in real-time, stores them in MongoDB, and presents them on a live-updating dashboard. With a modular Flask architecture, Docker containerization, and thorough documentation, it is production-ready and easily extensible.
