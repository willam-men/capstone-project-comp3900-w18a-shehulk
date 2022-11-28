#!/bin/bash

# Setup our Demo environment for the project 
cd ~/cs3900/capstone-project-comp3900-w18a-shehulk-main/
touch .env 
echo "DB_HOST=db
PG_USER=demo
PG_USER_PASSWORD=password
PG_ADMIN_EMAIL=demo@mail.com
PG_ADMIN_PASSWORD=password
FLASK_SECRET=demoSecret

FLASK_APP=project/__init__.py
FLASK_ENV=development" > .env

# Setup shorthand commands in .bashrc for convenience
touch ~/.bashrc 
echo "alias dostart='cd ~/cs3900/capstone-project-comp3900-w18a-shehulk-main/ && sudo service docker start && sudo docker-compose up -d --build'" >> ~/.bashrc
echo "alias dostop='cd ~/cs3900/capstone-project-comp3900-w18a-shehulk-main/ && sudo docker-compose down -v && sudo service docker stop'" >> ~/.bashrc 
echo "alias festart='cd ~/cs3900/capstone-project-comp3900-w18a-shehulk-main/frontend/ && npm start'" >> ~/.bashrc
echo "alias pypop='python3 -m pytest ~/cs3900/capstone-project-comp3900-w18a-shehulk-main/'" >> ~/.bashrc


source ~/.bashrc

# Setup the Docker repository 
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker engine
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

sudo apt install docker-compose

# install NodeJs

curl -fsSL https://deb.nodesource.com/setup_19.x | sudo -E bash - &&\

sudo apt-get install -y nodejs

sudo npm install -g npm@9.1.1

# Instal Node.js modules required by our frontend
cd ~/cs3900/capstone-project-comp3900-w18a-shehulk-main/frontend/ && npm install --force

# Install Python3 and Pytest for populating db with test data
sudo apt-get update 
sudo apt-get install python3.6
sudo apt install python3-pip
sudo pip3 install pytest 






