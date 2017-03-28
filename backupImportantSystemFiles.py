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
    #print(cloudDirectory)
    #print(fileNames)
except configparser.Error:
    print('Configuration file could not be read at the location: ' + configFilePath)
    sys.exit(1)

try:
    if cloudDirectory.startswith('"') and cloudDirectory.endswith('"'):
            cloudDirectory = cloudDirectory[1:-1]

    for filename in fileNames:
        filename = os.path.expanduser(filename)
        print('Copying file' + filename + ' to '+cloudDirectory+os.path.basename(filename))
        shutil.copy2(filename, cloudDirectory)
except shutil.Error:
    print('Error while copying files.')



#TODO Match md5 sums of the file, if same do nothing, if different, append date in the filename.
