from flask import Blueprint, request, jsonify
from app.services.detect_from_video import detect_from_video

bp = Blueprint("frame", __name__)

@bp.route("/analyze-video", methods=["POST"])
def analyze_frame():
    if "frame" not in request.files:
        return jsonify({"error": "No frame uploaded"}), 400

    file = request.files["frame"]
    boxes = detect_from_video(file)

    if boxes is None:
        return jsonify({"error": "Erro ao processar frame"}), 500

    return jsonify(boxes)
