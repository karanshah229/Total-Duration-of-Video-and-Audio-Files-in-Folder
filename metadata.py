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


def print_duration(duration_in_secs):
    if(duration_in_secs < 3600):
        # MM:SS
        minutes = int(duration_in_secs // 60)
        seconds = int(math.floor(duration_in_secs - (minutes*60)))
        # Format the numbers correctly
        if(minutes < 10):
            minutes = str("0" + str(minutes))
        if(seconds < 10):
            seconds = str("0" + str(seconds))
        duration = str(minutes) + ":" + str(seconds)
    elif (duration_in_secs < 86400):
        # HH:MM:SS
        hours = int(duration_in_secs // 3600)
        minutes = int(math.floor(duration_in_secs - (hours * 3600)) // 60)
        seconds = int(math.floor(duration_in_secs -
                      (hours*3600) - (minutes*60)))
        # Format the numbers correctly
        if(hours < 10):
            hours = str("0" + str(hours))
        if(minutes < 10):
            minutes = str("0" + str(minutes))
        if(seconds < 10):
            seconds = str("0" + str(seconds))
        duration = str(hours) + ":" + str(minutes) + ":" + str(seconds)
    elif (duration_in_secs < 2592000):
        # DD:HH:MM:SS
        days = int(duration_in_secs // 86400)
        hours = int(math.floor(duration_in_secs - (days * 86400)) // 3600)
        minutes = int(math.floor(duration_in_secs -
                      (days*86400) - (hours*3600)) // 60)
        seconds = int(math.floor(duration_in_secs -
                      (days*86400) - (hours*3600) - (minutes*60)))
        # Format the numbers correctly
        if(days < 10):
            days = str("0" + str(days))
        if(hours < 10):
            hours = str("0" + str(hours))
        if(minutes < 10):
            minutes = str("0" + str(minutes))
        if(seconds < 10):
            seconds = str("0" + str(seconds))
        duration = str(days) + ":" + str(hours) + ":" + \
            str(minutes) + ":" + str(seconds)

    return duration


def divide(duration_in_secs, speed):
    duration_in_secs /= speed
    return print_duration(duration_in_secs)


if(len(sys.argv) > 1):
    files = sys.argv[1:len(sys.argv)]
else:
    files = os.listdir()
files = list(filter(only_video_audio_files, files))

cwd = os.getcwd().split("\\")[-1]
print("\n" + cwd.title(), ":", sep="")
# print(style.BRIGHT + fg.CYAN + cwd.title() + ":" + fg.RESET + style.RESET_ALL, sep="")
individual_file_duration = {}
total_duration_in_secs = 0
if(len(files) > 0):
    for file in files:
        metadata = TinyTag.get(file)
        individual_file_duration[file] = print_duration(
            math.floor(metadata.duration))
        total_duration_in_secs += metadata.duration

    total_duration_in_secs_str = print_duration(total_duration_in_secs)
    print("Total Duration:", total_duration_in_secs_str)
    print("No of files:", len(files))
    print("Average length of File:", print_duration(
        total_duration_in_secs / len(files)))
    print("Total Duration (1.25x):", divide(total_duration_in_secs, 1.25))
    print("Total Duration (1.5x):", divide(total_duration_in_secs, 1.5))
    print("Total Duration (1.75x):", divide(total_duration_in_secs, 1.75))
    print("Total Duration (2x):", divide(total_duration_in_secs, 2))
    print("Total Duration (2.5x):", divide(total_duration_in_secs, 2.5))
    print("")
    print("Enter 1 to get individual file duration")
    print("Enter 2 to enter custom multiplier (?)x")
    print("Enter any other character to quit")
else:
    print("No audio / video files found")
    print("Enter any character to quit")
    msvcrt.getch()

# Specially formatted Console Outputs
# print("Total Duration:", style.BRIGHT, total_duration_in_secs_str, style.RESET_ALL)
# print("No of files:", style.BRIGHT, len(files), style.RESET_ALL)
# print("Total Duration" + fg.GREEN, "(1.25x): "  + fg.RESET + fg.CYAN + divide(total_duration_in_secs, 1.25) + fg.RESET)
# print("Total Duration" + fg.GREEN, "(1.5x): "  + fg.RESET + fg.CYAN + divide(total_duration_in_secs, 1.5) + fg.RESET)
# print("Total Duration" + fg.GREEN, "(1.75x): " + fg.RESET + fg.CYAN + divide(total_duration_in_secs, 1.75) + fg.RESET)
# print("Total Duration" + fg.GREEN, "(2x): " + fg.RESET + fg.CYAN + divide(total_duration_in_secs, 2) + fg.RESET)
# print("Total Duration" + fg.GREEN, "(2.5x): " + fg.RESET + fg.CYAN + divide(total_duration_in_secs, 2.5) + fg.RESET)
# print("")
# print("Enter 1 to get individual file duration")
# print("Enter any other character to quit")

# 2. Get Duration for selected items - Dont know yet

try:
    while True:
        x = int(input())
        if x == 1:
            print()
            for x in individual_file_duration:
                print(x, " => ", individual_file_duration[x])
        elif x == 2:
            multiplier = float(input("\nEnter multiplier: "))
            print("Total Duration (",multiplier,"x): ", divide(total_duration_in_secs, multiplier), sep="")
        else: exit()
        print("\nEnter 1 to get individual file duration")
        print("Enter 2 to enter custom multiplier (?)x")
        print("Enter any other character to quit")
except Exception as e:
    # print(e)
    exit()
