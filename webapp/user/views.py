from flask import Blueprint, render_template, flash, redirect, url_for, request
from webapp.user.forms import RequestsForm, Request_clientForm

from webapp.db import posts
from bson.objectid import ObjectId
import crypt

blueprint = Blueprint('user', __name__, url_prefix='/user')


@blueprint.route('/requests', methods=['GET'])
def requests():
    title = 'Requests'
    form = RequestsForm()
    username_for_tm = crypt.decrypt_dict(posts.find_one('username'))
    request_list = crypt.decrypt_dict(posts.find())
    return render_template('user/requests.html',
                           page_title=title,
                           request_list=request_list,
                           form=form,
                           username_for_tm=username_for_tm
                           )


@blueprint.route('/requests/considers', methods=['GET'])
def requests_considers():
    title = 'Requests considers'
    form = RequestsForm()
    status_request = 'В обработке'
    request_list = crypt.decrypt_dict(posts.find({'status': status_request}))
    username_for_tm = crypt.decrypt_dict(posts.find_one('username'))
    return render_template('user/requests_considers.html',
                           page_title=title,
                           request_list=request_list,
                           form=form,
                           username_for_tm=username_for_tm
                           )


@blueprint.route('/requests/done', methods=['GET'])
def requests_done():
    title = 'Requests done'
    form = RequestsForm()
    status_request = 'Одобрено'
    request_list = crypt.decrypt_dict(posts.find({'status': status_request}))
    username_for_tm = crypt.decrypt_dict(posts.find_one('username'))
    return render_template('user/requests_done.html',
                           page_title=title,
                           request_list=request_list,
                           form=form,
                           username_for_tm=username_for_tm
                           )


@blueprint.route('/requests/refused', methods=['GET'])
def requests_refused():
    title = 'Requests refused'
    form = RequestsForm()
    status_request = 'Отказано'
    request_list = crypt.decrypt_dict(posts.find({'status': status_request}))
    username_for_tm = crypt.decrypt_dict(posts.find_one('username'))
    return render_template('user/requests_refused.html',
                           page_title=title,
                           request_list=request_list,
                           form=form,
                           username_for_tm=username_for_tm
                           )


@blueprint.route('/request_client/')
@blueprint.route('/request_client/<id_client>', methods=['GET', 'POST'])
def request_client(id_client):
    title = 'Client id: ' + str(id_client)
    form = Request_clientForm()
    request_list = crypt.decrypt_dict(posts.find_one({'_id': ObjectId(id_client)}))
    # data_list =
    if request.args.get('status_request'):
        marker_change_request = request.args.get('status_request')

        if marker_change_request == 'unchanged':
            flash('You left the request without modifications.', 'secondary')
            return redirect(url_for('user.requests'))

        if marker_change_request == 'update':
            # status_request_done = 'Одобрено'
            # request_list['status'] = status_request_done
            # posts.find_one_and_replace({"_id": ObjectId(id_client)}, request_list)
            if form.validate_on_submit():
                request_update = posts.find(
                    product=form.product.data,
                    date_add=form.date_add.data,
                    status_request=form.status_request.data,
                    first_name_client=form.first_name_client.data,
                    last_name_client=form.last_name_client.data,
                    passport_series=form.passport_series.data,
                    passport_number=form.passport_number.data,
                    phone_client=form.phone_client.data
                )
                flash(f'You have successfully data update for user with id: {id_client}.', 'success')
                return render_template('user/request_client.html', page_title=title, id_client=id_client,
                                       form=form)
            else:
                flash('Update unsuccessful. Please check data.', 'warning')
            return render_template('user/request_client.html',
                                   page_title=title,
                                   id_client=id_client,
                                   form=form,
                                   request_list=request_list
                                   )

        if marker_change_request == 'done':
            status_request_done = 'Одобрено'
            request_list['status'] = status_request_done
            crypt.encrypt_dict(posts.find_one_and_replace({"_id": ObjectId(id_client)}, request_list))
            flash(f'You have successfully change the request to DONE for user with id: {id_client}.', 'success')
            return redirect(url_for('user.requests'))

        if marker_change_request == 'refused':
            status_request_done = 'Отказано'
            request_list['status'] = status_request_done
            crypt.encrypt_dict(posts.find_one_and_replace({"_id": ObjectId(id_client)}, request_list))
            flash(f'You have successfully change the request to REFUSED for user with id: {id_client}.', 'success')
            return redirect(url_for('user.requests'))

    return render_template('user/request_client.html',
                       page_title=title,
                       id_client=id_client,
                       form=form,
                       request_list=request_list
                       )







