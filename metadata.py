from tinytag import TinyTag
import os
import math
import msvcrt
import sys
import time

# Terminal color definitions

# class fg:
#     BLACK   = '\033[30m'
#     RED     = '\033[31m'
#     GREEN   = '\033[32m'
#     YELLOW  = '\033[33m'
#     BLUE    = '\033[34m'
#     MAGENTA = '\033[35m'
#     CYAN    = '\033[36m'
#     WHITE   = '\033[37m'
#     RESET   = '\033[39m'

# class bg:
#     BLACK   = '\033[40m'
#     RED     = '\033[41m'
#     GREEN   = '\033[42m'
#     YELLOW  = '\033[43m'
#     BLUE    = '\033[44m'
#     MAGENTA = '\033[45m'
#     CYAN    = '\033[46m'
#     WHITE   = '\033[47m'
#     RESET   = '\033[49m'

# class style:
#     BRIGHT    = '\033[1m'
#     DIM       = '\033[2m'
#     NORMAL    = '\033[22m'
#     RESET_ALL = '\033[0m'

def only_video_audio_files(file):
    valid_extensions = [".mp4", ".mp3", ".m4a", ".m3a",
                        ".avi", ".flv", ".aac", ".ogg", ".wav", ".wma", ".raw", ".mov", ".webm", ".mpg", ".mpeg", ".3gp", ".mkv"]
    for valid_extension in valid_extensions:
        if valid_extension in file:
            return True
    return False


def add_durations(orignal, dur):
    # Split on :
    og = orignal.split(":")
    new = dur.split(":")

    # Convert all strings to numbers
    for i in range(len(og)):
        og[i] = (int)(og[i])
    for i in range(len(new)):
        new[i] = (int)(new[i])

    size = min(len(new), len(og))
    carry = 0
    res = []

    for i in range(size-1, -1, -1):
        res.insert(0, og[i] + new[i] + carry)
        if res[0] >= 60:
            res[0] %= 60
            carry = 1
            if i == 0:
                res.insert(0, 1)
        else: carry = 0

    if(len(new) > len(og)):
        for i in range(len(new)-1-size, -1, -1):
            res.insert(0, new[i])
    else:
        for i in range(len(og)-1-size, -1, -1):
            res.insert(0, og[i])

    return ":".join(map(str, res))

def divide(duration, speed):
    og = duration.split(":")

    for i in range(len(og)):
        og[i] = (int)(og[i])

    for i in range(len(og)):
        og[i] /= speed
        og[i] = (int)(og[i])

    return ":".join(map(str, og))

if(len(sys.argv) > 1):
    files = sys.argv[1:len(sys.argv)]
else:
    files = os.listdir()
files = list(filter(only_video_audio_files, files))

cwd = os.getcwd().split("\\")[-1]
# print(style.BRIGHT + fg.CYAN + cwd.title() + ":" + fg.RESET + style.RESET_ALL, sep="")
individual_file_duration = {}
total_duration = "00:00"
if(len(files) > 0):
    print(cwd.title(), ":", sep="")
    for file in files:
        metadata = TinyTag.get(file)
        duration = ""
        if(metadata.duration < 3600):
            # MM:SS
            duration = str( str(math.floor(metadata.duration / 60)) + ":" + str((math.floor(metadata.duration) % 60)) )
        elif (metadata.duration < 86400):
            # HH:MM:SS
            duration = str( str(math.floor(metadata.duration / 3600)) + ":" + str(math.floor(metadata.duration / 60)) + ":" + str((math.floor(metadata.duration) % 60)) )
        
        individual_file_duration[file] = duration
        total_duration = add_durations(total_duration, duration)
    
    print("Total Duration:", total_duration)
    print("No of files:", len(files))
    print("Total Duration (1.25x):", divide(total_duration, 1.25))
    print("Total Duration (1.5x):", divide(total_duration, 1.5))
    print("Total Duration (1.75x):", divide(total_duration, 1.75))
    print("Total Duration (2x):", divide(total_duration, 2))
    print("")
    print("Enter 1 to get individual file duration")
    print("Enter any other character to quit")
else:
    print("No audio / video files found")
    msvcrt.getch()

# Specially formatted Console Outputs
# print("Total Duration:", style.BRIGHT, total_duration, style.RESET_ALL)
# print("No of files:", style.BRIGHT, len(files), style.RESET_ALL)
# print("Total Duration" + fg.GREEN, "(1.25x): "  + fg.RESET + fg.CYAN + divide(total_duration, 1.25) + fg.RESET)
# print("Total Duration" + fg.GREEN, "(1.5x): "  + fg.RESET + fg.CYAN + divide(total_duration, 1.5) + fg.RESET)
# print("Total Duration" + fg.GREEN, "(1.75x): " + fg.RESET + fg.CYAN + divide(total_duration, 1.75) + fg.RESET)
# print("Total Duration" + fg.GREEN, "(2x): " + fg.RESET + fg.CYAN + divide(total_duration, 2) + fg.RESET)
# print("")
# print("Enter 1 to get individual file duration")
# print("Enter any other character to quit")

# 2. Get Duration for selected items - Dont know yet

try:
    x = int(input())
    if(x == 1):
        for x in individual_file_duration:
            print(x, " => ", individual_file_duration[x])
    msvcrt.getch()
except Exception as e:
    exit()