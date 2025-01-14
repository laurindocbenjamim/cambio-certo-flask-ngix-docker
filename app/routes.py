
from app.dependencies import render_template
from app.dependencies import flash
from app.dependencies import secrets


def generate_secret_key(length=32):
  """Generates a cryptographically secure random secret key.

  Args:
    length: The desired length of the key (default: 32 characters).

  Returns:
    A string containing the randomly generated secret key.
  """
  alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+'
  return ''.join(secrets.choice(alphabet) for _ in range(length))

# Method to load routes
def load_routes(*,app):
    """ This method load all the routes 
    Args:

    Returns:
    
    """
    @app.route('/')
    def index():
        return render_template('video_player.html', title="Home", secret="")

    @app.route('/secret-key/gen')
    def gene_secret_key():

        secret = generate_secret_key()
        return f"SECRET-KEY: {secret}"