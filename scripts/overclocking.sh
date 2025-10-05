#!/bin/bash

 
LACT=$(curl -s https://api.github.com/repos/ilya-zlobintsev/LACT/releases/latest | grep -oP 'https://github\.com/ilya-zlobintsev/LACT/releases/download/[^"]*lact-headless[^"]*fedora-42\.rpm' | head -n 1)


dnf install -y $LACT
dnf install -y mangohud