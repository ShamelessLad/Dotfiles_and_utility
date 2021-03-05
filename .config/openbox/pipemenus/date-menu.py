#!/usr/bin/env python3
#
# DATE-MENU by Derek Taylor (DistroTube)
# A simple python script that creates an openbox pipemenu that displays time and date.

# This program is free software: you can redistribute it and/or modify it under the terms of
# the GNU General Public License version 3 as published by the Free Software Foundation.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without 
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see: http://www.gnu.org/licenses

# Copy this file somewhere on your path and make it executable.
# Add the following line somewhere to your /.config/openbox/menu.xml
#       <menu execute="/PATH/TO/date-menu.py" id="datetime" label="Time and Date"/>
# Be sure to change the PATH/TO to the correct path to this file.
# Reconfigure openbox.

# SETTINGS
 
import datetime

dt = datetime.datetime.now()
theDate = dt.strftime('%A, %B %d, %Y')
theTime = dt.strftime('%I:%M %p %Z')
theDay = dt.strftime('%j')
theWeek = dt.strftime('%U')

# OPENBOX PIPEMENU

print ('<?xml version=\"1.0\" encoding=\"UTF-8\"?>')
print ('<openbox_pipe_menu>')
print ('<separator />')
print ('<item label="DATE AND TIME" />')
print ('<separator />')
print ('<item label="'+theTime+'"/>')
print ('<item label="'+theDate+'"/>')
print ('<item label="'+'Day '+theDay+'"/>')
print ('<item label="'+'Week '+theWeek+'"/>')
print ('</openbox_pipe_menu>')
