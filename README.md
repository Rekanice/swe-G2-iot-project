# swe-G2-iot-project
This is the repository for Group 2's IOT project for SWE course in UTM FKE. 

### Navigate this repo
The list below stacks the most recently created folder at the top
```
master
L IdleWasher_Flask_API_Server     - A folder for the code used in making the Flask web server for the project (Milestone 3)
L IdleWasher_ESP8266_LightSensor  - A folder for code used in the ESP8266 reading & sending data to server (Milestone 3)
L images        - A folder for storing the pics used in README.md files. 
L UML diagrams  - A folder for the UML models for the main project (Milestone 2.1)
L Test Flask Server - A test Flask Web app for suggesting a content (Milestone 1.3) 
L Test              - A Python script to test collaborating on Github (Milestone 1.2)
```


### Table of contents
1. [Main Project Details](#project)
    1. [Problem Statement](#prob)
    2. [Proposed solution](#sol)
    3. [Use Case diagram](#uc)
    4. [System architecture](#sysarc)
    5. [Hardware](#hw)
    6. [Communication Protocol](#comm)
    7. [Server & Hosting](#cloud)
    8. [Frontend](#ui)

2. [Updates](#updates)
    1. [Milestone 3: Send realtime sensor data to cloud server](#mi3)
    2. [Milestone 4: Send sensor data to database, Flask server reads data from database](#mi4)
    3. [Milestone 5: Dashboard UI improvements](#mi5)

3. [Demo Videos Rewind](#rewind)




<br/>

# Main Project: Idle Washer 🧺 <a name="project"></a>

### Problem Statement <a name="prob"></a>

>**tldr**: *Inconvenient for dorm residents to physically check if shared washing machine is available to use.*
```
Students living in UTM dorms use a shared set of washing machines to do their laundry. 

Often, the washing machines are located at the ground floor.

The students have only one way of knowing if a washing machine
- is idle & available to use, OR
- was busy & has finished running.

They have to go to the washing machine & manually see it for themselves. 

This is a hassle, especially if they live at higher floors OR far from (and even near to) the washing machines.

Imagine having to walk back & forth between your room & the washing machine. Not once, but multiple times.

Doing laundry should be easy. Let's make the washing machines work FOR you, not against you.
```

<br/>

### Our Solution <a name="sol"></a>
A full stack IOT application to automate the checking if a washing machine is busy or idle, and relay this info to a dashboard app for users to see & plan their laundry trip to the washing machine accordingly.

<br/>

### Use case diagram <a name="uc"></a>

![Use case diagram](https://github.com/Rekanice/swe-G2-iot-project/blob/55faecf1ef122f0b1f06967e5f15ea0fc0469247/UML%20diagrams/usecase_diagram1.png)

**Tentative features**
- booking slots for using the washing machine

<br/>

### System Architecture <a name="sysarc"></a>
![Overview of the tech stack](https://github.com/Rekanice/swe-G2-iot-project/blob/e0d91b83c3a7868e55449eced2450638003cc4a4/images/system_arch_pic.png)

<br/>

### Hardware <a name="hw"></a>
```
- Sensor : RGB light sensor module
- MCU    : NodeMCUv1 ESP8266 
```
![Light Module sensor from Cytron](https://github.com/Rekanice/swe-G2-iot-project/blob/f124691cfb8c146144e130dbb8553d363e562a06/images/light_sensor_module.jpg)
![NodeMCU ESP8266](https://github.com/Rekanice/swe-G2-iot-project/blob/e8a1b532913f9c267a11f2c236fd56e05f51c070/images/nodemcu_ESP8266.jpg)

<br/>

#### Hardware Setup <a name="hwsetup"></a>
![Device setup](https://github.com/Rekanice/swe-G2-iot-project/blob/d76a08e94ea6444962755b7ac9bf270c3a8d7b9a/images/device_setup.jpg)

<br/>

### Communication Protocol <a name="comm"></a>
```
HTTP
```

<br/>


### Cloud Platform & Web server <a name="cloud"></a>
```
Backend framework      : Flask
Cloud hosting platform : Heroku
```
Check out our Flask toy app [here](https://tell-me-something-flask-app.herokuapp.com/)

Check out our Django toy app [here](https://this-is-django-1.herokuapp.com/)

Here is a [video](https://youtu.be/oEzaFD8RCEE) of deploying the Flask/Deploy app in Heroku.

This is the accompanying article on [Deploying the Flask / Django app in Heroku](https://github.com/Rekanice/swe-G2-iot-project/blob/f4e41c6ab807bea9e7c15f0c16e89c8eff10dd4d/Deploying-on-Heroku.md).

<br/>

### Dashboard Frontend <a name="ui"></a>
```
Web    : Basic HTML-CSS-JS
Mobile : MIT Inventor
```

Here is a [demo video](https://www.youtube.com/watch?v=bYe--Yvlxbc) of the mobile app prototype made in MIT App Inventor.

<br/>

**UI Wireframe - Version 1**

[Figma Design of the UI](https://www.figma.com/file/upOI1YDz3MclTJADYTzi7z/Figma-UI?node-id=0%3A1)


![page1](https://github.com/Rekanice/swe-G2-iot-project/blob/c0d8e5974da57e7b26fbca8b5b33419303bdb059/images/figma_v1_page1.png)
![page2](https://github.com/Rekanice/swe-G2-iot-project/blob/c0d8e5974da57e7b26fbca8b5b33419303bdb059/images/figma_v1_page2.png)
![page3](https://github.com/Rekanice/swe-G2-iot-project/blob/c0d8e5974da57e7b26fbca8b5b33419303bdb059/images/figma_v1_page3.png)
![page4](https://github.com/Rekanice/swe-G2-iot-project/blob/c0d8e5974da57e7b26fbca8b5b33419303bdb059/images/figma_v1_page4.png)
![page5](https://github.com/Rekanice/swe-G2-iot-project/blob/c0d8e5974da57e7b26fbca8b5b33419303bdb059/images/figma_v1_page5.png)

<br/>

# Updates <a name="updates"></a>

### Milestone 3: Send sensor data directly to Flask server <a name="mi3"></a>

The ESP8266 sends the light sensor data to the Flask web server hosted on Heroku via HTTP POST requests. The Flask web app dynamically updates the status of the washing machine display box, with a ~5s delay (this is negligible in real use case) without the user needing to refresh the page.

[Heroku web app](https://idle-washer.herokuapp.com/)

[Demo video for milestone 3](https://youtu.be/WuiT0wlSRcE)

![Sensor setup](https://github.com/Rekanice/swe-G2-iot-project/blob/bbef47352ffa9df50c8eafda36a5559154607df4/images/ldr.jpg)

![Flask web server UI](https://github.com/Rekanice/swe-G2-iot-project/blob/bbef47352ffa9df50c8eafda36a5559154607df4/images/flaskwebhtml.png)

<br/>

### Milestone 4: Send sensor data to database, Flask server reads data from database <a name="mi4"></a>

The ESP8266 sends the light sensor data to the Flask web server hosted on Heroku via HTTP POST requests. The Flask server has a dedicated url to accept & parse the POST request & store the data into the connected PostgreSQL database. The Flask web app dynamically updates the UI by querying necessary data from the database, and processing them in the application to be delivered in the UI templates.

[Demo video for Milestone 4](https://youtu.be/-4hxKUfy3Ok)

Database tables design: 
1. Washing_Machine : contains all the attributes about the washing machines.
![Washing Machine table](https://github.com/Rekanice/swe-G2-iot-project/blob/b5c75e600e6379d77504918cd4bc5cbfa9e4ab16/images/db_table_washing_machines.jpg)

2. Sensor_Log: records the detected light data from a given washing machine (identified by its wm_id), every 5 minutes. The two tables are linked by the wm_id column.


![Sensor log table](https://github.com/Rekanice/swe-G2-iot-project/blob/b5c75e600e6379d77504918cd4bc5cbfa9e4ab16/images/db_table_sensor_log.jpg)

![Flask web server UI](https://github.com/Rekanice/swe-G2-iot-project/blob/b5c75e600e6379d77504918cd4bc5cbfa9e4ab16/images/flask_webpage_with_static_heatmap.jpg)

<br/>

### Milestone 5: Dashboard UI improvements <a name="mi5"></a>

From the feedback on the dashboard in milestone 4, these changes were made:
- more washing machine indicators
- a more recent timeline plot (hence, we went with the last hour readings in 5 minute intervals)
- a more dashboard box-style layout

All the data required by the dashboard to display are served via APIs in the Flask app.py. The necessary data are queried from the PostgreSQL database and processed before passing to the frontend.


The repository for cloning and reproducing our milestone 5 Flask app is transferred to a new repository ([link here](https://github.com/Rekanice/Check-WM-Dashboard)).


[Youtube Demo for Milestone 5](https://youtu.be/qwATc6cMqR8)

![How the new dashboard looks like](https://github.com/Rekanice/swe-G2-iot-project/blob/fe0e162c5e2c1b701822b52d4fc0dace6c6adb8d/new_dashboard.png)


<br/>

# Milestones Demo Videos Rewind <a name="rewind"></a>


1. Milestone 1 [Part 1](https://youtu.be/BIsVwdGV0DI) [Part 2](https://youtu.be/cB8r0cHiGOs) [Part 3](https://youtu.be/qsbzFyFUOwY)
2. Milestone 2 [Heroku Deployment](https://youtu.be/oEzaFD8RCEE) [UI Prototype](https://www.youtube.com/watch?v=bYe--Yvlxbc)
3. [Milestone 3 video](https://youtu.be/WuiT0wlSRcE)
4. [Milestone 4 video](https://youtu.be/-4hxKUfy3Ok)
5. [Milestone 5 video](https://youtu.be/qwATc6cMqR8)

