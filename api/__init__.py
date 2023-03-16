from flask import Flask
from api.Routes.UserHandler import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
