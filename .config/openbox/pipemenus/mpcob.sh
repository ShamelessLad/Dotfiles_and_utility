#!/bin/sh
# mpcob - control mpc in your openbox menu
# 02/03/10 - supulton - vrfeight3@gmail.com
# chmod +x mpcob.sh, and place:
# "<menu id="pipe-mpc-menu" label="music" execute="/path/to/script/mpcob.sh" />"
# somewhere in your menu.

# replace "urxvtc" with your preferred terminal
set_term=`echo urxvt`

# gui mpd preference?
set_player=`echo ncmpcpp`

#set variables
playing=`mpc -f "%track%. %artist% - %title%" | sed -n '1p'`
nowstatus=`mpc | sed -n '2p' | cut -d ' ' -f1`
repeat=`mpc | tail -n 1 | cut -c 15-25`
random=`mpc | tail -n 1 | cut -c 29-39`
single=`mpc | tail -n 1 | cut -c 43-53`
consume=`mpc | tail -n 1 | cut -c 57-`
 
# tell when mpc is stopped

if [ "$nowstatus" != "[Playing]" -a "$nowstatus" != "[Paused]" ]
then
export nowstatus=`echo "[Stopped]"`
fi
if [ "$nowstatus" = "[Stopped]" ]
then
export Playing=`echo Play`
fi
 
# convert reserved XML characters '&', '<', '>', '"' for songs containing characters

if [[ $playing =~ '&' ]]
then
export playing=${playing//\&/\&amp\;}
fi
if [[ $playing =~ '<' ]]
then
export playing=${playing//\</\&lt\;}
fi
if [[ $playing =~ '>' ]]
then
export playing=${playing//\>/\&gt\;}
fi
if [[ $playing =~ '"' ]]
then
export playing=${playing//\"/\&quot\;}
fi
# echo menu
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
echo "<openbox_pipe_menu>"
echo " <menu id=\"mpcob-playing\" label=\"$nowstatus\">"
echo " <item label=\"$playing\"> "
echo " <action name=\"Execute\"><execute>mpc toggle</execute></action>"
echo " </item>"
echo " <separator />"
echo " <item label=\"$set_player\"> "
echo " <action name=\"Execute\"><execute>urxvt -e ncmpcpp</execute></action>"
echo " </item>"
echo " </menu>"
echo " <separator />"
echo " <item label=\"Play/Pause\">"
echo " <action name=\"Execute\"><execute>mpc toggle</execute></action>"
echo " </item>"
echo " <item label=\"Prev\">"
echo " <action name=\"Execute\"><execute>mpc prev</execute></action>"
echo " </item>"
echo " <item label=\"Next\">"
echo " <action name=\"Execute\"><execute>mpc next</execute></action>"
echo " </item>"
echo " <item label=\"Stop\">"
echo " <action name=\"Execute\"><execute>mpc stop</execute></action>"
echo " </item>"
echo " <separator />"
echo " <menu id=\"mpcob-options\" label=\"Options\">"
echo " <item label=\"$random\">"
echo " <action name=\"Execute\"><execute>mpc random</execute></action>"
echo " </item>"
echo " <item label=\"$repeat\">"
echo " <action name=\"Execute\"><execute>mpc repeat</execute></action>"
echo " </item>"
echo " <item label=\"$consume\">"
echo " <action name=\"Execute\"><execute>mpc consume</execute></action>"
echo " </item>"
echo " <item label=\"$single\">"
echo " <action name=\"Execute\"><execute>mpc single</execute></action>"
echo " </item>"
echo " <separator />"
echo " <item label=\"Update\">"
echo " <action name=\"Execute\"><execute>mpc update</execute></action>"
echo " </item>"
echo " </menu>"
echo "</openbox_pipe_menu>"
