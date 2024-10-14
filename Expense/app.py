from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Register Blueprints
from auth import auth
from expenses import expenses

migrate = Migrate(app, db)

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(expenses, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
