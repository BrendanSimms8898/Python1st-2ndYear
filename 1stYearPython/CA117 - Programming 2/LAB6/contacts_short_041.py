#!/usr/bin/env python 

import sys 

with open("contacts_short_041", "r") as f:
	line = f.readlines()
	line = line.split().strip()