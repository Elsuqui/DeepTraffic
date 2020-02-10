from flask import Flask, request, jsonify
from service.ProcesadorImagenes import ProcesadorImagenes
from flask_marshmallow import Marshmallow
import os

directorio_base = os.getcwd()

# Proceso Inicial para precargar el modelo de Red Neuronal y los rostros que estan en la base de datos
# casco_recognizer = FirstPredictor(os.path.join(directorio_base, "static/DataSet"))
print(os.path.join(directorio_base, "static/DataSet"))
# casco_recognizer.cargarModelo()
# casco_recognizer.mapearBaseDatos()

app = Flask(__name__)
ma = Marshmallow(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/procesar-imagen', methods=['POST'])
def procesar_imagen():
    data = request.get_json()
    imagenes = data["imagenes"]
    procesador = ProcesadorImagenes(imagenes)
    imagenes_coded = procesador.obtener_imagen()
    # Primero se predice por el numero de personas
    # resultado = recognizer.realizarReconocimiento(imagenes_coded)
    # Segundo se predice por el uso de casco
    casco = {}
    # if resultado == 0:
    #    print("El docente no esta registrado en la base de datos")
    # else:
    #    print("El docente ha sido reconocido como: " + resultado)
    #    usuario_db = Docente.query.get(resultado)
    #    # Si esto es None no hay resultados
    #    print(usuario_db)
    #    usuario_db.request = True
    #   usuario_db.validatorKey = secrets.token_urlsafe(32)
    #    db.session.commit()
    #    usuario_obj = DocenteSchema().dump(usuario_db).data
    #    print(usuario_obj)
    #    usuario = usuario_obj

    return jsonify(casco)


if __name__ == '__main__':
    app.run()
