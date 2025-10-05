#!/bin/bash

GPU_INFO=$(lspci | grep -E "VGA|3D")

if echo "$GPU_INFO" | grep -qi "NVIDIA"; then
    dnf install -y akmod-nvidia xorg-x11-drv-nvidia-cuda
elif echo "$GPU_INFO" | grep -qi "AMD"; then
    dnf install -y mesa-dri-drivers mesa-libGL mesa-vulkan-drivers
elif echo "$GPU_INFO" | grep -qi "Intel"; then
    # Aucun pilote spécifique à installer
    :
else
    echo "GPU non reconnu automatiquement"
fi