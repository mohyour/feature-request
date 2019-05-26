from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, IntegerField, \
                    SelectField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Required
from .models import Client, Feature


class Unique:
    """ validator that checks field uniqueness """
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = u'This Client already exists'
        self.message = message

    def __call__(self, form, field):         
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)


class FeatureForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    client = SelectField('Client', coerce=int, validators=[DataRequired()])
    client_priority = IntegerField('Priority Level')
    target_date = DateField('Target Date', format='%d-%m-%Y')
    product_areas = SelectField('Product Areas', choices=[
                                (0, "Select a priority"),
                                ('Policies', 'Policies'),
                                ('Billing', 'Billing'), ('Claims', 'Claims'),
                                ('Reports', 'Reports')], coerce=str,
                                validators=[DataRequired()])
    submit = SubmitField('Submit Feature Request')


class ClientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Unique(Client,
                                           Client.name)])
    location = StringField('Location')
    submit = SubmitField('Add Client')
