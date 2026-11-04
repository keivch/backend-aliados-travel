from flask import Blueprint
from app.controller.uppercase_controller import UppercaseController

uppercase_bp = Blueprint('uppercase', __name__)

uppercase_bp.route('/uppercase', methods = ['POST'])(UppercaseController.count_uppercase)