from flask_restful import Resource
from flask import request
from entity.Author import Author

class AuthorController(Resource):
	def get(self,id):
		return Author.getById(id)

	def delete(self, id):
		return Author.deleteById(id)

	def put(self, id):
		data = request.get_json()
		name = data['name']
		email = data['email']
		return Author.updateById(id, name, email)