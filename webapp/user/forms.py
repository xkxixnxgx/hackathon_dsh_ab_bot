from flask_wtf import FlaskForm
from flask_login import current_user

from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from flask_wtf.file import FileField, FileAllowed

from webapp.user.models import User


class StartForm(FlaskForm):
    start_form = StringField('Start', render_kw={"class": "alert alert-secondary"})


class RegisterForm(FlaskForm):
    username = StringField('Name',
                           validators=[DataRequired(), Length(min=1, max=30)],
                           render_kw={"class": "form-control"})
    user_email = StringField('Email',
                             validators=[DataRequired(), Length(min=6, max=50), Email()],
                             render_kw={"class": "form-control"})
    user_password = PasswordField('Password', validators=[DataRequired()], render_kw={"class": "form-control"})
    confirm = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('user_password', message='Passwords do not match')],
                            render_kw={"class": "form-control"})
    submit = SubmitField('Create account',
                         render_kw={"class": "btn btn-success"})

    def validate_user_email(self, user_email):
        user_count = User.query.filter_by(user_email=user_email.data).count()
        if user_count > 0:
            raise ValidationError('A user with this email address already exists.')


class LoginForm(FlaskForm):
    # render_kw параметр в wtf, в котором можно указать то, что будет добавлено при отрисовке формы.
    # Мы добавляем класс из bootstrap из строки input class="form-control"
    user_email = StringField('Email', validators=[DataRequired()], render_kw={"class": "form-control"})
    user_password = PasswordField('Password', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Remember me', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Log in', render_kw={"class": "btn btn-success"})


class AdminForm(FlaskForm):
    content = StringField('Text', validators=[DataRequired()], render_kw={"class": "form-control"})
    picture = FileField('Update Picture', render_kw={"class": "form-control"})
    submit = SubmitField('Save', render_kw={"class": "btn btn-success"})


class RequestsForm(FlaskForm):
    id = StringField('id', validators=[DataRequired()], render_kw={"class": "form-control"})
    product = StringField('product', validators=[DataRequired()], render_kw={"class": "form-control"})
    date_add = StringField('date add', validators=[DataRequired()], render_kw={"class": "form-control"})
    status_request = StringField('status_request', validators=[DataRequired()], render_kw={"class": "form-control"})
    first_name_client = StringField('first name', validators=[DataRequired()], render_kw={"class": "form-control"})
    last_name_client = StringField('last name', validators=[DataRequired()], render_kw={"class": "form-control"})
    phone_client = StringField('phone', validators=[DataRequired()], render_kw={"class": "form-control"})
    passport_series = StringField('passport_series', validators=[DataRequired()], render_kw={"class": "form-control"})
    passport_number = StringField('passport_number', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Status', render_kw={"class": "btn btn-secondary dropdown-toggle"})
    submit_filter_all = SubmitField('Requests all', render_kw={"class": "btn btn-secondary dropdown-toggle"})
    submit_filter_done = SubmitField('Requests done', render_kw={"class": "btn btn-success dropdown-toggle"})
    submit_filter_considers = SubmitField('Requests considers', render_kw={"class": "btn btn-warning dropdown-toggle"})
    submit_filter_refused = SubmitField('Requests refused', render_kw={"class": "btn btn-danger dropdown-toggle"})


class Request_clientForm(FlaskForm):
    id = StringField('id', validators=[DataRequired()], render_kw={"class": "form-control"})
    product = StringField('Product', validators=[DataRequired()], render_kw={"class": "form-control"})
    date_add = StringField('Date create', validators=[DataRequired()], render_kw={"class": "form-control"})
    status_request = StringField('Status Request', validators=[DataRequired()], render_kw={"class": "form-control"})
    first_name_client = StringField('First Name', validators=[DataRequired()], render_kw={"class": "form-control"})
    last_name_client = StringField('Last Name', validators=[DataRequired()], render_kw={"class": "form-control"})
    phone_client = StringField('Phone', validators=[DataRequired()], render_kw={"class": "form-control"})
    passport_series = StringField('Passport Series', validators=[DataRequired()], render_kw={"class": "form-control"})
    passport_number = StringField('Passport Number', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit_update = SubmitField('Update', render_kw={"class": "btn btn-warning"})
    submit_accept = SubmitField('Accept', render_kw={"class": "btn btn-success"})
    submit_reject = SubmitField('Reject', render_kw={"class": "btn btn-danger"})
    submit_unchanged = SubmitField('Back', render_kw={"class": "btn btn-secondary"})


