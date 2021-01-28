# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, DataRequired

## login and registration

class LoginForm(FlaskForm):
    username = StringField    ('Username', id='username_login'   , validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login'        , validators=[DataRequired()])

class CreateAccountForm(FlaskForm):
    username = StringField('Username'     , id='username_create' , validators=[DataRequired()])
    email    = StringField('Email'        , id='email_create'    , validators=[DataRequired(), Email()])
    password = PasswordField('Password' , id='pwd_create'      , validators=[DataRequired()])

## Clients
class CreateClient(FlaskForm):
    nom    = StringField('nom', id='nom_client', validators=[DataRequired()])
    prenom = StringField('prenom', id='prenom_client', validators=[DataRequired()])

## Compte-rendu
class CreateData(FlaskForm):
    id_client = SelectField('id_client', id='id_client', validators=[DataRequired()])
    compte_rendu = TextAreaField('compte-rendu', id='compte_rendu', validators=[DataRequired()])
    id_collab = StringField('id_collab', id='id_collab', validators=[DataRequired()])