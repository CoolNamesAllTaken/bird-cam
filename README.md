# bird-cam
This project is created with the objective of using camera-based motion detection to capture pictures of birds at a window bird feeder.  As configured, this code is meant to run on a raspberry pi using a pi camera in conjunction with the [motion firmware](https://motion-project.github.io).

## Relevant Ports

Live Camera Stream: 8081

SSH: 8082

![image of birb](https://i.imgur.com/HvVQGKY.jpg)

## Overview

### Folder Structure
* `images/` contains disk images for setting up the raspberry pi
* `src/` contains scripts that will be put into the `/home` folder on the pi
	* `src/pi/config` contains configuration files for Motion
	* `src/pi/motion_files` is the directory on the pi where captured images will be uploaded
	* `src/pi/scripts` is the directory used for storing startup scripts, automated posting scripts, etc

## Detailed Setup
The following details document steps that were done during the creation of birdcam, for those wishing to configure a similar project on their own.

### Set up SSH over USB
Follow [these steps](https://www.thepolyglotdeveloper.com/2016/06/connect-raspberry-pi-zero-usb-cable-ssh/) to enable SSHing into the pi over a USB connection.

### Setting Raspberry Pi System Time
SSH into the pi and run `sudo raspi-config`.  Select Localization > Time Zone and update the current time zone of the device.  If the device is connected to the internet, the system time will update automatically.

### Configuring Motion
Motion can be configured using its config file, which has been symlinked from its normal home at `etc/motion/motion.conf` to the `/home/pi/config` folder in the system images on this repository.  The config files included in this repository have been modified to expose a camera stream from the pi, mask out the top half of the frame (to ignore trees / shadows / etc for motion detection), capture images at a high frame rate when motion is detected, and more.  The full list of confiurable parameters can be found on the [Motion reference](https://motion-project.github.io/motion_config.html#area_detect).

### Setting Up Motion with Crontab
The motion service needs to be configured to start every time the raspberry pi boots up.  The file `startup.sh` in `/home/pi/scripts` should be set up to run on boot.

SSH into the pi and run the following command: `sudo crontab -e`.  This will bring up the configuration file for the crontab service, which can be used to run files at specific time intervals on the pi.

Using the built-in text editor, append the following line to the end of the crontab file: `@reboot sh /home/pi/scripts/startup.sh > /var/log/startup.log`.  This will run the `startup.sh` file as a shell script, and will output any dialog to `/var/log/startup.log` on the pi.  If you have issues with the motion service, check this log file for errors.