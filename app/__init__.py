
"""import os
import uuid
import secrets
from flask import Flask,Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename

from flask_wtf.csrf import CSRFProtect"""
from app.dependencies import os
from app.dependencies import uuid
from app.dependencies import secrets
from app.dependencies import Flask
from app.dependencies import render_template
from app.dependencies import request
from app.dependencies import redirect
from app.dependencies import url_for
from app.dependencies import flash
from app.dependencies import jsonify
from app.dependencies import secure_filename
from app.dependencies import CSRFProtect
from app.dependencies import FileField
from app.dependencies import SubmitField
from app.dependencies import FlaskForm

#from flask import Flask, render_template, url_for

#from . upload_app.upload_view import app as bp_upload

from app.config import TestConfig, ProductionConfig

from app.blue_prints import load_blue_prints


def generate_secret_key(length=32):
  """Generates a cryptographically secure random secret key.

  Args:
    length: The desired length of the key (default: 32 characters).

  Returns:
    A string containing the randomly generated secret key.
  """
  alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+'
  return ''.join(secrets.choice(alphabet) for _ in range(length))


class UploadForm(FlaskForm):
    file = FileField('Select File')
    submit = SubmitField('Upload')

def create_app(*,JDBC, test_app):

    app = Flask(__name__)
    app.secret_key = '&g!8a@B)=zmWUbZ%VpxFsG6Rn_GAMFNd'  # Replace with a strong, unique secret key
    csrf = CSRFProtect(app)

    if test_app:
        app.config.from_object(TestConfig(JDBC))
    else: app.config.from_object(ProductionConfig(JDBC))


    load_blue_prints(app=app)
    # Create routes

    @app.route('/')
    def index():
        return render_template('index.html', title="Home", secret="")

    @app.route('/secret-key/gen')
    def gene_secret_key():

        secret = generate_secret_key()
        return f"SECRET-KEY: {secret}"
    

    # Return the application instance
    return app
