<p align="center">
  <a href="https://rover.io/">
    <img src="rover_logo1.png" alt="Logo" width=272 height=102>
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

- [Quick start](#quick-start)
- [What's included](#whats-included)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Contributing](#contributing)
- [Creators](#creators)
- [Thanks](#thanks)
- [Copyright and license](#copyright-and-license)

## Quick start

To get started, you will need a raspberry pi 3b that will serve as your controller, and a second raspberry pi 3b mounted on Rover. You will want a desktop img on your controller and a CLI on Rover.

-  [Clone this repo](https://github.com/seb3n/Rover.git) and run the respective install script on both the controller and Rover.

- If installing this on a new machine, make sure the machine has python3 at the latest verion.


- activate i2c using sudo raspi-config command => peripherals

- your root folder should look like the following on the rover: /home/pi/development/Rover/

- When testing the install, make sure it is done on the rover, as you will get an error from not having any sensors connected.

- Once tested without openCV, you can install opencv on a pytho-env 

## What's included

* OpenCV tracking.
* Forward distance measurement.
* Claw manupulation.
* Motion using tank tracks.

## Controller setup

Once the Repo is cloned on your device, you should be able to run 

``` 
$ python3 /home/pi/Rover/Controller/RaspTankTest.py
``` 
<br> This should display a GUI on your controller.

Now lets install OpenCV and other dependencies so that we can receive the camera stream from Rover.

on your controller, run the following commands:
```
$ cd
$ cd Rover/Controller
$ sudo python3 controller_setup.py
```


## Rover setup

run the install script

## Bugs and feature requests

Have a bug or a feature request? Please first read the [issue guidelines](https://github.com/seb3n/Rover/master/CONTRIBUTING.md) and search for existing and closed issues. If your problem or idea is not addressed yet, [please open a new issue](https://github.com/seb3n/Rover/issues/new).

## Creators

**SEB3N**

- <https://github.com/seb3n>

<a href='https://ko-fi.com/' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi4.png?v=0' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

## Thanks

Thanks to all contributors and their support:

## Copyright and license

Code and documentation copyright 2019 the authors. Code released under the [MIT License](https://github.com/seb3n/Rover/LICENSE).

Enjoy :metal:
