from app import app
from flaskext.mysql import MySQL


#DATA BASE CONNECTION
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'cws'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)