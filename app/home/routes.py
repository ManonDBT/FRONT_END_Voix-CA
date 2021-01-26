# -*- encoding: utf-8 -*-
import json

import requests
from app.home import blueprint
from app.base.forms import CreateClient
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound

apiURL = 'http://149.91.88.54:1234//'

@blueprint.route('/index')
@login_required
def index():

    return render_template('index.html', segment='index')

@blueprint.route('/clients.html', methods=['GET', 'POST'])
def clients():
    _clients = requests.get(apiURL+'clients').json()
    _createForm = CreateClient(request.form)
    if 'add' in request.form:
        #read data from create form
        prenom = request.form['prenom']
        nom = request.form['nom']
        _toSend = {'prenom': prenom,'nom':nom}
        _toSend = json.dumps(_toSend)
        #request to api
        retour = requests.post(apiURL+'client', json=_toSend).status_code

        if retour == 201:
            return render_template('clients.html', segment='clients', clients=_clients)
        else:
            return render_template('clients.html', segment='clients', clients=_clients, msg='Erreur d\'ajout du client')

    if 'modify' in request.form:
        return True;

    if 'delete' in request.form:
        return True;

    return render_template('clients.html', segment='clients', clients=_clients, createForm=_createForm)


@blueprint.route('/mescomptesrendu.html', methods=['GET', 'POST'])
def data():
    _data = requests.get(apiURL+'data').json()
    return render_template('mescomptesrendu.html', segment='mescomptesrendu', datas=_data)


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith( '.html' ):
            template += '.html'

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( template, segment=segment )

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500

# Helper - Extract current page name from request 
def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  
