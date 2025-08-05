import cv2

# Cargar imagen en escala de grises
imagen = cv2.imread("imagen.jpg")

# Verifica si se cargó correctamente
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar detector de bordes Canny
bordes = cv2.Canny(imagen, threshold1=100, threshold2=200)

# Mostrar la imagen original y el resultado
cv2.imshow("Imagen original", imagen)
cv2.imshow("Bordes con Canny", bordes)

# Esperar una tecla y cerrar ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
