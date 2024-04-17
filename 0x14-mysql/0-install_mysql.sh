#!/usr/bin/env bash
# This script installs MySQL 5.7.x on web-01 and web-02 servers.

# Update apt package index
sudo apt-get update

# Install MySQL server
sudo apt-get install -y mysql-server-5.7

# Verify installation
mysql --version

