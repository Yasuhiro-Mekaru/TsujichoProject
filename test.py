import mysql.connector


# Create DataBase
# conn = mysql.connector.connect(host='localhost', user='root', use_pure=True)
# cursol = conn.cursor()
# cursol.execute('CREATE DATABASE tsujicho_db')
# cursol.close()
# conn.close()



# Create Table
# conn = mysql.connector.connect(host='localhost', user='root', use_pure=True, database='tsujicho_db')
# cursol = conn.cursor()
# cursol.execute('CREATE TABLE reservation('
#                'id int NOT NULL AUTO_INCREMENT,'
#                'name varchar(30) NOT NULL,'
#                'address int NOT NULL,'
#                'time varchar(30) NOT NULL,'
#                'number int NOT NULL,'
#                'course int,'
#                'detail varchar(100) NOT NULL,'
#                'PRIMARY KEY(id))'
#                )
# conn.commit()
# cursol.close()
# conn.close()



# Insert
# conn = mysql.connector.connect(host='localhost', user='root', use_pure=True, database='tsujicho_db')
# cursol = conn.cursor()
# cursol.execute('INSERT into menuMaster(languageId, category, type, name, price, description, src)'
#                ' Values(1, 2, 1, "串焼き", 130, "xxxxxxx", "/static/img/skewers2.jpg")')
# conn.commit()
# cursol.close()
# conn.close()


# Delete
# conn = mysql.connector.connect(host='localhost', user='root', use_pure=True, database='tsujicho_db')
# cursol = conn.cursor()
# cursol.execute('DELETE FROM menuMaster WHERE id=4')
# conn.commit()
# cursol.close()
# conn.close()



# Select
# conn = mysql.connector.connect(host='localhost', user='root', use_pure=True, database='test_tsujicho')
# cursol = conn.cursor()
# cursol.execute('SELECT * FROM menus WHERE name="Kushimori"')
# for row in cursol:
#     print(row)
# cursol.close()
# conn.close()





