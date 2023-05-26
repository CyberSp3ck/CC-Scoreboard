#!/usr/bin/env bash

set -e

usage() {
    echo "Usage: $0 xfce"
    exit 1
}

if [ $# -ne 1 ]; then
    usage
fi

mkdir -p ~/.local/share/fonts
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.3.3/JetBrainsMono.zip
unzip JetBrainsMono.zip -d ~/.local/share/fonts
rm JetBrainsMono.zip
fc-cache -fv

case "$1" in
    xfce)
        mkdir -p ~/.config/xfce4/terminal
        if [ -f ~/.config/xfce4/terminal/terminalrc ]; then
            mv ~/.config/xfce4/terminal/terminalrc ~/.config/xfce4/terminal/terminalrc.bak
        fi
        cp ./configs/xfce ~/.config/xfce4/terminal/terminalrc
        ;;
    *)
        usage
        ;;
esac
