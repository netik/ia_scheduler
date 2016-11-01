#!/bin/bash
#
# this is a collection of scripts to download the iceland airwaves
# data/schedule, and translate that data/schedule, along with a list of your
# favorite bands, into a filtered data/schedule that you can import into
# whatever.

# add additional bands to "additional_bands.txt"

# 1. Get the data/schedules...
if [ ! -f data/schedule.pdf ]; then 
  wget http://icelandairwaves.is/data/schedule.pdf
  wget http://icelandairwaves.is/data/schedule-off-venue.pdf
fi

# 2. translate them to text files. 
if [ ! -f data/schedule.txt ]; then
  pdf2txt.py data/schedule.pdf  > data/schedule.txt
fi

if [ ! -f data/schedule-off-venue.txt ]; then
  pdf2txt.py data/schedule-off-venue.pdf > data/schedule-off-venue.txt
fi

# go into spotify and export your account at
# http://www.spotmybackup.com
./gen_artist_cache.py

# run the matcher
echo "Now, go manually clean up schedule.txt and schedule-off-venue.txt"
echo "then run ./matcher.py !"
