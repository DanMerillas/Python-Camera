import cv2

# Inicializar la cámara (0 es para la cámara predeterminada)
cap = cv2.VideoCapture(0)


# Bucle para leer y mostrar las imágenes en tiempo real
while True:
    # Leer un frame de la cámara
    ret, frame = cap.read()

    # Verificar si el frame fue leído correctamente
    if not ret:
        print("No se pudo leer el frame")
        break

    # Mostrar el frame en una ventana
    cv2.imshow('Imagen normal', frame)

      # Convertir la imagen a escala de grises
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Mostrar el frame en escala de grises en una ventana
    cv2.imshow('Imagen en escala de grises', gray_frame)

          # Convertir la imagen a HSV
    gray_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Mostrar el frame en HSV
    cv2.imshow('Imagen en escala de HSV', gray_HSV)

    # Esperar 1 ms y salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
