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
