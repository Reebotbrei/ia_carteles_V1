🦯 Detector de Franjas de Seguridad para Personas con Discapacidad Visual

Este proyecto tiene como objetivo desarrollar un sistema de detección de franjas de seguridad que sirva como apoyo para personas con discapacidad visual.
El sistema es capaz de identificar las franjas o señales de seguridad en el entorno (como zonas seguras, salidas de emergencia, áreas restringidas, entre otras) y emitir alertas sonoras o de voz para comunicar la información detectada.

🚀 Objetivo del Proyecto

Diseñar e implementar un sistema inteligente de visión artificial que detecte franjas o señales de seguridad en tiempo real y las comunique de forma accesible e intuitiva a las personas con discapacidad visual.

🧠 Descripción General

El detector utiliza técnicas de inteligencia artificial y visión por computadora, basadas en modelos YOLO (You Only Look Once), para reconocer señales de seguridad establecidas en la norma NTP 399.010-1:2016.
Al identificar una señal, el sistema convierte el resultado en salida de texto y audio, facilitando la comprensión de la información por parte del usuario.

🧩 Funcionalidades

🔍 Detección en tiempo real de franjas y señales de seguridad.

🔈 Conversión automática de texto a voz (TTS) para asistencia auditiva.

📱 Envío de resultados a una aplicación móvil (texto y audio).

🧩 Interfaz amigable para usuarios y administradores.

⚙️ Compatibilidad con cámaras y módulos embebidos (Raspberry Pi, ESP32-CAM, etc.).

🧰 Tecnologías Utilizadas
Tipo	Tecnologías
Lenguajes	Python, Dart
Frameworks	Flutter (para la app móvil)
IA / Visión	Ultralytics YOLOv11
Hardware	Raspberry Pi / IA Cámara Raspberry pi
Audio	pyttsx3 / gTTS
Comunicación	Socket / MQTT / HTTP según configuración
Interfaz	Flutter UI con vistas para usuario y administrador
