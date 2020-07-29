from flask_restful import Resource
from flask import request
from entity.Author import Author

class AuthorListController(Resource):
	def get(self):
		return Author.all()

	def post(self):
		data = request.get_json()
		name = data['name']
		email = data['email']
		return Author.create(name, email)