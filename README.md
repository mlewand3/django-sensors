Read and store dallas 1-wire temperature sensor values. It was written for the 
  Raspberry Pi, so you might have to do some tweaking to get things working on
  other platforms.

# Windows / OS X

Are not supported.

# Installation (Linux)

You'll need the following packages to run the app:

- PIP
- virtualenv
- Python's sqlite interface package

## Device Installation

Since this project is designed to read 1-wire sensors, you'll need to have the
  appropriate kernel modules loaded.

- w1-gpio

And probably

- w1-therm

After that, if you've got 1-wire devices connected, there should be more than 
  one symlink in /sys/bus/w1/devices

## App Setup

- clone this app somewhere
- `cd` into your clone
- run the setup script `./setup.sh`
- enter your new virtual environment `source env/bin/activate`
- set up the database `./server/manage.py syncdb`
- collect static assets `./server/manage.py collectstatic --noinput`
- test that the app runs by running `./server/manage.py runserver 0.0.0.0:2000`

## Cron Job Install

So, we're not using django-cellery or anything like that here- this was designed 
  to run on an embedded linux machine like a Pi, so we're trying to keep the 
  number of required services to a minumum. SO.. You'll need to install a cron
  job- it all depends on how often you want to record temperatures. If you need
  sub-minute readings, the simplest way achieve this is to create a bash script
  with a `while true` loop with a sleep statement and run it on startup.
  Here's an example;

    #! /bin/bash

    while [true]; do
        wget http://localhost/update-readings/
        sleep 10
    done

See that url? Yeah, that can be hit from anything that can reach the box. If
  that's not what you want you'll need to alter that behaviour.

## Apache Setup

At work, I'm a Django / PHP DevOps, and I usually deploy Python stuff on uWSGI-
  however, this isn't an app that's supposed to handle 10k concurrent users, the
  web administration is really just sugar on top, so for ease of installation,
  I recommend Apache with mod\_wsgi.

There are plenty of guides on how to set this up, and I'm not going to cover it
  in detail here.

The things you'll want to watch out for are:

- pass the 'user' argument to set the UID of the daemon processes, make it match
  the UID of the owner of the files on disk (otherwise you'll get sqlite errors
  or worse)
- if you followed this guide without modifying settings, your static files will
  be located at the root of your clone, in a folder called *static*

## Usage

So, you've made it! You now have the app running. To see a dashboard of your 
  gauges, visit the device's IP address.

You'll want to be sure to reboot the device to verify that you've got everything
  set up to run on boot.

