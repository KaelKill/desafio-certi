from flask import Flask, request, g
from flask_babel import Babel, _
import json

from number_handler import Number_Handler
 
app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    if not g.get('lang_code', None):
        translations = ['pt', 'en']
        g.lang_code = request.accept_languages.best_match(translations)
    return g.lang_code

@app.route('/')
def home():
    return _("Ola")

@app.route('/<lang>/<number>', methods=['GET'])
@app.route('/<number>', methods=['GET'])
def index(number, lang='pt'):
    g.lang_code = lang
    if not number.isdigit():
        return _("Argumento invalido")

    if int(number) < -99999 or int(number) > 99999:
        return _("Número fora do intervalo")

    nh = Number_Handler(number)
    resp = dict()
    resp[_('extenso')] = nh.written_form

    return json.dumps(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0')