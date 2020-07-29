import pymysql.cursors

connection = pymysql.connect(host='localhost',
							 user='root',
							 password='root123',
							 db='blog_1',
							 charset='utf8mb4',
							 cursorclass=pymysql.cursors.DictCursor) 

try:
	# Write
	# with connection.cursor() as cursor:
	# 	sql = "INSERT INTO `author` (`name`, `email`) VALUES (%s, %s)"
	# 	cursor.execute(sql, ('Anusree PS', 'anusree2@gmail.com'))

	# connection.commit()

	# Read
	# with connection.cursor() as cursor:
	# 	sql = "SELECT * FROM `author`"
	# 	cursor.execute(sql)
	# 	result = cursor.fetchall()
	# 	print(result)

except:
	print("An error occured while executing DB query")
finally:
	connection.close()

