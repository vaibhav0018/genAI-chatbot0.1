from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from app.services.data_service import fetch_google_sheet_data
from app.config import Config

scheduler = BackgroundScheduler()

def create_app(config_class=Config):
    app = Flask(__name__)
    
    # Explicitly set the secret key
    app.config['SECRET_KEY'] = Config.FLASK_SECRET_KEY
    if not app.config['SECRET_KEY']:
        app.config['SECRET_KEY'] = 'dev-temporary-key'  # Fallback for development
        
    app.config.from_object(config_class)
    
    # Initialize services
    fetch_google_sheet_data()
    
    # # Schedule data refresh
    scheduler.add_job(fetch_google_sheet_data, 'interval', minutes=3)
    scheduler.start()

    if not scheduler.running:
        scheduler.start()
    
    # Register blueprints
    from app.routes.chat_routes import chat_bp
    app.register_blueprint(chat_bp)

    # @app.teardown_appcontext
    # def shutdown_scheduler(exception=None):
    #     if scheduler.running:
    #         scheduler.shutdown()
    
    return app




















