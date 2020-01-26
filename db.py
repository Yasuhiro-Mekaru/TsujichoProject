import mysql.connector
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
        conn = mysql.connector.connect(host='localhost', user='root', use_pure=True, database='tsujicho_db')
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
        conn = mysql.connector.connect(host='localhost', user='root', use_pure=True, database='tsujicho_db')
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
    def get_all_menu(table):
        logger.info({
            'action': 'get_all_menu',
            'data': table
        })
        conn = mysql.connector.connect(host='localhost', user='root', use_pure=True, database='tsujicho_db')
        cursol = conn.cursor()
        logger.info({
            'action': 'get_all_menu',
            'cursol': 'run'
        })
        datas = []
        if table:
            cursol.execute('SELECT * FROM {}'.format(table))
            for row in cursol:
                logger.info({
                    'action': 'get_db for if',
                    'data': row
                })
                datas.append(row)
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

        conn = mysql.connector.connect(host='localhost', user='root', use_pure=True, database='tsujicho_db')
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

        conn = mysql.connector.connect(host='localhost', user='root', use_pure=True, database='tsujicho_db')
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
        conn = mysql.connector.connect(host='localhost', user='root', use_pure=True, database='tsujicho_db')
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

        conn = mysql.connector.connect(host='localhost', user='root', use_pure=True, database='tsujicho_db')
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


