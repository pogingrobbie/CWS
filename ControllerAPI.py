import string

import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request



# BALANCE INQUIRY API
@app.route('/balance/<int:id>')
def emp123(id):
    try:

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        rowcount = cursor.execute("SELECT id , balance FROM user WHERE id = %s", id)
        if rowcount > 0:
            empRows = cursor.fetchmany()
            respone = jsonify(empRows)
            respone.status_code = 200
            return respone

        else:
            message = {

                'status': 404,
                'message': 'ID not found',
            }
            respone = jsonify(message)
            respone.status_code = 404
            return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# CASH-IN API
@app.route('/cashin', methods=['POST'])
def update_emp():

    try:
        _json = request.json
        _id = _json['id']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        rowcount = cursor.execute("SELECT id , balance FROM user WHERE id = %s", _id)
        #CHECK IF ID IS NULL
        if rowcount > 0:
            empRows = cursor.fetchone()
            respone = jsonify('Easd')
            respone.status_code = 200
            _balancee = empRows['balance']

            _json = request.json
            _id = _json['id']
            _amount = _json['amount']
            #IF STATEMENT IF THE INPUT IS A LETTER
            if str(_amount).isalpha():
                message = {

                    'status': 200,
                    'message': 'The amount is invalid. Letters are not allowed!',
                }
                respone = jsonify(message)
                respone.status_code = 200
                return respone
            else:
                print("Continue")
            print(_balancee)
            #Validation if the input type has a special character.
            if str(_amount).isdigit():
                sqlQuery = "UPDATE user SET balance=%s+""" + _amount + """ WHERE id=%s"""
                bindData = (_balancee, _id,)
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                cursor.execute(sqlQuery, bindData)
                conn.commit()
                message = {

                    'status': 200,
                    'message': 'Cash-in Successful!',
                }
                respone = jsonify(message)
                respone.status_code = 200
                return respone
            else:
                message = {

                    'status': 404,
                    'message': 'The amount is invalid. Special characters are not allowed!',
                }
                respone = jsonify(message)
                respone.status_code = 404
                return respone


        else:
            message = {

                'status': 404,
                'message': 'ID not found',
            }
            respone = jsonify(message)
            respone.status_code = 404
            return respone


    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#CASH-OUT API
@app.route('/cashout', methods=['POST'])
def update_emp2():
    #SELECTING BALANCE FIRST TO COMPARE
    try:
        _json = request.json
        _id = _json['id']
        conn = mysql.connect()
        conn.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        rowcount = cursor.execute("SELECT id , balance FROM user WHERE id = %s", _id)
        #CHECK IF ID IS NULL
        if rowcount > 0:
            empRows = cursor.fetchone()
            respone = jsonify('Easd')
            respone.status_code = 200
            _balancee: int = empRows['balance']
            _json = request.json
            _id = _json['id']
            _amount = _json['amount']
            print(_balancee)
            if str(_amount).isalpha():
                message = {

                    'status': 200,
                    'message': 'The amount is invalid. Letters are not allowed!',
                }
                respone = jsonify(message)
                respone.status_code = 200
                return respone
            else:
                print("Continue")



            #COMPARE THE INPUT AND USER BALANCE AND VALIDATES IF IT HAS A SPECIAL CHARACTER
            if str(_amount).isdigit():
                if int(_amount) <= int(_balancee):

                    sqlQuery = "UPDATE user SET balance=%s-""" + _amount + """ WHERE id=%s"""
                    bindData = (_balancee, _id,)
                    conn = mysql.connect()
                    cursor = conn.cursor(pymysql.cursors.DictCursor)
                    cursor.execute(sqlQuery, bindData)
                    conn.commit()

                    message = {

                        'status': 200,
                        'message': 'Cash-out Successful!',
                    }
                    respone = jsonify(message)
                    respone.status_code = 200

                    return respone
                else:
                    message = {

                        'status': 404,
                        'message': 'Not enough balance',
                    }
                    respone = jsonify(message)
                    respone.status_code = 404
                    return respone
            else:
                message = {

                    'status': 404,
                    'message': 'The amount is invalid. Special characters are not allowed!',
                }
                respone = jsonify(message)
                respone.status_code = 404
                return respone

        else:
            message = {

                'status': 404,
                'message': 'ID not found',
            }
            respone = jsonify(message)
            respone.status_code = 404
            return respone

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone




if __name__ == "__main__":
    app.run()