# Christmas Card Python
Silly little Christmas card with lots of animations using Pygame

This was part of a small university project (and also something neat for Christmas!). It is more like a demonstration of some of the animations I can make using Pygame. You can also type in the boxes.

WARNING: May be a little slow on lower-end computers. I may try and figure out how to better optimise the program, but I have no plans to do so in the nearby future, and it still works fine as-is.

## Downloads
Downloads are found in [Releases](https://github.com/TheDragonary/Christmas-Card-Python/releases)
- [Windows](https://github.com/TheDragonary/Christmas-Card-Python/releases/latest/download/Christmas-Card-Windows.zip)
- [Linux](https://github.com/TheDragonary/Christmas-Card-Python/releases/latest/download/Christmas-Card-Linux.tar.gz)

## Screenshot
![](https://github.com/TheDragonary/Christmas-Card-Python/blob/main/screenshot.png)

## Building

Latest builds are already provided in [Releases](https://github.com/TheDragonary/Christmas-Card-Python/releases), however if you prefer to build, here's the instructions:

Clone the repo
```
git clone https://github.com/TheDragonary/Christmas-Card-Python
```
Install requirements
```
pip install -r requirements.txt
```
But really you just need Pygame, so you can just type
```
pip install pygame
```
You also need cx-freeze to be able to build the program
```
pip install cx-freeze
```
Run the setup file
```
python setup.py build
```
For Linux, run
```
python setup-linux.py build
```

<hr>

Music source: [Rockin' Around The Christmas Tree](https://www.youtube.com/watch?v=TFsZy9t-qDc)
