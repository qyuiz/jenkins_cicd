#!/bin/bash

# Update package list
sudo apt update

# Install necessary packages
sudo apt install -y build-essential libbz2-dev libdb-dev libreadline-dev libffi-dev libgdbm-dev liblzma-dev libncursesw5-dev libsqlite3-dev libssl-dev zlib1g-dev uuid-dev tk-dev

# Download Python source
curl -O https://www.python.org/ftp/python/3.10.13/Python-3.10.13.tar.xz -o ~/Downloads/python-3.10.13.tar.xz

# Navigate to the Downloads directory
cd ~/Downloads

# Extract Python source
tar xJf python-3.10.13.tar.xz

# Navigate to the Python source directory
cd Python-3.10.13/

# Configure and install Python
./configure
make
sudo make install

# Install pip
sudo apt install -y python3-pip

# Upgrade pip
pip3 install --upgrade pip

# Install virtualenv
pip3 install virtualenv