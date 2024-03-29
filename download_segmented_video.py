#!/usr/bin/env python3

# Downloads and combines video segments from the web. You need to put segment's url in proper order in the "link_prefix" and "link_suffix" variable.
# Tested on Ubuntu 23.10. Must work on Debian and Ubuntu derivatives.
# Dependencies: sudo apt install python3 python3-wget ffmpeg
# Written by kashish sharma. Github link: https://github.com/skashish/pyprograms/blob/master/download_segmented_video.py

import os
import sys
import wget
import threading

directory = str(os.environ['HOME'])+'/Downloads/.temp'

if not os.path.exists(directory):
    os.makedirs(directory)

os.chdir(directory)

segment_number = 1

link_prefix = ''
link_suffix = ''

def Join_all_segments():
    os.system('touch mylist')
    os.system('''for i in $(ls -vN *.ts); do  echo "file '$i'" >> mylist; done''')
    os.system('ffmpeg -f concat  -safe 0 -i mylist -c copy all.ts')
    os.system('ffmpeg -i all.ts -acodec copy -vcodec copy output.mp4')
    # move the final output to Downloads folder and delete temporary folder.
    os.system("mv output.mp4 ~/Downloads/ ")
    #os.system("rm -R " + str(directory))

while(True):
    link1 = link_prefix + str(segment_number) + link_suffix
    link2 = link_prefix + str(segment_number + 1) + link_suffix
    link3 = link_prefix + str(segment_number + 2) + link_suffix
    link4 = link_prefix + str(segment_number + 3) + link_suffix

    def task1():
        try:
            print("Downloading segement "+ str(segment_number))
            wget.download(link1)
        except Exception as e:
            print("Exception in Task 1:", e)
            Join_all_segments()
            sys.exit()
        print()
    def task2():
        try:
            print("Downloading segement "+ str(segment_number + 1))
            wget.download(link2)
        except Exception as e:
            print("Exception in Task 1:", e)
            Join_all_segments()
            sys.exit()
        print()
    def task3():
        try:
            print("Downloading segement "+ str(segment_number + 2))
            wget.download(link3)
        except Exception as e:
            print("Exception in Task 1:", e)
            Join_all_segments()
            sys.exit()
        print()
    def task4():
        try:
            print("Downloading segement "+ str(segment_number + 3))
            wget.download(link4)
        except Exception as e:
            print("Exception in Task 1:", e)
            Join_all_segments()
            sys.exit()
        print()
    
    # Create threads
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)
    thread3 = threading.Thread(target=task3)
    thread4 = threading.Thread(target=task4)

    # Start threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # Wait for threads to finish
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    segment_number = segment_number + 4
    retry_count = 0
    continue


