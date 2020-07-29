from flask import Flask
from flask_restful import Resource, Api

from controller.AuthorController import AuthorController
from controller.AuthorListController import AuthorListController


app = Flask(__name__)
api = Api(app)

api.add_resource(AuthorListController,'/api/author')
api.add_resource(AuthorController,'/api/author/<id>')

app.run(port=5000, debug=True)