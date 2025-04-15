import cv2
import numpy as np

# Crear una imagen de gradiente (0 a 255 en horizontal)
height, width = 200, 512
gradient = np.linspace(0, 255, width, dtype=np.uint8)
gray_image = np.tile(gradient, (height, 1))

# Aplicar un mapa de color (ejemplo: INFERNO)
colored_image = cv2.applyColorMap(gray_image, cv2.COLORMAP_INFERNO)

# Mostrar las imágenes
cv2.imshow('Grayscale Gradient', gray_image)
cv2.imshow('ColorMap - INFERNO', colored_image)

# Esperar tecla y cerrar ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()


