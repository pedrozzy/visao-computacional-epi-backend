import numpy as np
from PIL import Image
from app.models.yolo_models import model_capacete, model_pessoa
from app.services.detectors import (
    get_head_regions, get_capacete_detections,
    match_helmets_to_heads, find_heads_without_helmets
)

def detect_from_video(file):
    try:
        # Abre a imagem e converte para RGB
        image = Image.open(file.stream).convert("RGB")
        img_array = np.array(image)

        # Aplicação dos modelos
        results_cap = model_capacete(img_array)[0]
        results_pessoa = model_pessoa(img_array)[0]

        # Lógica de detecção
        heads = get_head_regions(results_pessoa)
        helmets = get_capacete_detections(results_cap)
        matched = match_helmets_to_heads(heads, helmets)
        missing = find_heads_without_helmets(heads, matched)

        # Monta boxes
        boxes = []
        for m in matched:
            x1, y1, x2, y2 = m["head"]
            boxes.append({
                "x1": x1, "y1": y1, "x2": x2, "y2": y2,
                "label": "Capacete: OK."
            })
        for x1, y1, x2, y2 in missing:
            boxes.append({
                "x1": x1, "y1": y1, "x2": x2, "y2": y2,
                "label": "Capacete: Falta."
            })

        return boxes
    except Exception as e:
        print(f"[ERRO] Erro na detecção de frame: {e}")
        return None
