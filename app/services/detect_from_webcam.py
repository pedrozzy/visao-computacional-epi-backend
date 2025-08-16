import cv2
import numpy as np
from flask import Response
from PIL import Image

from app.models.yolo_models import model_capacete, model_pessoa
from app.services.detectors import (
    get_head_regions, get_capacete_detections,
    match_helmets_to_heads, find_heads_without_helmets
)
from app.services.visualizer import draw_annotations

def get_working_camera(max_index=5):
    """Tenta encontrar uma câmera funcional testando diferentes backends."""
    for i in range(max_index):
        for backend in [cv2.CAP_DSHOW, cv2.CAP_MSMF, cv2.CAP_V4L2, 0]:
            cap = cv2.VideoCapture(i, backend)
            if cap.isOpened():
                print(f"[INFO] Câmera encontrada no índice {i} com backend {backend}")
                return cap
            cap.release()
    return None

def detect_from_frame(frame_bgr):
    """Processa um frame: detecção, correspondência e anotação."""
    try:
        # Conversão direta para RGB sem PIL para performance
        frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)

        # Inferência
        results_cap = model_capacete(frame_rgb)[0]
        results_pessoa = model_pessoa(frame_rgb)[0]

        # Processamento lógico
        heads = get_head_regions(results_pessoa)
        helmets = get_capacete_detections(results_cap)
        matched = match_helmets_to_heads(heads, helmets)
        missing = find_heads_without_helmets(heads, matched)

        # Anotações visuais
        annotated = draw_annotations(frame_bgr, matched, missing)
        return annotated

    except Exception as e:
        print(f"[ERRO] Falha ao processar frame: {e}")
        return frame_bgr  # Retorna o frame original se falhar

def generate_frames_from_camera():
    """Gera frames contínuos da câmera com as anotações em tempo real."""
    cap = get_working_camera()
    if cap is None:
        raise RuntimeError("Nenhuma câmera disponível")

    try:
        while True:
            success, frame = cap.read()
            if not success:
                print("[ERRO] Falha ao ler frame da câmera")
                break

            annotated = detect_from_frame(frame)
            ret, buffer = cv2.imencode(".jpg", annotated)

            if not ret:
                print("[ERRO] Falha ao codificar frame em JPEG")
                continue

            yield (b"--frame\r\n"
                   b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n")
    finally:
        cap.release()
        print("[INFO] Câmera liberada")
