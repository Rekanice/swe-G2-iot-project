from flask import Flask
from flask import render_template, request
from time import localtime, strftime, sleep
import os
import logging 
from turbo_flask import Turbo
import threading

logging.basicConfig(level=logging.DEBUG)

# Replace these variables initial values with the previous values in database later
gotLight = 0
update_time = 0 
turbocount = 0
glcount = 0
app = Flask(__name__)
turbo = Turbo(app)

@app.route("/", methods=['GET','POST'])
def home():
    global gotLight
    global glcount

    # For POST requests, show the data
    if request.method == 'POST':
        glcount += 1
        # app.logger.info(request.form)  
        gotLight = int(request.form.get('light'))
        print()
        return render_template('home.html')
    
    # For GET requests, show the global gotLight variable value passed to template
    # app.logger.info("During GET request, gotLight=" + str(gotLight)) 
    print()
    return render_template('home.html')


@app.context_processor
def injectSensorData():
    global gotLight
    # app.logger.info("injectSensorData ran. Pass gotlight = " + str(gotLight))
    return dict(gotLight = int(gotLight))

@app.context_processor
def injectDateTime():
    # app.logger.info("injectDateTime ran")
    return dict(update_time = strftime("%Y %b %d, %a %I:%M %p", localtime()) )


# Background updater thread that runs before 1st client connects
@app.before_first_request
def before_first_request():
    threading.Thread(target=update_sensor_data).start()

def update_sensor_data():
    global turbocount
    global glcount

    with app.app_context():    
        while True:
            sleep(4)
            app.logger.info("At turbo function #" + str(turbocount) + " now. It sees gotlight " + "#" + str(glcount) +" = " + str(gotLight))
            turbocount+=1
            turbo.push(turbo.replace(render_template('wm_element.html'), 'wm_element'))

if __name__ == '__main__':
    port = os.environ.get("PORT", 5000)              # Get port number of env at runtime, else use default port 5000
    app.run(debug=False, host='0.0.0.0', port=port)  # 0.0.0.0 port forwarding resolves the host IP address at runtime
 
