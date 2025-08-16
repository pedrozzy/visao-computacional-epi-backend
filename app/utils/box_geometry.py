def box_area(x1, y1, x2, y2):
    """Calcula a área de uma caixa delimitadora."""
    return max(0, x2 - x1) * max(0, y2 - y1)

def intersection_area(boxA, boxB):
    """Calcula a área de interseção entre duas caixas."""
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    width = max(0, xB - xA)
    height = max(0, yB - yA)

    return width * height

def iou(boxA, boxB):
    """
    Calcula a IoU (Intersection over Union) entre duas caixas.
    Retorna um valor entre 0 e 1.
    """
    inter = intersection_area(boxA, boxB)
    if inter == 0:
        return 0.0

    areaA = box_area(*boxA)
    areaB = box_area(*boxB)

    union = areaA + areaB - inter
    return inter / union if union > 0 else 0.0
