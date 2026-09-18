from flask import Flask

from lib.properties import Properties

# Initialize Flask related properties
webapp_properties = Properties('Properties.ini').webapp()
app = Flask(__name__)

def stub_1():
    """
    This is a stub function for the webapp test cases to work initially
    """
    return 1

def stub_2():
    """
    This is a stub function to simulate missed coverage
    """
    return 2


if __name__ == '__main__':
    app.run(host=webapp_properties['host'], port=webapp_properties['port'])