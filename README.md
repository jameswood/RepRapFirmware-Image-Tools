# RepRapFirmware-Image-Tools
Python tools to generate and test RepRapFirmware LCD images from any common image format. Preserves the pixel dimensions, reduces to single-colour.

## Requirements
Python3

math, sys, and PIL libraries installed

## RRF-Gen.py
Generates images for use with the [RepRapFirmware 128x64 LCD implementation](https://duet3d.dozuki.com/Wiki/Duet_2_Maestro_12864_display_menu_system)

Usage: `./RRF-Gen.py [inputfile] [outputfile]`

eg: `./RRF-Gen.py nozzle.gif nozzle.img`

## RRF-View.py
Displays a preview of the images.

Usage: `./RRF-View.py [inputfile]`

## In use
I used this to generate some images for [my menu setup](https://github.com/jameswood/Duet-Maestro-Menu)
