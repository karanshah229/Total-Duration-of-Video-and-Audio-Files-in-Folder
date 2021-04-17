from tinytag import TinyTag
import os
import math
import msvcrt
import sys


def only_video_audio_files(file):
    valid_extensions = [".mp4", ".mp3", ".m4a", ".m3a", ".avi", ".flv"]
    for valid_extension in valid_extensions:
        if valid_extension in file:
            return True
    return False


files = os.listdir()
files = list(filter(only_video_audio_files, files))

cwd = os.getcwd().split("\\")[-1]
print(cwd.title(), ":", sep="")
if(len(files) > 0):
    for file in files:
        metadata = TinyTag.get(file)
        print(file, " ", math.floor(metadata.duration / 60),
              ":", (math.floor(metadata.duration) % 60), sep="")
else:
    print("No audio / video files found")

# 1. Add time to get Total Duration
# 2. Get Duration for selected items

msvcrt.getch()
