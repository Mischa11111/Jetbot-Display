Script to automatically display the IP address on the small screen at the back of the jetbot for Ubuntu image. Usable for SSH direct connection without having to manually check IP
address of Wifi via connecting monitor etc.


1. Dependencies:

# Update and upgrade the system
sudo apt update
sudo apt upgrade -y

# Install Python and pip if needed
sudo apt install python3 python3-pip -y

# Install required Python libraries
sudo pip3 install Adafruit-SSD1306
sudo pip3 install Pillow
sudo pip install netifaces

# Install additional dependencies
sudo apt install i2c-tools -y
sudo apt install python3-smbus -y

# navigate to home folder, create new directory for display scripts e.g. disp
mkdir disp

2. copy python script disp_IP.py into the folder, make it executable
3. open startup applications, add new Startup Program
4. Name: ....
   Command: [path/to/python3] [path/to/disp_IP.py] # get path to python3 with $ which python3 and path to script with realpath disp_IP.py
   Comment: ....

Now the script should run on startup, and if your jetbot is connected to a Wifi-network, the IP address should be shown on the small screen at the back.
