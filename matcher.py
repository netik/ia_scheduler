#!/usr/bin/python

import codecs
import re

# matcher.py - matches up bands and the schedule together
sched = {}

def genkey(k):
    k = k.upper()
    k = re.sub(' \([a-zA-Z /]+\)$','',k)
    return k

# open band files
def prettyprint(s):
    for act in s: 
        print act["venue"]
        print "%s: %s" % (act["date"], act["time"])

def load_artists():
    af = codecs.open("data/artists_cache.txt", "r", "utf-8")
    artists = {}
    
    for line in af:
        if not line.startswith("#"):
            artists[line.rstrip()] = 1

    altf = codecs.open("data/additional_artists.txt", "r", "utf-8")

    for line in altf:
        if not line.startswith("#"):
            artists[line.rstrip()] = 1

    return artists

def parse_unofficial():
    return

def parse_official():
    # sets the global state array with the schedule
    state = 0
    lastdate = ""
    lastvenue = ""
    sf = codecs.open("data/schedule.txt","r","utf-8")

    for line in sf:
        theline=line.rstrip()
        if len(theline) == 0:
            continue

        # filthy. There's got to be a better way. 
        if theline.find(" NOV ") > 0:
            state = 0

        if state == 2 and (re.match("^\d\d\:",theline) == None):
            state = 1

        if state == 0:
            # date
            lastdate = theline
            state = state + 1
        elif state == 1:
            lastvenue = theline
            state = state + 1
        elif state == 2:
            parts = re.split(' +',theline, maxsplit=1)
            key = genkey(parts[1])
            
            if sched.has_key(key):
                sched[key].append({ "date": lastdate,
                                    "venue": lastvenue,
                                    "time": parts[0],
                                    "artist": parts[1] })
            else:
                sched[key] = [{ "date": lastdate,
                                "venue": lastvenue,
                                "time": parts[0],
                                "artist": parts[1] }];
                
# load bands
artists_sorted = sorted(load_artists())

# parse official schedule
parse_official()
parse_unofficial()

    
# ============= output stage ===========
# this is by-artist 
for artist in artists_sorted:
    print artist
    if sched.has_key(genkey(artist)):
        prettyprint(sched[genkey(artist)])
        print
    else:
        print "None."
        print

