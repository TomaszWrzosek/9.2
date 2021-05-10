from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class Currencyform(FlaskForm):
    currency = SelectField('Waluta',validators=[DataRequired])
    calculated = StringField('calculate')


 
   