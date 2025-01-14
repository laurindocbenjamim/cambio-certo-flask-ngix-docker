from app.dependencies import os
from app import create_app


# Get the application instance
app = create_app(JDBC='sqlite',test_app=True)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'], debug=app.config['DEBUG'])