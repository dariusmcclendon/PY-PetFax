from flask import (Blueprint, render_template)
bp = Blueprint('pet',__name__,url_prefix="/pets")

import json
pets = json.load(open('pets.json'))


@bp.route('/')
def index():
    return render_template('index.html',pets=pets)