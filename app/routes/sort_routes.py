from flask import Blueprint
from app.controller.sort_controller import SortController

sort_bp = Blueprint('sort', __name__)

sort_bp.route('/sort',methods=['POST'])(SortController.sort_numbers)