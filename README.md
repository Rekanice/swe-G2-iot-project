# swe-G2-iot-project
This is the repository for Group 2's IOT project for SWE course in UTM FKE. 

### Navigate this repo
The list below stacks the most recently added folder at the top
```
master
L Flask Server - A test Flask Web app for suggesting a content (Milestone 1.3) 
L Test         - A Python script to test collaborating on Github (Milestone 1.2)
```

---


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

This is a hassle, especially if they live at higher floors OR far from (& near to) the washing machines.

Imagine having to walk back & forth between your room & the washing machine. Not once, but multiple times.

Doing laundry should be easier. Let's make the washing machines work for you, not against you.


```


### Our Solution
A full stack IOT application to automate the checking of if a washing machine is in use or idle, & relaying this info to our dashboard app for users to see.

### Use case diagram

![Use case diagram](https://github.com/Rekanice/swe-G2-iot-project/blob/55faecf1ef122f0b1f06967e5f15ea0fc0469247/UML%20diagrams/usecase_diagram1.png)
```
*Tentative features*
- booking slots for using the washing machine
```


#### Low level - System Architecture
![Overview of the tech stack]()



### Sensors
Analog sensor: RGB light sensor module

![Light Module sensor from Cytron](https://github.com/Rekanice/swe-G2-iot-project/blob/f124691cfb8c146144e130dbb8553d363e562a06/images/light_sensor_module.jpg)


Microcontroller: NodeMCU ESP8266

![NodeMCU ESP8266](https://github.com/Rekanice/swe-G2-iot-project/blob/e8a1b532913f9c267a11f2c236fd56e05f51c070/images/nodemcu_ESP8266.jpg)


