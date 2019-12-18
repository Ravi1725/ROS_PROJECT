# ROS_PROJECT
Internship at IITP in summer recess(2019)-Topic ROS_PROJECT

# LED_BLINK_ROS_CODE
1) INSTALLATION OF UBUNTU 18.04 0N RASPBERRY PI: -
  a) Download the ubuntu mate 18.04 from webpage (https://ubuntu-mate.org/download/)
  b) Extract the Ubuntu image
  c) Format the SD card (Windows 10) through command prompt
  d)Make the SD card bootable through Rufus software and write the ubuntu image.
  e) Insert SD card to the raspberry pi and connect the raspberry pi to the monitor through HDMI port.
  f) Set up the ubuntu on raspberry pi 
You can follow this link(https://www.techradar.com/how-to/how-to-install-ubuntu-on-the-raspberry-pi)



2) INSTALLATION OF ROS(MELODIC) ON UBUNTU MATE 18.04: -
  Follow the steps of this webpage (https://www.intorobotics.com/installing-ros-melodic-on-raspberry-pi-3b-running-ubuntu-mate-   18-04-2-bionic/)
  
  
3) MANAGING YOUR ENVIRONMENT: -
	$ printenv | grep ROS
	$ source /opt/ros/<distro>/setup.bash
	$ source /opt/ros/melodic/setup.bash
  
  
4) SETTING ROS WORKSPACE: -
	$ mkdir -p ~/catkin_ws/src 
	$ cd ~/catkin_ws/ 
	$ catkin_make
	$ source devel/setup.bash
	$ echo $ROS_PACKAGE_PATH /home/youruser/catkin_ws/src:/opt/ros/melodic/share


LED BLINKING WORK
First step, we have to download "wiringPi" for downloading wiringPi follow run follow code:-
$ git clone git://git.drogon.net/wiringPi
$ cd wiringPi
$ sudo ./build
 

GPIO PIN DIAGRAM OF RASPBERRY PI3,WIRINGPI NUMBER IS DIFFERENT FROM GPIO PIN NUMBER,
WIRINGPI NUMBER CORRESSPONDING TO PIN NUMBER IS SHOWN IN BELOW PHOTO.

Physical connection:
Anode of LED is connected to 12th pin of raspberry pi3
Cathode of LED is connected to any ground pin of raspberry pi3
 
$ cd ~/catkin_ws
$ catkin_create_pkg ros_wiring_example roscpp std_msgs
$ cd ros_wiring_examples
$ mkdir src
$ cd src
$ vi blink_led.cpp and put source code in this text editor and save it
$ vi button_led.cpp and put source code in this text editor and save it
$ cd ..
$ vi CMakeLists.txt (modify the CMakeLists.txt given in another file)
$ cd ~/catkin_ws
$ catkin_make
Open another terminal and run roscore
Open another terminal and run following code: -
$ cd ~/catkin_ws
$ source devel/setup.bash
$ cd build
$ cd src
$ cd ros_wiring_example
$ ./blink_led
Open one more terminal and run
$ cd ~/catkin_ws
$source devel/setup.bash
$ rostopic pub /led_blink std_msgs/Bool 1(Led start glowing)
$ rostopic pub /led_blink std_msgs/Bool 0(Led will go to OFF state)



PUBLISHING Bool 1 AND Bool 0 ON TOPIC THROUGH CODE: -
Open the terminal 
$ cd ~/catkin_ws/src/ros_wiring_example/src
$ vi exp.py and (put the code here, provided in another file)
$ chmod +x exp.py
$ cd ~/catkin_ws
$ source devel/setup.bash
Terminal in which roscore and./blink_led is running should be open.
$ rosrun ros_wiring_example exp.py
