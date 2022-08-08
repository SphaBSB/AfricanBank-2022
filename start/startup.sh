#!/bin/sh

RED='\033[0;31m'

NOCOLOR='\033[0m'

YELLOW='\033[0,34m'

GREEN='\033[0;32m'



echo "${RED}WARNING: ${NOCOLOR}This script will install PYTHON AND add it as an apt source."

echo ""

echo "If you do not want this, please press ctrl + C to cancel the script."

echo ""

echo "The script will start in 10 seconds."

echo "${GREEN}@BSB-Developers 2022 ${NOCOLOR}"



sleep 10



echo "${YELLOW}Running African Bank app setup...${NOCOLOR}"



# Install Python if necessary

which python3 > /dev/null

status=$?



if test $status -ne 0

then

	echo "${RED}Installing Python 3.6...${NOCOLOR}"

	apt-get install python3.6 -y



else

	echo "${RED}Confirmed Python is installed.${NOCOLOR}"

	

	# Installs Pip even if a Python installation is found because some users don't install pip

	

	sudo apt install python3-pip



fi





# Install Python packages

echo "${YELLOW}Installing Python packages...${NOCOLOR}"

python3 -m pip install CMake==3.18.4

python3 -m pip install -r requirements.txt





read -p" Open Your DATA File with Information = [Y].  Run the Code = [R] " agreeTo

#Reboots system if user answers Yes

case $agreeTo in

    y|Y|yes|Yes|YES)

    echo "Opening File.........."

    sleep 1

    cat Data.csv

    exit

    ;;

#Runs app if user answers No

    r|R|RUN|Run|run)

    cd ..

    echo "${YELLOW}Running C2 server${NOCOLOR}";

    echo "${RED}Navigate to http://127.0.0.1:5000 and set up your user to get started.${NOCOLOR}";

    python3 start/app.py

    exit

    ;;

esac
