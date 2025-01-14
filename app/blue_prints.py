
from app.upload_app.upload_view import app as bp_upload

#
def load_blue_prints(*,app):
    """ This method load all the blueprints 
    Args:

    Returns:
    
    """
    app.register_blueprint(bp_upload)