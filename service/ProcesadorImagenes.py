import base64
import cv2
import numpy as np
import os

directorio_guardado = "static\DataSet"


class ProcesadorImagenes:

    # def __init__(self, imagenes=None):
    #     self.imagenes = imagenes

    def __init__(self, imagen=None):
        self.imagen = imagen

    def data_uri_to_cv2_img(self, uri):
        encoded_data = uri.split(',')[1]
        # Matriz que hace referencia a la imagen que viene en formato base 64
        nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
        # Transformacion de la imagen a un formato Matricial entendible para opencv
        # img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img

    # def obtener_imagen(self):
    #     for imagen in self.imagenes:
    #         if len(imagen) % 4 != 0:  # check if multiple of 4
    #             while len(imagen) % 4 != 0:
    #                 imagen = imagen + "="
    #         img = self.data_uri_to_cv2_img(imagen)

    # def obtener_imagenes(self):
    #     imagenes_encoded = []
    #     for imagen in self.imagenes:
    #         if len(imagen) % 4 != 0:  # check if multiple of 4
    #             while len(imagen) % 4 != 0:
    #                 imagen = imagen + "="
    #         img = self.data_uri_to_cv2_img(imagen)
    #         imagenes_encoded.append(img)
    #     return imagenes_encoded

    def obtener_imagen(self):
        if len(self.imagen) % 4 != 0:  # check if multiple of 4
            while len(self.imagen) % 4 != 0:
                self.imagen = self.imagen + "="
        img = self.data_uri_to_cv2_img(self.imagen)
        return img


    # def guardarImagenes(self, dir, usuario):
    #     photos = 1
    #     for imagen in self.imagenes:
    #         if len(imagen) % 4 != 0:  # check if multiple of 4
    #             while len(imagen) % 4 != 0:
    #                 imagen = imagen + "="
    #         self.guadar_imagen(dir, usuario["id"], imagen, photos)
    #         photos += 1

    def guardarImagen(self, dir, usuario):
        print(self.imagen)
        if len(self.imagen) % 4 != 0:  # check if multiple of 4
            while len(self.imagen) % 4 != 0:
                self.imagen = self.imagen + "="
        self.guadar_imagen(dir, usuario["id"], self.imagen, 1)


    def leer_imagen(self, imagen):
        cv2.imshow("imagen", imagen)
        cv2.waitKey(0)

    def guardar_usuario(self, docente, db):
        db.session.add(docente)
        db.session.commit()
        db.session.refresh(docente)
        return docente

    def guadar_imagen(self, dir, usuario, imagen, orden):
        ruta_recursos = os.path.join(dir, directorio_guardado)
        ruta_nuevo_usuario = os.path.join(ruta_recursos, str(usuario))
        if not os.path.isdir(ruta_nuevo_usuario):
            os.mkdir(ruta_nuevo_usuario)

        encoded_data = imagen.split(',')[1]
        imgdata = base64.b64decode(encoded_data)
        # I assume you have a way of picking unique filenames
        filename = os.path.join(ruta_nuevo_usuario, str(usuario) + "_" + str(orden) + '.jpg')
        with open(filename, 'wb') as f:
            f.write(imgdata)











