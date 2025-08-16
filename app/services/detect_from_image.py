import numpy as np
import cv2
from PIL import Image
from io import BytesIO

from app.models.yolo_models import model_capacete, model_pessoa
from app.services.detectors import (
    get_head_regions, get_capacete_detections,
    match_helmets_to_heads, find_heads_without_helmets
)
from app.services.visualizer import draw_annotations

def detect_from_image(file):
    image = Image.open(file.stream).convert("RGB")
    img_array = np.array(image)

    # Detecção com modelos
    results_cap = model_capacete(img_array)[0]
    results_pessoa = model_pessoa(img_array)[0]

    # Processamento lógico
    heads = get_head_regions(results_pessoa)
    helmets = get_capacete_detections(results_cap)
    matched = match_helmets_to_heads(heads, helmets)
    missing = find_heads_without_helmets(heads, matched)

    # Visualização
    img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    annotated = draw_annotations(img_bgr, matched, missing)

    _, img_encoded = cv2.imencode(".jpg", annotated)
    return BytesIO(img_encoded.tobytes())
