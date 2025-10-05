#!/bin/bash

mkdir -p $HOME/.tmp/
cd $HOME/.tmp/
dnf remove -y protonplus-next
wget https://download.copr.fedorainfracloud.org/results/wehagy/protonplus/fedora-42-x86_64/09353354-protonplus-next/protonplus-next-0.5.12-2.fc42.x86_64.rpm
dnf install -y protonplus-next-0.5.12-2.fc42.x86_64.rpm
rm -rf $HOME/.tmp/