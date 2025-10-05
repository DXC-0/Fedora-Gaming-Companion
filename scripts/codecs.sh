#!/bin/bash

dnf groupupdate -y multimedia --setop="install_weak_deps=False" --exclude=PackageKit-gstreamer-plugin
dnf groupupdate -y sound-and-video

dnf install -y \
  gstreamer1-plugins-{base,good,bad-free,bad-freeworld,ugly} \
  gstreamer1-libav lame \
  libavcodec-freeworld