from flask import Flask

from lib.properties import Properties

# Initialize Flask related properties
webapp_properties = Properties('Properties.ini').webapp()
app = Flask(__name__)


if __name__ == '__main__':
    app.run(host=webapp_properties['host'], port=webapp_properties['port'])