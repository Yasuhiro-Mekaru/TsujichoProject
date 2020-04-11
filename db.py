import mysql.connector
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_HOST = "us-cdbr-iron-east-04.cleardb.net"
DB_USERNAME = "b00f214264a795"
DB_PASSWORD = "9e5fc725"
DB_DATABASE = "heroku_60fc588795e8645"


class Db(object):

    """
    seatMasterを呼び出す処理
    """
    def post_seat(language, seats):
        logger.info({
            'action': 'get_db',
            'language': language,
            'seats': seats
        })
        # conn = mysql.connector.connect(host='localhost', user='root', use_pure=True,database='tsujicho_db')
        # conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD , use_pure=True, database=DB_DATABASE)
        conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATABASE)
        cursol = conn.cursor()
        logger.info({
            'action': 'get_db',
            'cursol': 'run'
        })
        datas = []
        cursol.execute('SELECT seatType, description, src FROM seatMaster WHERE languageId="{}" AND seatId="{}"'
                       .format(language, seats[0]))
        for row in cursol:
            logger.info({
                'action': 'get_db for',
                'data': row
            })
            print(row)
            datas.append(row)
        cursol.execute('SELECT seatType, description, src FROM seatMaster WHERE languageId="{}" AND seatId="{}"'
                       .format(language, seats[1]))
        for row in cursol:
            logger.info({
                'action': 'get_db for',
                'data': row
            })
            print(row)
            datas.append(row)
        conn.commit()
        cursol.close()
        conn.close()
        logger.info({
            'action': 'get_db return',
            'data': datas,
            'data type': type(datas)
        })
        return datas



    def post_menu(language, category, types):
        logger.info({
            'action': 'get_db',
            'language': language,
            'category': category,
            'type': types
        })
        # conn = mysql.connector.connect(host='localhost', user='root', use_pure=True, database='tsujicho_db')
        # conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD , use_pure=True, database=DB_DATABASE)
        conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATABASE)
        cursol = conn.cursor()
        logger.info({
            'action': 'get_db',
            'cursol': 'run'
        })
        datas = []
        cursol.execute(
            'SELECT name, description, src FROM menuMaster WHERE languageId="{}" AND category="{}" AND type={}'
                .format(language, category, types))
        for row in cursol:
            logger.info({
                'action': 'get_db for',
                'data': row
            })
            print(row)
            datas.append(row)
        cursol.close()
        conn.close()
        logger.info({
            'action': 'get_db return',
            'data': datas,
            'data type': type(datas)
        })

        return datas



    """
    DBの全データを取得する処理
    第一引数はDBのTable名
    """
    def get_all_menu(table, id=0):
        logger.info({
            'action': 'get_all_menu',
            'data': table,
            'id': id
        })
        # conn = mysql.connector.connect(host='localhost', user='root', use_pure=True, database='tsujicho_db')
        # conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD , use_pure=True, database=DB_DATABASE)
        conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATABASE)
        cursol = conn.cursor()
        logger.info({
            'action': 'get_all_menu',
            'cursol': 'run',
            'id': id
        })
        datas = []
        if table:
            if id == 0:
                cursol.execute('SELECT * FROM {}'.format(table))
                for row in cursol:
                    logger.info({
                        'action': 'get_db for if',
                        'data': row
                    })
                    datas.append(row)
            elif id != 0:
                cursol.execute('SELECT category, type, name, price, description FROM {} WHERE languageID={}'.format(table, id))
                for row in cursol:
                    menu_data = {}
                    logger.info({
                        'action': 'get_db for elif',
                        'data': row
                    })
                    menu_category = row[0]
                    menu_type = row[1]
                    menu_name = row[2]
                    menu_price = row[3]
                    menu_description = row[4]

                    menu_data['category'] = menu_category
                    menu_data['type'] = menu_type
                    menu_data['name'] = menu_name
                    menu_data['price'] = menu_price
                    menu_data['description'] = menu_description

                    datas.append(menu_data)
        else:
            cursol.execute('SELECT * FROM {}'.format(table))
            for row in cursol:
                logger.info({
                    'action': 'get_db for else',
                    'data': row
                })
                datas.append(row)
        conn.commit()
        cursol.close()
        conn.close()
        logger.info({
            'action': 'get_all_menu return',
            'data': datas,
            'data type': type(datas)
        })

        return datas



    """
    特定の行のデータを更新する処理
    """
    def put_menu_data(data):
        logger.info({
            'action': 'put_menu_data',
            'data': data
        })
        id = data['id']
        language = data['language']
        category = data['category']
        types = data['type']
        name = data['name']
        price = data['price']
        description = data['description']
        src = data['src']

        # conn = mysql.connector.connect(host='localhost', user='root', use_pure=True, database='tsujicho_db')
        # conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD , use_pure=True, database=DB_DATABASE)
        conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATABASE)
        cursol = conn.cursor()
        logger.info({
            'action': 'put_menu_data mysql',
            'cursol': 'run',
            'data': id
        })

        datas = []
        cursol.execute(
            'UPDATE menuMaster SET languageId="{}", category="{}", type="{}", name="{}", price="{}", description="{}", src="{}" WHERE id="{}"'
                       .format(language, category, types, name, price, description, src, id))
        conn.commit()
        cursol.close()
        conn.close()
        logger.info({
            'action': 'put_menu_data mysql return',
            'data': datas,
            'data type': type(datas)
        })

        return datas


    """
    新しい行を作成する処理
    """
    def post_menu_data(data):
        logger.info({
            'action': 'post_menu_data',
            'data': data
        })
        id = data['id']
        language = data['language']
        category = data['category']
        types = data['type']
        name = data['name']
        price = data['price']
        description = data['description']
        src = data['src']

        # conn = mysql.connector.connect(host='localhost', user='root', use_pure=True, database='tsujicho_db')
        # conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD , use_pure=True, database=DB_DATABASE)
        conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATABASE)
        cursol = conn.cursor()
        logger.info({
            'action': 'post_menu_data mysql',
            'cursol': 'run',
            'data': id
        })
        datas = []
        cursol.execute('INSERT into menuMaster(languageId, category, type, name, price, description, src)'
                        ' Values("{}", "{}", "{}", "{}", {}, "{}", "{}")'.format(
                        language, category, types, name, price, description, src))
        conn.commit()
        cursol.close()
        conn.close()
        logger.info({
            'action': 'put_menu_data mysql return',
            'data': datas,
            'data type': type(datas)
        })

        return datas


    """
    特定の行を削除する処理
    """
    def delete_menu_data(data):
        logger.info({
            'action': 'delete_menu_data',
            'data': data
        })
        id = data
        # conn = mysql.connector.connect(host='localhost', user='root', use_pure=True, database='tsujicho_db')
        # conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD , use_pure=True, database=DB_DATABASE)
        conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATABASE)
        cursol = conn.cursor()
        logger.info({
            'action': 'put_menu_data mysql',
            'cursol': 'run',
            'data': data
        })
        datas = []
        cursol.execute('DELETE FROM menuMaster WHERE id="{}"'.format(id))
        conn.commit()
        cursol.close()
        conn.close()

        logger.info({
            'action': 'delete_menu_data mysql return',
            'data': datas,
            'data type': type(datas)
        })

        return datas


    """
    予約データを登録する処理
    """
    def post_reservation(data):
        logger.info({
            'action': 'post_reservation',
            'data': data
        })

        name = data['name']
        address = data['address']
        time = data['time']
        number = data['number']
        course = data['course']
        description = data['description']

        # conn = mysql.connector.connect(host='localhost', user='root', use_pure=True, database='tsujicho_db')
        # conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD , use_pure=True, database=DB_DATABASE)
        conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATABASE)
        cursol = conn.cursor()
        logger.info({
            'action': 'post_reservation',
            'cursol': 'run'
        })
        datas = []
        cursol.execute('INSERT into reservation(name, address, time, number, course, description)'
                       ' Values("{}", "{}", "{}", "{}", "{}", "{}")'.format(
            name, address, time, number, course, description))
        conn.commit()
        cursol.close()
        conn.close()
        logger.info({
            'action': 'post_reservation mysql return',
            'data': datas,
            'data type': type(datas)
        })

        return datas



