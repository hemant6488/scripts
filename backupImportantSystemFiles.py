#!/usr/local/bin/python3
################################################
# This script is intended to run with python3  #
# Desc  : Back up import files to Cloud synced #
#         local directory on the system.       #
# Author: hemant6488                           #
# Email : hemant6488@gmail.com                 #
################################################

import configparser
import os.path
import sys
import shutil

#config filename in the current working directory
configFilePath = os.path.join(os.getcwd(),'.config')

config = configparser.ConfigParser()
config.read(configFilePath)

try:
    fileNames = config.get("backup", "fileNames").split("\n")
    cloudDirectory = config.get("backup", "cloudDirectory")
    print(cloudDirectory)
    print(fileNames)
except configparser.Error:
    print('Configuration file could not be read at the location: ' + configFilePath)
    sys.exit(1)

try:
    for filename in fileNames:
        shutil.copy2(os.path.expanduser(filename), os.path.dirname(cloudDirectory))
except shutil.Error:
    print('Error while copying files.')
