#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 15:00:32 2021

@author: Max Harder
"""

import os

if __name__ == '__main__':
    # code below is only executed when the module is run directly
    myurl = input('URL: ')
    os.system('youtube-dl -x --audio-format "best" --audio-quality 5 '+myurl)
