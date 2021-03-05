#!/usr/bin/env python3
#
# GMUISCBROWSER by Derek Taylor (DistroTube)
# A simple script that creates an openbox pipemenu that controls gmusicbrowser.
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
#       <menu execute="/PATH/TO/gmusicbrowser.sh" id="gmusicbrowser" label="gmusicbrowser"/>
# Be sure to change the PATH/TO to the correct path to this file.
#
# Reconfigure openbox.
#
# REQUIRES the gmusicbrowser music player to be installed on your computer.

# The playlist submenu is designed to pull all .m3u files from the ~home/$USER/.config/gmusicbrowser/ directory.
# Therefore, you must create this folder and export your playlists to this folder.
# To enable song information to display, you must enable the NOW PLAYHING plugin in gmusicbrowser.
# Add this to "command for when playing song changed": tee /home/$USER/.config/gmusicbrowser/nowplaying.info
# Change $USER to your actual username. Tick the checkbox for send title/artist/album in standard input.
# You also should go to Preferences > Misc. and tick the checkbox for remember playing position between sessions.
# This allows gmusicbrowser to remember the song it was playing within the playlist upon exit.

# SETTING

import subprocess
import os

playlistDir = '/home/derek/.config/gmusicbrowser/'

cmd1 = "cat /home/derek/.config/gmusicbrowser/*.info | sed -n -e 's/^.*Title=//p' | tr -d '\"'"
process = subprocess.Popen(cmd1, stdout=subprocess.PIPE, shell=True)
songTitle = process.communicate()[0].decode("utf-8").rstrip()

cmd2 = "cat /home/derek/.config/gmusicbrowser/*.info | sed -n -e 's/^.*Artist=//p' | tr -d '\"'"
process = subprocess.Popen(cmd2, stdout=subprocess.PIPE, shell=True)
songArtist = process.communicate()[0].decode("utf-8").rstrip()

cmd3 = "cat /home/derek/.config/gmusicbrowser/*.info | sed -n -e 's/^.*Album=//p' | tr -d '\"'"
process = subprocess.Popen(cmd3, stdout=subprocess.PIPE, shell=True)
songAlbum = process.communicate()[0].decode("utf-8").rstrip()

cmd4 = "cat /home/derek/.config/gmusicbrowser/*.info | sed -n -e 's/^.*Length=//p' | tr -d '\"'"
process = subprocess.Popen(cmd4, stdout=subprocess.PIPE, shell=True)
songLength = process.communicate()[0].decode("utf-8").rstrip()

cmd5 = "cat /home/derek/.config/gmusicbrowser/*.info | sed -n -e 's/^.*Year=//p' | tr -d '\"'"
process = subprocess.Popen(cmd5, stdout=subprocess.PIPE, shell=True)
songYear = process.communicate()[0].decode("utf-8").rstrip()

cmd6 = "cat /home/derek/.config/gmusicbrowser/*.info | sed -n -e 's/^.*Track=//p' | tr -d '\"'"
process = subprocess.Popen(cmd6, stdout=subprocess.PIPE, shell=True)
songTrack = process.communicate()[0].decode("utf-8").rstrip()

cmd7 = "ls -l /home/derek/.config/gmusicbrowser/*m3u | wc -l | sed -n '1p'"
process = subprocess.Popen(cmd7, stdout=subprocess.PIPE, shell=True)
playlistNum = process.communicate()[0].decode("utf-8").rstrip()

# OPENBOX PIPEMENU

print ('<?xml version=\"1.0\" encoding=\"UTF-8\"?>')
print ('<openbox_pipe_menu>')
print ('<menu id=\"root-menu-325671\" label=\"Track Info\">')
print ('<item label="'+songTitle+' - '+songArtist+' - '+songAlbum+' ('+songYear+')'+'"><action name=\"Execute\"><execute>gmusicbrowser -cmd PlayPause</execute></action></item>')
print ('<item label="'+'Total Runtime: '+songLength+'"><action name=\"Execute\"><execute>gmusicbrowser -cmd PlayPause</execute></action></item>')
print ('<separator/>')
print ('<item label=\"Open gmusicbrowser\"><action name=\"Execute\"><execute>gmusicbrowser -cmd</execute></action></item>')
print ('</menu>')
print ('<menu id=\"root-menu-325676\" label=\"Playlists ('+playlistNum+')\">')
for filename in os.listdir('/home/derek/.config/gmusicbrowser/'):
	plist = "echo "+filename+" | rev | cut -d\"/\" -f1 | rev"
	process = subprocess.Popen(plist, stdout=subprocess.PIPE, shell=True)
	playlist = process.communicate()[0].decode("utf-8").rstrip()
	if playlist.endswith(".m3u"):
		print ('<item label="'+playlist+'"><action name=\"Execute\"><execute>gmusicbrowser '+playlistDir+filename+'</execute></action></item>')
print ('</menu>')
print ('<separator/>')
print ('<item label=\"Play\"><action name=\"Execute\"><execute>gmusicbrowser -cmd Play</execute></action></item>')
print ('<item label=\"Pause\"><action name=\"Execute\"><execute>gmusicbrowser -cmd Pause</execute></action></item>')
print ('<item label=\"Stop\"><action name=\"Execute\"><execute>gmusicbrowser -cmd Stop</execute></action></item>')
print ('<item label=\"Next\"><action name=\"Execute\"><execute>gmusicbrowser -cmd NextSong</execute></action></item>')
print ('<item label=\"Previous\"><action name=\"Execute\"><execute>gmusicbrowser -cmd PrevSong</execute></action></item>')
print ('<separator/>')
print ('<item label=\"Volume Up\"><action name=\"Execute\"><execute>gmusicbrowser -cmd IncVolume</execute></action></item>')
print ('<item label=\"Volume Down\"><action name=\"Execute\"><execute>gmusicbrowser -cmd DecVolume</execute></action></item>')
print ('<separator/>')
print ('<item label=\"Show/Hide\"><action name=\"Execute\"><execute>gmusicbrowser -cmd ShowHide</execute></action></item>')
print ('<item label=\"Quit\"><action name=\"Execute\"><execute>gmusicbrowser -cmd Quit</execute></action></item>')
print ('</openbox_pipe_menu>')
