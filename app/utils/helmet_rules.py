from app.utils.box_geometry import intersection_area, box_area

def check_helmet_warnings(persons, helmets, iou_threshold=0.3):
    warnings = []
    for px1, py1, px2, py2 in persons:
        head_box = (px1, py1, px2, py1 + (py2 - py1) // 2)
        has_helmet = False
        for hx1, hy1, hx2, hy2 in helmets:
            inter_area = intersection_area(head_box, (hx1, hy1, hx2, hy2))
            helmet_area = box_area(hx1, hy1, hx2, hy2)
            if helmet_area == 0:
                continue
            iou = inter_area / helmet_area
            if iou > iou_threshold:
                has_helmet = True
                break
        if not has_helmet:
            warnings.append({
                "x1": px1, "y1": py1, "x2": px2, "y2": py2,
                "warning": "Sem capacete"
            })
    return warnings