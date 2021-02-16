from app.forms import LoginForm
from flask import render_template, flash, redirect
from app.models import Usuario
from flask_login import login_user, login_required, logout_user, current_user
from . import auth
#from app.mysql_service import buscar_dicc


@auth.route('/login', methods=['GET', 'POST'])
def login():
	login_form = LoginForm() 
	
	context = {
		'login_form' : login_form
	}	
	if login_form.validate_on_submit():

		usuario = login_form.usuario.data
		password = login_form.password.data	
		user = Usuario.query.filter_by(usuario=usuario).first()
			
		if user is not None:
			password_db = user.password
			
			if password == password_db:
				login_user(user)
				flash('Ha ingresado éxitosamente a su sesión')
				
			else:
				flash('Revise de nuevo sus datos e intente de nuevo')
		else:
			flash('No existe su usuario')

	return render_template('login.html', **context)

#@app.route('/logout')
#@login_required
#def logout():
#	logout_user()
#	flash('Regresa pronto')
#	return redirect(url_for('login'))





