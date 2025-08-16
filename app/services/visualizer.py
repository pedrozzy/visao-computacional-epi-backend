import cv2

def draw_annotations(frame, heads_com_capacete, heads_sem_capacete):
    # Verde: Capacete: OK
    for pair in heads_com_capacete:
        x1, y1, x2, y2 = pair['head']
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, "Capacete: OK", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Vermelho: Capacete: FALTA
    for x1, y1, x2, y2 in heads_sem_capacete:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(frame, "Capacete: FALTA", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    return frame