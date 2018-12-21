from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, IntegerField, \
                    SelectField, TextAreaField
from wtforms.validators import DataRequired


class FeatureForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    client = SelectField('Client', coerce=int, validators=[DataRequired()])
    client_priority = SelectField('Client Priority', coerce=int,
                                  validators=[DataRequired()])
    target_date = DateField('Target Date', format='%d-%m-%Y')
    product_areas = SelectField('Product Areas', choices=[
                                (0, "Select a priority"), (1, 'Policies'),
                                (2, 'Billing'), (3, 'Claims'), (4, 'Reports')],
                                coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit Feature Request')


class ClientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    location = StringField('Location')
    submit = SubmitField('Add Client')
