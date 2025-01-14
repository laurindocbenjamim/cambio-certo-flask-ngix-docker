
from app.upload_app.upload_view import app as bp_upload

def load_blue_prints(*,app):
    app.register_blueprint(bp_upload)