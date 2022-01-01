from flask import Flask
from flask import render_template, request
import time 
import os
import logging 

logging.basicConfig(level=logging.DEBUG)

# Replace these variables initial values with the previous values in database later
wm_is_idle = 0
update_time = 0 
gotLight = 0

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=['GET','POST'])
def home():
    global wm_is_idle
    global update_time
    global gotLight

    if request.method == 'POST':

        requestContent = request.headers.get('Content-Type')
        
        # Parse LDR sensor reading
        if requestContent == 'application/json':
            app.logger.info(request.json)
            json = request.get_json()
            gotLight = json["light"]
            print("light = " + str(gotLight))
            print()
        
        if requestContent == "application/x-www-form-urlencoded":
            app.logger.info(request.form)
            gotLight = request.form.get('light')
            print("light = " + str(gotLight))
            print()

        
        if gotLight:
            wm_is_idle = 1
        else:
            wm_is_idle = 0

        # Time at which sensor reading is taken
        t = time.localtime()
        update_time = time.strftime("%H:%M", t)


    return render_template(
        'home.html', 
        update_time = update_time, 
        wm_is_idle  = wm_is_idle)


if __name__ == '__main__':
    port = os.environ.get("PORT", 5000)              # Get port number of env at runtime, else use default port 5000
    app.run(debug=False, host='0.0.0.0', port=port)  # 0.0.0.0 port forwarding resolves the host IP address at runtime
    # app.run(debug=False)
