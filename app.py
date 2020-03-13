from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///banco.db' # Informa o tipo de banco que será utilizado
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Evita sobrecarregar a aplicação sem o rastreio de modificações 
api = Api(app)

@app.before_first_request
def create_database():
    db.create_all() # Cria automáticamente o banco e todas as tabelas

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__ == '__main__': #Quando for iniciado por linha de comando o serviço devera iniciar o servidor para executar a aplicação
    from sql_alchemy import db
    db.init_app(app)
    app.run(host='0.0.0.0', debug=True, port=8081)