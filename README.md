# Pythonic Dog Door
Motorized door opening and closing, controlled by Jack the dog!

https://youtu.be/pmgy2o8wQfg

[![Video of the dog door operating](https://img.youtube.com/vi/pmgy2o8wQfg/0.jpg)](https://www.youtube.com/watch?v=pmgy2o8wQfg)


## Purpose
An door control mechanism that is able to be operated by a dog(Jack). I've trained Jack to know that the button opens the door, from both the inside and the outside.

The purpose of this project was to eliminate the need to cut a dog door into the existing door as I was in a rental house, while still giving Jack outdoor autonomy. It turned out to be a great project for both implementing hardware, and training a dog.

### Operation
The hardware was the difficult part of this project. It utilizes a Raspberry Pi as a controller. 
1. A liner motor opens the door
2. The door holds open for a set amount of time
3. The door starts closing
4. Two motion sensors start scanning for movement
5. If motion is detected, will halt for a set amount of time, then continue closing

### Issues
There are still two concerns with this setup:
1. A pressure sensor needs to be added for additional safety. If something(or someone) were to stand in the doorway and not move, the door would still continue to try closing. A pressure sensor bar would be able to detect something getting pinched and halt the closure.
2. The door is unable to be used manually and must be operated by bell. It is also a slow motor. This makes the door a pain to use for humans.

## Run
To start process, run 'python3 main_reader.py &'

## Archived - personal project no longer needed(Dog was adopted)
