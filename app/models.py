from main import app
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Usuario(UserMixin, db.Model):
	usuario = db.Column(db.String(20), primary_key=True)
	password = db.Column(db.String(10))

	def __init__(self, usuario, password):
		self.usuario = usuario
		self.password = password

	#def check_password(self, password):
		#return check_password_hash(self.password, password)
db.create_all()

