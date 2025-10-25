import cv2
import numpy as np
from pathlib import Path

# --- Configuración de archivos ---
modelo_zip = "/home/user/ia_carteles_V1/best_imx_model/packerOut.zip"
labels_file = "/home/user/ia_carteles_V1/best_imx_model/labels.txt"

# Leer etiquetas
with open(labels_file, "r", encoding="utf-8") as f:
    labels = [line.strip() for line in f.readlines()]

# --- Funciones de detección (simuladas para IMX500) ---
# NOTA: Aquí se requiere usar el API del rpicam-apps/imx500-postproc si existiera acceso a Python.
# Como ejemplo, vamos a capturar video con OpenCV y simular detecciones.

cap = cv2.VideoCapture(0)  # Cámara predeterminada

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara")
    exit()

# Colores para cada clase
colors = np.random.randint(0, 255, size=(len(labels), 3), dtype=int)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # --- Aquí va la llamada al NPU del IMX500 ---
    # Por ahora simulamos detecciones: lista de diccionarios
    # Ejemplo: [{'label_id': 0, 'confidence': 0.87, 'bbox': [x1,y1,x2,y2]}]
    detecciones = []  # <-- Aquí se llenaría con resultados reales

    # Dibujar detecciones
    for det in detecciones:
        x1, y1, x2, y2 = det['bbox']
        label_id = det['label_id']
        conf = det['confidence']
        color = [int(c) for c in colors[label_id]]
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        texto = f"{labels[label_id]} {conf:.2f}"
        cv2.putText(frame, texto, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    cv2.imshow("Detección Carteles", frame)

    key = cv2.waitKey(1)
    if key == 27:  # ESC para salir
        break

cap.release()
cv2.destroyAllWindows()
