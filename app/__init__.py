from flask import Flask
from flask_cors import CORS

from app.routes import analyze_video, analyze_image, detect_webcam

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    app.register_blueprint(analyze_image.bp)
    app.register_blueprint(analyze_video.bp)
    app.register_blueprint(detect_webcam.bp)

    return app