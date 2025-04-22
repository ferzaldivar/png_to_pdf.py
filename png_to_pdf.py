import os
import img2pdf

#--------------------------
#
# UBICACION DE LAS IMAGENES
#
#--------------------------
carpeta_imagenes = './Imagenes'

# Listado de las imagenes
lista_imagenes = []

# Agrega las imagenes al listado
for archivo in os.listdir(carpeta_imagenes):
    if archivo.endswith(('.jpg', 'jpeg', '.png')):
        ruta_completa = os.path.join(carpeta_imagenes, archivo)
        lista_imagenes.append(ruta_completa)

# Ordena las imagenes por nombre. Deben tener dos digitos (01, 02, 20, 30, etc). Para agregar una imagen intermedia: Ej a 02 le sigue 021, 022, etc 
lista_imagenes.sort()

#--------------------------
#
# NOMBRE DEL ARCHIVO pdf final
#
#--------------------------
archivo_pdf = 'Imagenes.pdf'

# Crea el pdf
with open(archivo_pdf, 'wb') as f:
    f.write(img2pdf.convert(lista_imagenes))
    
