from flask import Flask

app = Flask(__name__)

# including this file to ensure that circular imports do not occur
