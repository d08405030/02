from flask_restful import Resource,reqparse
import pymysql
from flask import jsonify

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('gender')
parser.add_argument('note')
parser.add_argument('birth')

class User(Resource):
    def db_init(self):
        db = pymysql.connect('localhost','root','123456','api')
        cursor = db.cursor(pymysql.cursors.DictCursor)

        return db, cursor
    def get(self,id):
        db, cursor = self.db_init()
        sql = """SELECT * FROM api.users WHERE id={}""".format(id)
        cursor.execute(sql)
        db.commit()
        user = cursor.fetchone()
        db.close()

        return jsonify({'data':user})
    def delete(self,id):
        db, cursor = self.db_init()
        sql = """UPDATE api.users SET deleted=1 WHERE id ={}""".format(id)
        cursor.execute(sql)
        response = {}
        try:
            cursor.execute(sql)
            response['msg'] = 'Success'
        except:
            response['msg'] = 'Failed'
        db.commit()
        db.close()
        return jsonify(response)


class Users(Resource):
    def db_init(self):
        db = pymysql.connect('localhost','root','123456','api')
        cursor = db.cursor(pymysql.cursors.DictCursor)

        return db, cursor
    
    def get(self):
        db, cursor = self.db_init()
        sql = 'SELECT * FROM api.users'
        cursor.execute(sql)
        db.commit()
        users = cursor.fetchall()
        db.close()

        return jsonify({'data':users})

    def post(self):
        db, cursor = self.db_init()
        arg = parser.parse_args()
        user = {
            'name' : arg['name'],
            'gender' : arg['gender'],
            'note' : arg['note'],
            'birth' : arg['birth'],
        }
        sql = """
            INSERT INTO `api`.`users` (`name`, `gender`, `note`, `birth`)
            VALUES ('{}', '{}', '{}', '{}');
        """.format(user['name'],user['gender'],user['note'],user['birth'])

        response = {}
        try:
            cursor.execute(sql)
            response['msg'] = 'Success'
        except:
            response['msg'] = 'Failed'
        db.commit()
        db.close()
        return jsonify(response)
