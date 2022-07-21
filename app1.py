# Import flask dependency
import flask as Flask

# Create a new flask app instance
app = Flask(__name__)

# Create flask route
@app.route('/')
def hello_world():
    return 'Hello world'

# Run flask app
# export FLASK_APP=app1.py
