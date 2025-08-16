from ultralytics import YOLO

model_capacete = YOLO("app/models/best.pt")
model_pessoa = YOLO("app/models/yolov8s.pt")

class_names_capacete = model_capacete.model.names
class_names_pessoa = model_pessoa.model.names