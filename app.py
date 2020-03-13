from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel

app = Flask(__name__)
api = Api(app) 

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__ == '__main__': #Quando for iniciado por linha de comando o serviço devera iniciar o servidor para executar a aplicação
    app.run(host='0.0.0.0', debug=True, port=8081)