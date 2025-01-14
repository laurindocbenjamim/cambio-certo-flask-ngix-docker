from app.dependencies import os
from app.dependencies import uuid

from app.dependencies import Blueprint
from app.dependencies import render_template
from app.dependencies import make_response
from app.dependencies import request
from app.dependencies import redirect
from app.dependencies import url_for

from app.dependencies import jsonify
from app.dependencies import secure_filename

from app.dependencies import FileField
from app.dependencies import SubmitField
from app.dependencies import FlaskForm

app = Blueprint("upload_view",__name__,url_prefix='/upload')

class UploadForm(FlaskForm):
    file = FileField('Select File')
    submit = SubmitField('Upload')

@app.route('/')
def upload():
    response = make_response(render_template('upload_video.html', title="Upload", secret=""))
    return response

@app.route('/videos', methods=['POST'])
def upload_videos():
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
