from flask import request, jsonify
from app.models.uppercase_model import UppercaseModel
from app.services.uppercase_service import UppercaseService

MAX_FILE_SIZE = 2 * 1024 * 1024 #2MB

class UppercaseController:
    
    @staticmethod
    def count_uppercase():

        # validar que sea un archivo
        if 'file' not in request.files:
            return jsonify({"error": "no se envió un archivo"}), 400

        file = request.files['file']

        # validar nombre
        if not file.filename:
            return jsonify({"error": "el archivo no tiene nombre"}), 400

        # validar extension
        if not file.filename.endswith(('.txt')):
            return jsonify({"error": "el archivo debe tener una extensión .txt"}), 400

        # validar el tamaño
        file.stream.seek(0, 2)
        file_size = file.stream.tell()
        file.stream.seek(0)

        if file_size > MAX_FILE_SIZE:
            return jsonify({"error": "el archivo supera el tamaño máximo de 2MB"}), 400
        
        model = UppercaseModel(file.filename, file)

        try: 
            count = UppercaseService.count_uppercase(file)

            return jsonify({
                "filename": model.filename,
                "count": count,
                "status": "success"
            }), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
