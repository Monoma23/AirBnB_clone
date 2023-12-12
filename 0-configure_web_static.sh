#!/usr/bin/env bash
# Bash script for configuring web servers for web_static deployment

# Update package lists
sudo apt-get -y update

# Upgrade installed packages
sudo apt-get -y upgrade

# Install nginx web server
sudo apt-get -y install nginx

# Create necessary directories for web_static
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a test HTML file
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link to the current deployment
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership and permissions for directories
sudo chown -hR ubuntu:ubuntu /data/

# Configure nginx to serve web_static content
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Start nginx service
sudo service nginx start
