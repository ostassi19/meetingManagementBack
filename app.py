from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from customJSONEncoder import CustomJSONEncoder
from models import Meeting,db
from routes import meeting_bp

app = Flask(__name__)

# Allow all origins for development, but you should restrict it in production.
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

app.json_encoder = CustomJSONEncoder

# MySQL Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/mycalendar'

db.init_app(app)
migrate = Migrate(app, db)

try:
    db.engine.connect()
    print("Connected to the database.")
except Exception as e:
    print("Failed to connect to the database:", str(e))

app.register_blueprint(meeting_bp, url_prefix='/api/meetings')

if __name__ == '__main__':
    app.run(debug=True)