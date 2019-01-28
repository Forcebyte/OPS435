#!/usr/bin/env python3

import subprocess
import os

def free_space():
        space = subprocess.check_output("df -h | grep '/$' | awk '{print $4}'", shell = True)
        stdout = space.decode('utf-8').strip()
        return stdout

if __name__ == '__main__':
        a = free_space()
        print(a)
