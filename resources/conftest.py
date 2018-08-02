
from flask import Flask
from flask_cors import CORS
from unittest.mock import patch
import pytest


@pytest.fixture
def test_client_factory():
    def create_test_client(blueprint):
        app = Flask(__name__)
        app.config['TESTING'] = True

        app.register_blueprint(blueprint)

        test_client = app.test_client()
        return test_client
    return create_test_client
