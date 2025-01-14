
"""

"""

from app.dependencies import Flask
from app.dependencies import CSRFProtect

from app.config import TestConfig, ProductionConfig

from app.blue_prints import load_blue_prints
from app.routes import load_routes


def create_app(*,JDBC, test_app):

    app = Flask(__name__)
    app.secret_key = '&g!8a@B)=zmWUbZ%VpxFsG6Rn_GAMFNd'  # Replace with a strong, unique secret key
    csrf = CSRFProtect(app)
    #CORS(app)  # Allow cross-origin requests for frontend-backend communication.
    
    if test_app:
        app.config.from_object(TestConfig(JDBC))
    else: app.config.from_object(ProductionConfig(JDBC))

    # Create and load the blueprints application
    load_blue_prints(app=app)

    # Load and Create routes
    load_routes(app=app)


    # Return the application instance
    return app
