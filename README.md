<p align="center">
  <a href="https://github.com/seb3n/Rover">
    <img src="images/rover.png" alt="Logo">
  </a>

 <h3 align="center">Rover</h3>

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

# Table of contents

- [Table of contents](#table-of-contents)
- [What's Included](#whats-included)
- [Getting Started](#getting-started)
  - [Controller Setup](#controller-setup)
  - [Rover Setup](#rover-setup)
- [Bugs and Feature Requests](#bugs-and-feature-requests)
- [Creators](#creators)
- [Thanks](#thanks)
- [Copyright and license](#copyright-and-license)


# What's Included

* OpenCV tracking.
* Forward distance measurement.
* Claw manupulation.
* Motion using tank tracks.

# Getting Started

To get started, you will need a raspberry pi with a desktop image(tested on the raspberry pi 3b) that will serve as your controller, and a second raspberry pi (CLI image) mounted on Rover (tested with pi 3b and 4).

-  Clone [this](https://github.com/seb3n/Rover.git) repo to both controller and Rover.

- If installing this on a new machine, make sure the machine has python3 installed. You can do this using:
 ``` 
$ sudo apt-get install python3
```

- Assuming you clone the repo into your home directory, it should look like the following: ```/home/pi/Rover/```

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

Once the install is complete, reboot the contoller if it did not do so automatically.

That should be it in terms of setting up the controller. Now let's configure Rover.

<br>

## Rover Setup

Let's run the install script on Rover, just like we did on the controller.
```
$ cd Rover/server
```

# Bugs and Feature Requests

Have a bug or a feature request? Please first read the [issue guidelines](https://github.com/seb3n/Rover/master/CONTRIBUTING.md) and search for existing and closed issues. If your problem or idea is not addressed yet, [please open a new issue](https://github.com/seb3n/Rover/issues/new).

# Creators

**ADEEPT**

- <https://github.com/adeept>

**SEB3N**

- <https://github.com/seb3n>

<a href='https://ko-fi.com/' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi4.png?v=0' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

# Thanks

Thanks to all contributors and their support:

# Copyright and license

Code and documentation copyright 2019 the authors. Code released under the [MIT License](https://github.com/seb3n/Rover/LICENSE).

Enjoy :metal:
