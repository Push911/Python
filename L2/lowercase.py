import os
import sys


def lower_case_all(dirname):
    for dirpath, dirs, files in os.walk(dirname, topdown=False):

        for filename in files:
            os.rename(os.path.join(dirpath, filename),
                      os.path.join(dirpath, filename.lower()))

        for adir in dirs:
            os.rename(os.path.join(dirpath, adir),
                      os.path.join(dirpath, adir.lower()))

    os.rename(dirname, dirname.lower())


# /home/push/Desktop/4Sem/Python/L2
if sys.argv[1]:
    lower_case_all(sys.argv[1])
else:
    print("Please pass the paths to check as parameters to the script")


