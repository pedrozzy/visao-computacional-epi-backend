from app.utils.box_geometry import iou

def get_head_regions(results_pessoa):
    """Extrai regiões da cabeça a partir das caixas da classe 'person'."""
    head_regions = []
    for box in results_pessoa.boxes:
        if int(box.cls[0]) == 0:  # classe 'person'
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            head_h = int((y2 - y1) * 0.35)  # Assume o topo como região da cabeça
            head_regions.append([x1, y1, x2, y1 + head_h])
    return head_regions

def get_capacete_detections(results_cap, conf_threshold=0.7):
    """Filtra as caixas da classe 'capacete' com confiança suficiente."""
    detections = []
    for box in results_cap.boxes:
        conf = float(box.conf[0])
        if conf >= conf_threshold:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            detections.append({
                'bbox': [x1, y1, x2, y2],
                'conf': conf
            })
    return detections

def match_helmets_to_heads(heads, helmets, iou_threshold=0.25):
    """Relaciona capacetes às cabeças com base na IoU."""
    matched = []
    used_helmets = set()

    for head in heads:
        best_match = None
        best_iou = 0

        for idx, helmet in enumerate(helmets):
            if idx in used_helmets:
                continue

            iou_val = iou(head, helmet['bbox'])
            if iou_val > iou_threshold and iou_val > best_iou:
                best_match = (idx, helmet)
                best_iou = iou_val

        if best_match:
            helmet_idx, helmet_data = best_match
            used_helmets.add(helmet_idx)
            matched.append({
                "head": head,
                "helmet": helmet_data
            })

    return matched

def find_heads_without_helmets(heads, matched_pairs):
    """Retorna as cabeças que não possuem capacetes correspondentes."""
    matched_heads = {tuple(m['head']) for m in matched_pairs}
    return [head for head in heads if tuple(head) not in matched_heads]
