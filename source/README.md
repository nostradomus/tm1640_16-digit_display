## Firmware

This folder contains the firmware source code related to the project :

version | name             | description
--------|------------------|--------------------------------------------------------------------------------------------
v1.0    | *.ino | 
The above Arduino sketches are to be loaded in the ATmega328p chip of the respective µ-controller board.

### External libraries
Some of these sketches require external libraries. Please check below table for cross-references. This source folder also contains snapshots from these libraries at the time of build (tested version). Libraries can be installed using the [standard procedure](https://www.arduino.cc/en/Guide/Libraries).

library              | to be used in    | origin                                               | docs                                                             | notes
---------------------|------------------|------------------------------------------------------|------------------------------------------------------------------|---------------------------------------------
lib-tm1638           | *.ino | [link](https://github.com/rjbatista/tm1638-library/) | [link](https://github.com/rjbatista/tm1638-library/wiki)         | to be used for the 16-digit display
