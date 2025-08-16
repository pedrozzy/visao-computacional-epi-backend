from flask import Blueprint, request, send_file
from app.services.detect_from_image import detect_from_image

bp = Blueprint("image", __name__, url_prefix="/")

@bp.route("/analyze-image", methods=["POST"])
def analyze_image():
    if "file" not in request.files:
        return {"error": "Arquivo de imagem não enviado"}, 400

    file = request.files["file"]
    result = detect_from_image(file)

    if not result:
        return {"error": "Erro no processamento da imagem"}, 500

    return send_file(result, mimetype="image/jpeg")