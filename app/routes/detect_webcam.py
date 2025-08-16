from flask import Blueprint, Response, stream_with_context, jsonify, request
from app.services.detect_from_webcam import generate_frames_from_camera

bp = Blueprint("webcam", __name__, url_prefix="/")

@bp.route("/detect-webcam")
def webcam_feed():
    return Response(
        stream_with_context(generate_frames_from_camera()),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )