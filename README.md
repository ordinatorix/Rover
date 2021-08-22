<p align="center">
  <a href="https://github.com/seb3n/Rover">
    <img src="images/rover.png" alt="Logo">
  </a>

  <h3 align="center">Rover Tank</h3>

  <p align="center">
    This repo contains the code running on "Rover" a robotic platform powered by a raspberry pi. 
    <br>
    The hardware platform "RaspTank by adeept" can be found on Amazon.
    <br>
    <br>
    <a href="https://github.com/seb3n/Rover/issues/new">Report bug</a>
    ·
    <a href="https://github.com/seb3n/Rover/issues/new">Request feature</a>
  </p>
</p>

## Table of contents

- [What's Included](#whats-included)
- [Getting Started](#getting-started)
- [Controller Setup](#controller-setup)
- [Rover Setup](#rover-setup)
- [Bugs and Feature Requests](#bugs-and-feature-requests)
- [Contributing](#contributing)
- [Creators](#creators)
- [Thanks](#thanks)
- [Copyright and license](#copyright-and-license)


## What's Included

* OpenCV tracking.
* Forward distance measurement.
* Claw manupulation.
* Motion using tank tracks.

## Getting Started

To get started, you will need a raspberry pi with a desktop image(tested on the raspberry pi 3b) that will serve as your controller, and a second raspberry pi (CLI image) mounted on Rover (tested with pi 3b and 4).

-  Clone [this](https://github.com/seb3n/Rover.git) repo to both controller and Rover.

- If installing this on a new machine, make sure the machine has python3 at the latest verion.

- Your root folder should look like the following: ```/home/pi/Rover/```
<!-- 
- At this point, you should be able to run the RaspTankTest.py on the controller using the following command: 
```
$ python3 /home/pi/Rover/Controller/RaspTankTest.py
```
-  This should display the GUI that will allow you interface with Rover.

<!-- - When testing the install, make sure it is done on the rover, as you will get an error from not having any sensors connected. -->

- Once tested without OpenCV, you can install OpenCV. -->

## Controller Setup

Once the Repo is cloned on your device, you should be able to run 

``` 
$ python3 /home/pi/Rover/Controller/RaspTankTest.py
``` 
<br> This should display a GUI on your controller.

<br>
Now lets install OpenCV and other dependencies so that we can receive the camera stream and have access to other features on Rover.

In your controller terminal, run the following commands:
```
$ cd
$ cd Rover/Controller
$ sudo python3 controller_setup.py
```


## Rover Setup

run the install script

## Bugs and Feature Requests

Have a bug or a feature request? Please first read the [issue guidelines](https://github.com/seb3n/Rover/master/CONTRIBUTING.md) and search for existing and closed issues. If your problem or idea is not addressed yet, [please open a new issue](https://github.com/seb3n/Rover/issues/new).

## Creators

**ADEEPT**

- <https://github.com/adeept>

**SEB3N**

- <https://github.com/seb3n>

<a href='https://ko-fi.com/' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi4.png?v=0' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

## Thanks

Thanks to all contributors and their support:

## Copyright and license

Code and documentation copyright 2019 the authors. Code released under the [MIT License](https://github.com/seb3n/Rover/LICENSE).

Enjoy :metal:
