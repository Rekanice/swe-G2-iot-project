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
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/", methods=['GET','POST'])
def home():
    global wm_is_idle
    global update_time
    # global gotLight

    if request.method == 'POST':
        
        global gotLight

        # Parse LDR sensor reading
        app.logger.info(request.form)
        gotLight = request.form.get('light')
        app.logger.info("gotLight = " + str(gotLight))
        print()

        # Time at which sensor reading is taken
        t = time.localtime()
        update_time = time.strftime("%H:%M", t)

        return render_template(
        'home.html', 
        update_time = update_time, 
        gotLight  = gotLight)
    
    # For GET requests, show the global gotLight variable value passed to template
    app.logger.info("gotLight=" + str(gotLight))
    print()

    return render_template(
        'home.html', 
        update_time = update_time, 
        gotLight  = gotLight)



if __name__ == '__main__':
    port = os.environ.get("PORT", 5000)              # Get port number of env at runtime, else use default port 5000
    app.run(debug=False, host='0.0.0.0', port=port)  # 0.0.0.0 port forwarding resolves the host IP address at runtime
