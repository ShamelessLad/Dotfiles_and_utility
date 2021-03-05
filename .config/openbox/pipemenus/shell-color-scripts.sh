#! /bin/bash 
#
# SHELL-COLOR-SCRIPTS by Derek Taylor (DistroTube)
# A simple script that creates an openbox pipemenu that runs shell-color-scripts
# (https://github.com/dwt1/shell-color-scripts) in a terminal window.
# 
# shell-color-scripts was forked from Color-Scripts (https://github.com/stark/Color-Scripts)
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
#       <menu execute="/PATH/TO/shell-color-scripts.sh" id="shell-color-scripts" label="Shell Color Scripts"/>
# Be sure to change the PATH/TO to the correct path to this file.
#
# Reconfigure openbox.


# output the initial menu
# NOTE: If you do not use the "termite" terminal program or the "ranger" file manager, edit the <command> below.
cat <<EOF
<openbox_pipe_menu>
    <item label="Color Scripts">
        <action name="Execute">
            <command>
                 termite -e 'ranger ~/color-scripts' 
            </command>
        </action>
    </item>
EOF


# seperate the main command from the virtuals
echo "    <separator/>"

echo "    <menu id=\"color-scripts-01-15\" label=\"01-15\">"
# each color script listed in the menu
for file in $(ls ~/shell-color-scripts/* | head -15); do
NAME=$(echo "$file" | rev | cut -d"/" -f1 | rev)
echo "    <menu id=\"$NAME\" label=\"$NAME\">"
# NOTE: If you do not use the "termite" terminal program, then change "termite" to your preferred terminal (ex. xterm, urxvt, etc.)
echo "<item label=\"Run in terminal\"><action name=\"Execute\"><execute>termite -e '$file' -t '$file'</execute></action></item>"
# NOTE: If you do not use the "vim" text editor, then change "vim" to your preferred editor (ex. nano, geany, etc.)
echo "<item label=\"Edit in vim\"><action name=\"Execute\"><execute>termite -e 'vim $file'</execute></action></item>"
echo "    </menu>"
done
echo "    </menu>"

echo "    <menu id=\"color-scripts-16-30\" label=\"16-30\">"
# each color script listed in the menu
for file in $(ls ~/shell-color-scripts/* | tail -37 | head -15); do
NAME=$(echo "$file" | rev | cut -d"/" -f1 | rev)
echo "    <menu id=\"$NAME\" label=\"$NAME\">"
# NOTE: If you do not use the "termite" terminal program, then change "termite" to your preferred terminal (ex. xterm, urxvt, etc.)
echo "<item label=\"Run in terminal\"><action name=\"Execute\"><execute>termite -e '$file' -t '$file'</execute></action></item>"
# NOTE: If you do not use the "vim" text editor, then change "vim" to your preferred editor (ex. nano, geany, etc.)
echo "<item label=\"Edit in vim\"><action name=\"Execute\"><execute>termite -e 'vim $file'</execute></action></item>"
echo "    </menu>"
done
echo "    </menu>"

echo "    <menu id=\"color-scripts-31-45\" label=\"31-45\">"
# each color script listed in the menu
for file in $(ls ~/shell-color-scripts/* | tail -22 | head -15); do
NAME=$(echo "$file" | rev | cut -d"/" -f1 | rev)
echo "    <menu id=\"$NAME\" label=\"$NAME\">"
# NOTE: If you do not use the "termite" terminal program, then change "termite" to your preferred terminal (ex. xterm, urxvt, etc.)
echo "<item label=\"Run in terminal\"><action name=\"Execute\"><execute>termite -e '$file' -t '$file'</execute></action></item>"
# NOTE: If you do not use the "vim" text editor, then change "vim" to your preferred editor (ex. nano, geany, etc.)
echo "<item label=\"Edit in vim\"><action name=\"Execute\"><execute>termite -e 'vim $file'</execute></action></item>"
echo "    </menu>"
done
echo "    </menu>"

echo "    <menu id=\"color-scripts-46+\" label=\"46+\">"
# each color script listed in the menu
for file in $(ls ~/shell-color-scripts/* | tail -7 | head -15); do
NAME=$(echo "$file" | rev | cut -d"/" -f1 | rev)
echo "    <menu id=\"$NAME\" label=\"$NAME\">"
# NOTE: If you do not use the "termite" terminal program, then change "termite" to your preferred terminal (ex. xterm, urxvt, etc.)
echo "<item label=\"Run in terminal\"><action name=\"Execute\"><execute>termite -e '$file' -t '$file'</execute></action></item>"
# NOTE: If you do not use the "vim" text editor, then change "vim" to your preferred editor (ex. nano, geany, etc.)
echo "<item label=\"Edit in vim\"><action name=\"Execute\"><execute>termite -e 'vim $file'</execute></action></item>"
echo "    </menu>"
done
echo "    </menu>"

# and finally...
echo "</openbox_pipe_menu>"

