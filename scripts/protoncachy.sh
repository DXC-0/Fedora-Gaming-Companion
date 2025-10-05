#!/bin/bash

if [ -n "$SUDO_USER" ]; then
    ORIGINAL_HOME=$(eval echo "~$SUDO_USER")
elif [ -n "$PKEXEC_UID" ]; then
    ORIGINAL_HOME=$(getent passwd "$PKEXEC_UID" | cut -d: -f6)
else
    ORIGINAL_HOME="$HOME"
fi

PROTON_DIR="$ORIGINAL_HOME/.steam/root/compatibilitytools.d"
mkdir -p "$PROTON_DIR"
cd "$PROTON_DIR"

LATEST_URL=$(curl -s https://api.github.com/repos/CachyOS/proton-cachyos/releases/latest | \
  grep 'browser_download_url' | grep 'slr-x86_64\.tar\.xz' | cut -d '"' -f 4 | head -n 1)

if [[ -z "$LATEST_URL" || "$LATEST_URL" != *.tar.xz ]]; then
    echo "Release CachyOS non trouvée"
    exit 1
fi

FILE_NAME=$(basename "$LATEST_URL")
wget "$LATEST_URL" -O "$FILE_NAME"
tar -xvf "$FILE_NAME"
echo "Proton CachyOS installé dans : $PROTON_DIR"

HEROIC_DIR="$ORIGINAL_HOME/.config/heroic/tools/proton"
mkdir -p "$HEROIC_DIR"
cp "$FILE_NAME" "$HEROIC_DIR/"
cd "$HEROIC_DIR"
tar -xvf "$FILE_NAME"

echo "Proton CachyOS installé dans : $HEROIC_DIR"

rm -f "$PROTON_DIR/$FILE_NAME" "$HEROIC_DIR/$FILE_NAME"

if [ -n "$PKEXEC_UID" ]; then
    ORIGINAL_USER=$(getent passwd "$PKEXEC_UID" | cut -d: -f1)
    chown -R "$ORIGINAL_USER":"$ORIGINAL_USER" "$ORIGINAL_HOME/.steam"
    chown -R "$ORIGINAL_USER":"$ORIGINAL_USER" "$ORIGINAL_HOME/.config/heroic"
fi