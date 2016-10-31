#!/bin/bash
#
# this is a collection of scripts to download the iceland airwaves
# schedule, and translate that schedule, along with a list of your
# favorite bands, into a filtered schedule that you can import into
# whatever.

# add additional bands to "additional_bands.txt"

# 1. Get the schedules...
if [ ! -f schedule.pdf ]; then 
  wget http://icelandairwaves.is/schedule.pdf
  wget http://icelandairwaves.is/schedule-off-venue.pdf
fi

# 2. translate them to text files. 
if [ ! -f schedule.txt ]; then
  pdf2txt.py schedule.pdf  > schedule.txt
fi

if [ ! -f schedule-off-venue.txt ]; then
  pdf2txt.py schedule-off-venue.pdf > schedule-off-venue.txt
fi

# go into spotify and export your account at
# http://www.spotmybackup.com
./gen_artist_cache.py

# run the matcher
./matcher.py
