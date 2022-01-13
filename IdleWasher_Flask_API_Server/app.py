from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask.json import loads
from time import localtime, strftime, sleep
from datetime import datetime
from pytz import timezone
import os
import logging 
from turbo_flask import Turbo
import threading
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# -----------------------------------------------------------------------------------------------------------------------------------------------

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
turbo = Turbo(app)

# CHANGE to 'dev' when devloping locally, 'prod' when deploying
ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mypwd@localhost/idle_washer'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -----------------------------------------------------------------------------------------------------------------------------------------------

# Model = a blueprint for a single resource = to create a row in the table
# Each table in the database needs a class (model) to be created for it
class Washing_Machine(db.Model):

    # Create a table with these columns
    __tablename__ = 'washing_machine'
    id = db.Column(db.Integer, primary_key=True)            # Washing machine global ID
    college = db.Column(db.String, nullable=False)
    block = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)    
    room_index = db.Column(db.Integer, nullable=False)      # Position in the room, starting from leftmost side & increase in clockwise direction
    money_input = db.Column(db.Boolean, nullable=False)     # True=paper notes, False=coins
    is_working = db.Column(db.Boolean, nullable=False)      # True=working, False=rosak
    
    # Create an object with the table columns as its properties
    def __init__(self, id, location, room_index, money_input, is_working):
        self.id = id
        self.college = college
        self.block = block
        self.location = location
        self.room_index = room_index
        self.money_input = money_input
        self.is_working = is_working

    # This is not necessary. This prints the following statement when we print an instance of this class
    def __repr__(self):
        return f"This table has {self.id} washing machines in total."


class Sensor_Log(db.Model):

    # Create a table with these columns
    __tablename__ = 'sensor_log'
    timestamp = db.Column(db.DateTime, primary_key=True)                # DateTime format: 
    wm_id = db.Column(db.Integer, db.ForeignKey('washing_machine.id'))  # Washing machine global ID
    in_use = db.Column(db.Boolean, nullable=False)                      # True=in use, False=idle

    # Create an object with the table columns as its properties
    def __init__(self, timestamp, wm_id, in_use):
        self.timestamp = timestamp
        self.wm_id = wm_id
        self.in_use = in_use

    # This is not necessary. This prints the following statement when we print an instance of this class
    def __repr__(self):
        return f"The latest log: WM #{self.wm_id} is in_use={self.in_use} , at datetime={self.timestamp}."


# Track changes in table schemas (column names, typing & edits)
# Add = flask db migrate -m "comments", Commit = flask db upgrade
Migrate(app, db)

# -----------------------------------------------------------------------------------------------------------------------------------------------

# Home page (Dashboard)
@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')


# Update the Sensor Data variable every time before the home page is rendered
@app.context_processor
def injectSensorData():
    fetch_wm_id = 1
    fetched_latest_data = Sensor_Log.query.filter_by(wm_id=fetch_wm_id).order_by(Sensor_Log.timestamp.desc()).first()    #Just read as class object, insted of JSON object
    
    # the keys in this dict are the template variables
    return dict(
        wm_id = fetch_wm_id,
        gotLight = int(fetched_latest_data.in_use), 
        update_time = fetched_latest_data.timestamp.strftime("%Y %b %d, %a %I:%M %p")
    )

# Background updater thread that runs before a client connects for the 1st time
@app.before_first_request
def before_first_request():
    threading.Thread(target=update_sensor_data).start()

def update_sensor_data():
    with app.app_context():    
        while True:
            sleep(3)
            turbo.push(turbo.replace(render_template('wm_element.html'), 'wm_element'))


# -----------------------------------------------------------------------------------------------------------------------------------------------

# API: capture & store the latest sensor data into the sensor log in database
@app.route("/log_sensor_data", methods=['GET','POST'])
def log_sensor_data():
    if request.method == 'POST':
        new_log = Sensor_Log(
            datetime.now(tz=timezone('Asia/Kuala_Lumpur')),
            int(request.form.get('wm_id')),
            int(request.form.get('light'))
        )
        db.session.add(new_log)
        db.session.commit()
        return "New data is logged!", 200
    
    return "No data is logged yet. You should be POST-ing to this url, not GET-ing"


# API: read the latest sensor data
@app.route("/read_sensor_data/<int:wm_id>", methods=['GET'])
def read_sensor_data(wm_id):
    latest_data = Sensor_Log.query.filter_by(wm_id=wm_id).order_by(Sensor_Log.timestamp.desc()).first()
    print(latest_data)
    return dict(
        timestamp = latest_data.timestamp,
        wm_id     = latest_data.wm_id,
        in_use    = latest_data.in_use
    )

# API: select washing machine college, block, location

# API: extract sensor data history for given wm_id


# -----------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    port = os.environ.get("PORT", 5000)              # Get port number of env at runtime, else use default port 5000
    app.run(debug=False, host='0.0.0.0', port=port)  # 0.0.0.0 port forwarding resolves the host IP address at runtime
 
