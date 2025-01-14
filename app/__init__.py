
import os
import uuid
import secrets
from flask import Flask,Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename

from flask_wtf.csrf import CSRFProtect
#from flask import Flask, render_template, url_for

#from . upload_app.upload_view import app as bp_upload

from app.config import TestConfig, ProductionConfig


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


    # Create routes

    @app.route('/')
    def index():
        return render_template('index.html', title="Home", secret="")

    @app.route('/upload')
    def upload():
        return render_template('upload.html', title="Upload", secret="")

    @app.route('/upload/videos', methods=['POST'])
    def upload_file():
        form = UploadForm()
        if form.validate_on_submit():
            f = form.file.data
            if f:
                filename = secure_filename(f.filename)
                unique_filename = str(uuid.uuid4()) + '_' + filename 
                filepath = os.path.join(app.instance_path, 'uploads', unique_filename)
                os.makedirs(os.path.join(app.instance_path, 'uploads'), exist_ok=True)
                f.save(filepath)
                # ... (your file processing logic here) ...
                #flash('File uploaded successfully!', 'success')
                #return redirect(url_for('upload_file')) 
                return jsonify({"status":200})
        #return render_template('upload.html', form=form)
        return jsonify({"status":400})

    @app.route('/secret-key/gen')
    def gene_secret_key():

        secret = generate_secret_key()
        return f"SECRET-KEY: {secret}"
    

    # Return the application instance
    return app
