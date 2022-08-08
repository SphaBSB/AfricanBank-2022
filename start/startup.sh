#!/bin/sh
RED='\033[0;31m'
NOCOLOR='\033[0m'
YELLOW ='\033[0,32m-'

echo "${RED}WARNING: ${NOCOLOR}This script will install PYTHON AND add it as an apt source."
echo ""
echo "If you do not want this, please press ctrl + C to cancel the script."
echo ""
echo "The script will start in 10 seconds."

sleep 10

echo "${YELLOW}Running African Bank app setup..."

# Install Python if necessary
which python3 > /dev/null
status=$?

if test $status -ne 0
then
	echo "Installing Python 3.6..."
	apt-get install python3.6 -y

else
	echo "Confirmed Python is installed."
	
	# Installs Pip even if a Python installation is found because some users don't install pip
	
	sudo apt install python3-pip

fi


# Install Python packages
echo "Installing Python packages..."
python3 -m pip install CMake==3.18.4
python3 -m pip install -r requirements.txt


read -p "To use some Coffin Codes v8 features, you must reboot your system. If this is not your first time running this script, please answer no. Reboot now? [Y/n]: " agreeTo
#Reboots system if user answers Yes
case $agreeTo in
    y|Y|yes|Yes|YES)
    echo "Rebooting..."
    sleep 1
    sudo reboot now
    exit
    ;;
#Runs app if user answers No
    n|N|no|No|NO)
    cd ..
    echo "Running C2 server with";
    echo "Navigate to http://127.0.0.1:5000 and set up your user to get started.";
    python3 app.py
    exit
    ;;
esac
