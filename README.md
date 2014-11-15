Read and store dallas 1-wire temperature sensor values. It was written for the Raspberry Pi, so you might have to do
 some tweaking to get things working on other platforms.

# Windows / OS X

Are not supported.

# Installation (Linux)


Since this project is designed to read 1-wire sensors, you'll need to have the appropriate kernel modules loaded.

- w1-gpio

And probably

- w1-therm

After that, if you've got 1-wire devices connected, there should be more than one symlink in /sys/bus/w1/devices



