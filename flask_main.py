import request

from flask import Flask
from mysql_ops import post_data_to_mysql, get_data_from_mysql

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome! Please use /data/post or /data/get to post or get data from MySQL."

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'GET':
        return get_data()
    else:
        return post_data()


@app.route('/data/post'):
def post_data():
    content = request.form['data']

    return post_data_to_mysql(content)

@app.route('/data/get'):
def get_data():
    return get_data_from_mysql()

