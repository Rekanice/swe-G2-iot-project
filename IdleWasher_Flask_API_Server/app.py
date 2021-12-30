from flask import Flask
from flask import render_template
import time 
app = Flask(__name__)

@app.route("/")
def hello_world():
    # Time at which sensor reading is taken
    t = time.localtime()
    update_time = time.strftime("%H:%M", t)

    wm_is_idle = 0
    return render_template( 'home.html', update_time=update_time, wm_is_idle=wm_is_idle)