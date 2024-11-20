#!/bin/bash

# 1. Update system and install dependencies
echo "Updating system and installing dependencies..."
apt update -y
apt install -y wget unzip curl python3 python3-pip libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1 \
    libx11-xcb1 libxcomposite1 libxcursor1 libxdamage1 libxrandr2 libasound2 libatk1.0-0 libcups2 \
    libdbus-1-3 libxss1 libxtst6 fonts-liberation libappindicator3-1 libindicator7 xdg-utils xvfb

# 2. Install Google Chrome
echo "Installing Google Chrome..."
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O google-chrome-stable.deb
apt install -y ./google-chrome-stable.deb
rm google-chrome-stable.deb
echo "Installed Google Chrome version: ${google-chrome --version}"

# 3. Install ChromeDriver
echo "Installing ChromeDriver..."
CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d '.' -f 1)
wget https://chromedriver.storage.googleapis.com/${CHROME_VERSION}.0/chromedriver_linux64.zip -O chromedriver.zip
unzip chromedriver.zip
mv chromedriver /usr/local/bin/
chmod +x /usr/local/bin/chromedriver
rm chromedriver.zip
echo "Installed ChromeDriver verision: ${chromedriver --version}"

# 4. Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# 5. Complete setup
echo "Complete setup."
