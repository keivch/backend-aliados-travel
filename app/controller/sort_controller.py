from flask import request, jsonify
from app.models.sort_model import SortModel
from app.services.sort_service import SortService

class SortController:

    @staticmethod
    def sort_numbers():

        data = request.get_json(silent=True)

        if not isinstance(data, dict) or data is None:
            return jsonify({"error": "se debe enviar un formato json"}), 400

        numbers = data.get("numbers")

        if not isinstance(numbers, list):
            return jsonify({"error": "se debe enviar una lista de números"}), 400

        if any(
            isinstance(n, bool) or not isinstance(n, (int, float))
            for n in numbers
        ):
            return jsonify({"error": "se deben enviar solo números"}), 400

        model = SortModel(numbers)

        sorted_numbers = SortService.merge_sort(numbers)

        return jsonify({
            "original: ": model.numbers,
            "sorted: ": sorted_numbers,
            "algoritmo": "merge sort",
            "status": "success"
        }), 200