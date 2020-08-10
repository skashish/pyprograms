#!/usr/bin/env python3

# Downloads and combines video segments from the web. You need to put segment's url in proper order in the "link" variable.
# Tested on Debian 10 (Buster). Must work on Debian and Ubuntu derivatives.
# Dependencies: sudo apt install python3 wget ffmpeg

import os
import wget

directory = '/home/kashish/Downloads/.temp'

if not os.path.exists(directory):
    os.makedirs(directory)

os.chdir(directory)

segment_number = 1

retry_count = 0

while(True):
    try:
        link = 'https://cdn13.com/720p.h264.mp4/seg-' + str(segment_number) + '-v1-a1.ts?cdn_creation_time=15969&cdn_ttl=14456&cdn_cv_data=185.278.20.292&cdn_hash=7d801ca4868960a54297dd7853cf8c9'
        print("Downloading segement "+ str(segment_number))
        wget.download(link)
        print()
        segment_number = segment_number + 1
        continue
    except:
        if(retry_count < 4):
            print('Retrying segment '+ str(segment_number))
            retry_count = retry_count + 1
            continue
        else:
            print('Perhaps '+ str(segment_number-1) + ' was the last segment.')
            break

# Join all the segments.

os.system('touch mylist')
os.system('''for i in $(ls -vN *.ts); do  echo "file '$i'" >> mylist; done''')
os.system('ffmpeg -f concat  -safe 0 -i mylist -c copy all.ts')
os.system('ffmpeg -i all.ts -acodec copy -vcodec copy output.mp4')

# move the final output to Downloads folder and delete temporary folder.
os.system("mv output.mp4 ~/Downloads/ ")
os.system("rm -R " + str(directory))
