from helpers.connection_helper import ConnectionHelper

authors = [{
	'id': 1,
	'name':'anusree',
	'email':'anusreesubash@gmail.com'
}]

id = 2;

def findAuthorById(id):
	global authors
	return next((x for x in authors if x['id'] == int(id)), None)

class Author():
	def all():
		connectionHelper = ConnectionHelper()
		connection = connectionHelper.getConnection()

		with connection.cursor() as cursor:
			sql = "SELECT * FROM `author`"
			cursor.execute(sql)
			result = cursor.fetchall()
			connection.close();
			return result
		

	def create(name, email):
		connectionHelper = ConnectionHelper()
		connection = connectionHelper.getConnection()

		with connection.cursor() as cursor:
			sql = "INSERT INTO `author` (`name`, `email`) VALUES (%s, %s)"
			cursor.execute(sql, (name, email))
			

		connection.commit()
		connection.close();

	def getById(id):
		connectionHelper = ConnectionHelper()
		connection = connectionHelper.getConnection()

		with connection.cursor() as cursor:
			sql = "SELECT * FROM `author` WHERE `id` = %s"
			cursor.execute(sql, (id))
			result = cursor.fetchone()
			connection.close();
			return result
		

	def deleteById(id):
		connectionHelper = ConnectionHelper()
		connection = connectionHelper.getConnection()

		with connection.cursor() as cursor:
			sql = "DELETE FROM `author` WHERE id = %s"
			cursor.execute(sql, (id))
			
		connection.commit()
		connection.close();
		return ({'message':'author removed'})

	def updateById(id, name, email):
		connectionHelper = ConnectionHelper()
		connection = connectionHelper.getConnection()

		with connection.cursor() as cursor:
			sql = "UPDATE `author` SET `name` = %s, `email` = %s WHERE id = %s"
			cursor.execute(sql, (name, email, id))
			

		connection.commit()
		connection.close();
