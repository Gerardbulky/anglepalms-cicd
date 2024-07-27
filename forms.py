from wtforms import Form, BooleanField, StringField, PasswordField, validators


class ContactForm(Form):
    name = StringField('', [validators.DataRequired()])
    email = StringField('', [validators.Email(), validators.DataRequired(), validators.Length(max=120, message="This field requires a valid email address")])
    messages = StringField('', [validators.DataRequired()])