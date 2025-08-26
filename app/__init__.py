from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    
    # Get the root directory path
    root_dir = os.path.dirname(os.path.abspath(__file__ + "/.."))
    config_path = os.path.join(root_dir, 'config.py')
    
    # Load configuration from root directory
    if os.path.exists(config_path):
        app.config.from_pyfile(config_path)
    else:
        # Fallback to default configuration if config.py doesn't exist
        app.config['SECRET_KEY'] = 'dev-key-change-in-production'
        app.config['MQTT_BROKER_URL'] = 'localhost'
        app.config['MQTT_BROKER_PORT'] = 1883
        app.config['DATABASE'] = os.path.join(root_dir, 'smart_home.db')
        print("Using default configuration. Create config.py for custom settings.")
    
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Initialize database
    from app.models import init_db
    init_db(app.config['DATABASE'])
    
    # Register blueprints or routes
    from app.routes import main
    app.register_blueprint(main)
    
    # Connect to MQTT broker (but don't break if MQTT is not available)
    try:
        from app.mqtt_client import connect_mqtt
        connect_mqtt(app.config['MQTT_BROKER_URL'], app.config['MQTT_BROKER_PORT'])
    except Exception as e:
        print(f"Warning: Could not connect to MQTT broker: {e}")
        print("The app will still run, but MQTT functionality will be limited.")
    
    return app