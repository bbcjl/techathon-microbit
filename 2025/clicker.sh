#!/bin/bash

while read -r line < /dev/cu.usbmodem*; do
    echo $line

    if [ "$line" == "left" ]; then
        sendkeys --application-name "PowerPoint" --characters "<c:left>" --initial-delay 0
    fi

    if [ "$line" == "right" ]; then
        sendkeys --application-name "PowerPoint" --characters "<c:right>" --initial-delay 0
    fi
done