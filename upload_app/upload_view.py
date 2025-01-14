import os
import uuid
import secrets
from flask import Flask,Blueprint, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename


app = Blueprint("upload_view",__name__)

class UploadForm(FlaskForm):
    file = FileField('Select File')
    submit = SubmitField('Upload')

@app.route('/', methods=['GET', 'POST'])
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
            flash('File uploaded successfully!', 'success')
            return redirect(url_for('upload_file')) 
    return render_template('upload.html', form=form)
