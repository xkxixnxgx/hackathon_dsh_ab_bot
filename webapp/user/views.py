from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from webapp.user.forms import LoginForm, RegisterForm, AdminForm, LoginForm, RequestsForm, Request_clientForm
from webapp.user.models import User, Requests
from webapp.user.decorators import admin_required
from datetime import datetime
from webapp.user.utils import save_picture

from webapp import db

blueprint = Blueprint('user', __name__, url_prefix='/user')



@blueprint.route('/register')
def register():
    title = 'Register'
    if current_user.is_authenticated:
        return redirect(url_for('user.login'))
    reg_form = RegisterForm()
    return render_template('user/register.html', page_title=title, form=reg_form)


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegisterForm()
    if form.validate_on_submit():
        date_now = datetime.now()
        date_reg = date_now.strftime('%d.%m.%Y')
        new_user = User(username=form.username.data, user_email=form.user_email.data, user_password=form.user_password.data, role='user',
                        date_reg=date_reg)
        new_user.set_password(form.user_password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('You have successfully registered.', 'success')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in the field {getattr(form, field).label.text}: {error}", 'warning')
        return redirect(url_for('user.register'))


@blueprint.route('/login')
def login():
    title = 'Log in'
    if current_user.is_authenticated:
        return redirect(url_for('tracks.login'))
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.user_email == form.user_email.data).first()
        if user and user.check_password(form.user_password.data):
            login_user(user, remember=form.remember_me.data)
            flash('You have successfully logged in', 'success')
            return redirect(url_for('user.requests'))
        else:
            flash('Login unsuccessful. Please check email and password', 'warning')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out', 'success')
    return redirect(url_for("user.login"))


@blueprint.route('/admin')
@admin_required
def admin_index():
    if current_user.is_admin:
        title = 'Admin console'
        admin_form = AdminForm()
        return render_template('user/admin.html', page_tittle=title, form=admin_form)
    else:
        return redirect(url_for("user.console"))


@blueprint.route('/process_save', methods=['POST'])
def process_save():
    form = AdminForm()
    if form.validate_on_submit():
        new_content = Requests(content=form.content.data, picture=form.picture.data)
        db.session.add(new_content)
        db.session.commit()
        flash('You have new content.', 'success')
    return redirect(url_for('user.requests'))


@blueprint.route('/requests', methods=['GET'])
def requests():
    if current_user.is_authenticated:
        title = 'Requests'
        form = RequestsForm()
        request_list = Requests.query.all()
        return render_template('user/requests.html', page_title=title, request_list=request_list, form=form)
    else:
        flash('You are not authenticated. Please login.', 'warning')
        return redirect(url_for('user.login'))


@blueprint.route('/requests/considers', methods=['GET'])
def requests_considers():
    if current_user.is_authenticated:
        title = 'Requests considers'
        form = RequestsForm()
        status_request = 'considers'
        request_list = Requests.query.filter(Requests.status_request == status_request)
        return render_template('user/requests_considers.html',
                               page_title=title,
                               request_list=request_list,
                               form=form
                               )
    else:
        flash('You are not authenticated. Please login.', 'warning')
        return redirect(url_for('user.login'))


@blueprint.route('/requests/done', methods=['GET'])
def requests_done():
    if current_user.is_authenticated:
        title = 'Requests done'
        form = RequestsForm()
        status_request = 'done'
        request_list = Requests.query.filter(Requests.status_request == status_request)
        return render_template('user/requests_done.html',
                               page_title=title,
                               request_list=request_list,
                               form=form
                               )
    else:
        flash('You are not authenticated. Please login.', 'warning')
        return redirect(url_for('user.login'))


@blueprint.route('/requests/refused', methods=['GET'])
def requests_refused():
    if current_user.is_authenticated:
        title = 'Requests refused'
        form = RequestsForm()
        status_request = 'refused'
        request_list = Requests.query.filter(Requests.status_request == status_request)
        return render_template('user/requests_refused.html',
                               page_title=title,
                               request_list=request_list,
                               form=form
                               )
    else:
        flash('You are not authenticated. Please login.', 'warning')
        return redirect(url_for('user.login'))


@blueprint.route('/request_client/')
@blueprint.route('/request_client/<id_client>', methods=['POST', 'GET'])
def request_client(id_client):
    title = 'Client id: ' + str(id_client)
    form = Request_clientForm()
#   print(request.args.get('status_request'))
    if request.method == 'GET':
        return render_template('user/request_client.html', page_title=title, id_client=id_client, form=form)
    else:
        print(request.args.get('status_request'))
        if request.args.get('status_request'):
            marker_change_request = request.args.get('status_request')

            if marker_change_request == 'unchanged':
                flash('You left the request without modifications.', 'secondary')
                return redirect(url_for('user.requests'))

            if marker_change_request == 'update':
                if form.validate_on_submit():
                    request_update = Requests.query.filter(
                        Requests.status_request == request.args.get('status_request'))
                    # request_update = Requests.query.filter(Requests.id == id_client).first()
                    if request_update:
                        request_update = Requests(
                            id=id_client,
                            product=form.product.data,
                            date_add=form.date_add.data,
                            status_request=form.status_request.data,
                            first_name_client=form.first_name_client.data,
                            last_name_client=form.last_name_client.data,
                            phone_client=form.phone_client.data,
                            passport_series=form.passport_series.data,
                            passport_number=form.passport_number.data
                        )
                        db.session.add(request_update)
                        db.session.commit()
                        flash(f'You have successfully data update for user with id: {id_client}.', 'success')
                        return render_template('user/request_client.html', page_title=title, id_client=id_client,
                                               form=form)
                else:
                    flash('Update unsuccessful. Please check data.', 'warning')
                return redirect(url_for('user.requests'))

            if marker_change_request == 'done':
                new_status_request = 'done'
                request_update = Requests.query.filter(Requests.id == id_client).first()
                if request_update:
                    request_update = Requests(
                        status_request=new_status_request,
                    )
                    db.session.add(request_update)
                    db.session.commit()
                    flash(f'You have successfully change the request to DONE for user with id: {id_client}.', 'success')
                    return redirect(url_for('user.requests'))
                else:
                    flash('Update unsuccessful. Please check data.', 'warning')
                return redirect(url_for('user.requests'))

            if marker_change_request == 'refused':
                new_status_request = 'refused'
                request_update = Requests.query.filter(Requests.id == id_client).first()
                if request_update:
                    request_update = Requests(
                        status_request=new_status_request,
                    )
                    db.session.add(request_update)
                    db.session.commit()
                    flash(
                        f'You have successfully change the request to {(new_status_request).upper()} for user with id: {id_client}.',
                        'success')
                    return redirect(url_for('user.requests'))
                else:
                    flash('Update unsuccessful. Please check data.', 'warning')
                    return redirect(url_for('user.requests'))



# request_list = Request_clientForm.query.filter(Request_clientForm.status_request == request.arga.get('status_request'))





