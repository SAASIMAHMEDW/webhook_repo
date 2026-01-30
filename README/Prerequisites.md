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
