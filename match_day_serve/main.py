from flask import Flask, request
import pocketbase_config as pocketbaseClient
from services.actions_services import ActionsService
app = Flask(__name__)
client = pocketbaseClient.init()
actionsService = ActionsService(client)

@app.route('/actions/<id>')
def actions(id):
    actionsService.generate_standings(id)
    return 'Hola, mundo!'
@app.route('/saludo')
def saludo():
    return 'Hola como estas'


@app.route('/enviar', methods=['POST'])
def enviar():
    datos = request.get_json() # obtiene los datos de la solicitud POST
    # Aquí procesas los datos recibidos y retornas una respuesta
    return datos




if __name__ == '__main__':
    app.run(port=8086, host='0.0.0.0', debug=True)

