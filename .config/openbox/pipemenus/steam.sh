#!/bin/bash
#
# STEAM by Derek Taylor (DistroTube)
# A simple script that creates an openbox pipemenu that launches Steam games.
# 
# This program is free software: you can redistribute it and/or modify it under the terms of
# the GNU General Public License version 3 as published by the Free Software Foundation.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without 
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see: http://www.gnu.org/licenses
#
# Copy this file somewhere on your path and make it executable.
# Add the following line somewhere to your /.config/openbox/menu.xml
#       <menu execute="/PATH/TO/steam.sh" id="steam" label="Steam"/>
# Be sure to change the PATH/TO to the correct path to this file.
#
# Reconfigure openbox.

STEAMAPPS=~/.steam/steam/steamapps
echo '<openbox_pipe_menu>'
echo '<item icon="/home/derek/.config/openbox/square-open.png" label="Steam"><action name="Execute"><execute>steam</execute></action></item>'
echo '<separator/>'
for file in $(ls $STEAMAPPS/*.acf -1v); do
ID=$(cat "$file" | grep '"appID"' | head -1 | sed -r 's/[^"]*"appID"[^"]*"([^"]*)"/\1/')
NAME=$(cat "$file" | grep '"name"' | head -1 | sed -r 's/[^"]*"name"[^"]*"([^"]*)"/\1/')
echo "<item icon=\"/home/derek/.config/openbox/square-open.png\" label=\"$NAME\"><action name=\"Execute\"><execute>steam steam://run/$ID</execute></action></item>"
done
echo '</openbox_pipe_menu>'
