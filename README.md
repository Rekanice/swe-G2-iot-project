# swe-G2-iot-project
This is the repository for Group 2's IOT project for SWE course in UTM FKE. 

### Navigate this repo
The list below stacks the most recently created folder at the top
```
master
L images       - A folder for storing the pics used in README.md files. 
L UML diagrams - A folder for the UML models for the main project (Milestone 2.1)
L Flask Server - A test Flask Web app for suggesting a content (Milestone 1.3) 
L Test         - A Python script to test collaborating on Github (Milestone 1.2)
```

---

<br/>

## Main Project: Idle Washer 🧺

### Problem Statement

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

### Our Solution
A full stack IOT application to automate the checking if a washing machine is busy or idle, and relay this info to a dashboard app for users to see & plan their laundry trip to the washing machine accordingly.

<br/>

### Use case diagram

![Use case diagram](https://github.com/Rekanice/swe-G2-iot-project/blob/55faecf1ef122f0b1f06967e5f15ea0fc0469247/UML%20diagrams/usecase_diagram1.png)

**Tentative features**
- booking slots for using the washing machine

<br/>

### System Architecture
![Overview of the tech stack]()

<br/>

### Hardware
```
- Sensor : RGB light sensor module
- MCU    : NodeMCUv1 ESP8266 
```
![Light Module sensor from Cytron](https://github.com/Rekanice/swe-G2-iot-project/blob/f124691cfb8c146144e130dbb8553d363e562a06/images/light_sensor_module.jpg)
![NodeMCU ESP8266](https://github.com/Rekanice/swe-G2-iot-project/blob/e8a1b532913f9c267a11f2c236fd56e05f51c070/images/nodemcu_ESP8266.jpg)

<br/>

#### Hardware Setup
![Device setup](https://github.com/Rekanice/swe-G2-iot-project/blob/d76a08e94ea6444962755b7ac9bf270c3a8d7b9a/images/device_setup.jpg)

<br/>

### Communication Protocol
```
HTTP / MQTT / ESP NOW
```
*Will test out & choose the one that suits our use case after testing.*

<br/>

### Cloud Platform & Web server
```
Backend framework      : Flask
Cloud hosting platform : Heroku
```
Check out our Flask toy app [here](https://tell-me-something-flask-app.herokuapp.com/joke).

<br/>

### Dashboard Frontend
```
Web    : Basic HTML-CSS-JS or Flutter
Mobile : MIT Inventor or Flutter
```
*Will test out & choose the one that can be executed well.*

<br/>

**UI Wireframe - Version 1**

![Figma Design of the UI]()





