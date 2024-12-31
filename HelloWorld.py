import cv2

# PASO 1: LEER UNA IMAGEN
ruta_imagen = "./images/Python.png"  # Reemplaza con la ruta de tu imagen
imagen = cv2.imread(ruta_imagen)

# VERIFICAR SI LA IMAGEN SE CARGÓ CORRECTAMENTE
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta.")
else:
    # PASO 2: MOSTRAR LA IMAGEN
    cv2.imshow("Imagen Cargada", imagen)

    # PASO 3: ESPERAR A QUE EL USUARIO CIERRE LA VENTANA
    cv2.waitKey(0)  # Presiona cualquier tecla para cerrar
    cv2.destroyAllWindows()
