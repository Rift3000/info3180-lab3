from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['SECRET_KEY'] = 'ThisIsAnExtraordinarilyLongPasswordNoOneWouldGuessIt'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'Removed as requested'
app.config['MAIL_PASSWORD'] = 'Removed as Requested'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

"""app.config['SECRET_KEY'] = 'enter some random passphrase'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'  # (or try 2525)
app.config['MAIL_USERNAME'] = '	2272a32e29cc7e'
app.config['MAIL_PASSWORD'] = 'b41de60c845f38' """

mail = Mail(app)
from app import views
