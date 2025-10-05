#!/bin/bash

dnf install -y lutris
dnf install -y steam
dnf install -y wine winetricks

TMP_DIR="/tmp/heroic-install"
mkdir -p "$TMP_DIR"
cd "$TMP_DIR"

RPM_URL="https://sourceforge.net/projects/heroic-games-launcher.mirror/files/v2.18.1/Heroic-2.18.1-linux-x86_64.rpm/download"
wget "$RPM_URL" -O heroic.rpm
dnf install -y ./heroic.rpm
rm -rf "$TMP_DIR"