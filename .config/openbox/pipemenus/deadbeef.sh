#! /bin/bash 
#
# DEADBEEF by Derek Taylor (DistroTube)
# A simple script that creates an openbox pipemenu that controls the deadbeef music player.
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
#       <menu execute="/PATH/TO/deadbeef.sh" id="Music Player" label="Music Player"/>
# Be sure to change the PATH/TO to the correct path to this file.
#
# Reconfigure openbox.
#
# REQUIRES the Deadbeef music player to be installed on your computer.


nowplaying=`deadbeef --nowplaying "%n %a - %t - %b - %y" | sed -n '1p' | tr -d '"'`
tracktime=`deadbeef --nowplaying "%l" | sed -n '1p'`
playlist_num=`ls -l /home/dt/.config/deadbeef/playlists/* | wc -l | sed -n '1p'`

echo "<openbox_pipe_menu>"
echo "<menu id=\"root-menu-325671\" label=\""Track Info"\">"
echo "<item label=\""$nowplaying"\"><action name=\"Execute\"><execute>deadbeef</execute></action></item>"
echo "<item label=\"Total Runtime: "$tracktime"\"><action name=\"Execute\"><execute>deadbeef</execute></action></item>"
echo "<separator/>"
echo "<item label=\"Open Music Player\"><action name=\"Execute\"><execute>deadbeef</execute></action></item>"
echo "</menu>"
echo "<menu id=\"root-menu-325676\" label=\"Playlists ($playlist_num)\">"
for file in $(ls /home/dt/.config/deadbeef/playlists/*.dbpl -1v); do
NAME=$(echo "$file" | rev | cut -d"/" -f1 | rev)
echo "<item label=\"$NAME\"><action name=\"Execute\"><execute>deadbeef $file</execute></action></item>"
done
echo "</menu>"
echo "<separator/>"
echo "<item label=\"Play\"><action name=\"Execute\"><execute>deadbeef --play</execute></action></item>"
echo "<item label=\"Pause\"><action name=\"Execute\"><execute>deadbeef --pause</execute></action></item>"
echo "<item label=\"Stop\"><action name=\"Execute\"><execute>deadbeef --stop</execute></action></item>"
echo "<item label=\"Next\"><action name=\"Execute\"><execute>deadbeef --next</execute></action></item>"
echo "<item label=\"Previous\"><action name=\"Execute\"><execute>deadbeef --prev</execute></action></item>"
echo "<separator/>"
echo "<item label=\"Quit\"><action name=\"Execute\"><execute>deadbeef --quit</execute></action></item>"
echo "</openbox_pipe_menu>"
