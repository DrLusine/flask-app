
from flask import Flask
from flask_cors import CORS
import pytest

@pytest.fixture
def app_instance():
    app = Flask(__name__)
    app.config['TESTING'] = True
    return app
