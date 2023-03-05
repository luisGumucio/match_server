from flask import Flask
import pocketbase_config as pocketbaseClient
from services.actions_services import ActionsService
app = Flask(__name__)
client = pocketbaseClient.init()
actionsService = ActionsService(client)

@app.route('/actions/<id>')
def actions(id):
    actionsService.generate_standings(id)
    return 'Hola, mundo!'

if __name__ == '__main__':
    app.run(port=8086, debug=True)
