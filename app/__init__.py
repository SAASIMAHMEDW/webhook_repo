from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from app.extensions import mongo
from app.webhook.routes import webhook
from app.ui.routes import ui


def create_app():
    # Load environment variables
    load_dotenv()
    
    app = Flask(__name__)
    
    # Configuration
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key")
    app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/github_webhooks")
    
    # Initialize extensions
    mongo.init_app(app)
    CORS(app)
    
    # Register blueprints
    app.register_blueprint(webhook)   # Register the webhook blueprint
    app.register_blueprint(ui)        # Register the UI blueprint
    
    return app