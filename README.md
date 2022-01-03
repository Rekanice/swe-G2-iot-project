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
    2. [Milestone 4:]()
    3. [Milestone 5:]()
    4. [Milestone 6:]()
    5. [Milestone 7:]()




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
*Will test out & choose the one that suits our use case after testing.*

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
Web    : Basic HTML-CSS-JS or Flutter
Mobile : MIT Inventor or Flutter
```
*Will test out & choose the one that can be executed well.*

Here is a [video](https://www.youtube.com/watch?v=bYe--Yvlxbc) of the mobile app prototype made in MIT App Inventor.

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
[Demo video](https://youtu.be/WuiT0wlSRcE)

![Sensor setup](https://github.com/Rekanice/swe-G2-iot-project/blob/bbef47352ffa9df50c8eafda36a5559154607df4/images/ldr.jpg)

![Flask web server UI](https://github.com/Rekanice/swe-G2-iot-project/blob/bbef47352ffa9df50c8eafda36a5559154607df4/images/flaskwebhtml.png)

<br/>


