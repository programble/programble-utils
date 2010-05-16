#!/bin/bash
sudo pacman -Sy > /dev/null
pacman -Qu | wc --lines