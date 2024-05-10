#!/usr/bin/python3
import sys

# Iterate through the command line arguments starting from index 1 (skipping the script name)
for i in range(1, len(sys.argv)):
    print(sys.argv[i])
