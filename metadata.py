from tinytag import TinyTag
import os
import math
import msvcrt
import sys

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

files = os.listdir()
files = list(filter(only_video_audio_files, files))

cwd = os.getcwd().split("\\")[-1]
print(cwd.title(), ":", sep="")
individual_file_duration = {}
total_duration = "00:00"
if(len(files) > 0):
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
else:
    print("No audio / video files found")
    exit()

print("Total Duration:", total_duration)
print("No of files:", len(files))
print("Total Duration (1.25x):", divide(total_duration, 1.25))
print("Total Duration (1.5x):", divide(total_duration, 1.5))
print("Total Duration (1.75x):", divide(total_duration, 1.75))
print("Total Duration (2x):", divide(total_duration, 2))
print("")
print("Enter 1 to get individual file duration")
print("Enter any other character to quit")

# 2. Get Duration for selected items

try:
    x = int(input())
    if(x == 1):
        for x in individual_file_duration:
            print(x, " => ", individual_file_duration[x])
    else: print(False)
except Exception as e:
    exit()