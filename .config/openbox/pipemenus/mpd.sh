#! /bin/bash
 
# MPD/MPC by olshrimpeyes
nowplaying=`mpc -f "%track%. %artist% - %title%" | sed -n '1p'`
playing=`mpc | grep playing `
nowstatus=`mpc | sed -n '2p' | cut -d ' ' -f1`
 
echo "<openbox_pipe_menu>"



# 		<menu icon="/home/derek/.config/openbox/circle-filled.png" id="root-menu-151830" label="Places">
# 			<item icon="/home/derek/.config/openbox/square-open.png" label="Home">
# 				<action name="Execute">
# 					<execute>pcmanfm -n ~/</execute>
#				</action>
# 			</item>
# 		</menu>


if  [[ -z $nowplaying ]]
 
then
 
echo "<item label=\"Not Playing\"><action name=\"Execute\"><execute>mpc</execute></action></item>"
 
else
 
echo "<menu icon=\"/home/derek/.config/openbox/circle-filled.png\" id=\"root-menu-325671\" label=\""$nowstatus"\">"
echo "<item label=\""$nowplaying"\"><action name=\"Execute\"><execute>mpc</execute></action></item>"
echo "<item label=\""$playing"\"><action name=\"Execute\"><execute>mpc</execute></action></item>"
echo "<separator/>"
echo "<item label=\"Open Music Player\"><action name=\"Execute\"><execute>urxvt -e ncmpcpp</execute></action></item>"
echo "</menu>"

# if [[ -z $playing ]]
 
# then
 
# echo "<item label=\"Paused\"><action name=\"Execute\"><execute>mpc</execute></action></item>"
 
# else
 
# echo "<item label=\""$playing"\"><action name=\"Execute\"><execute>mpc</execute></action></item>"
 
# fi
 
fi
 
echo "<separator/>"
 
if [[ -z $playing ]]
 
then
 
echo "<item label=\"Play\"><action name=\"Execute\"><execute>mpc play</execute></action></item>"
 
else
 
echo "<item label=\"Pause\"><action name=\"Execute\"><execute>mpc pause</execute></action></item>"
echo "<item label=\"Stop\"><action name=\"Execute\"><execute>mpc stop</execute></action></item>"
 
fi
 
echo "<item label=\"Next\"><action name=\"Execute\"><execute>mpc next</execute></action></item>"
echo "<item label=\"Previous\"><action name=\"Execute\"><execute>mpc prev</execute></action></item>"
echo "<item label=\"Volume\"><action name=\"Execute\"><execute>urxvt -e alsamixer</execute></action></item>"
echo "</openbox_pipe_menu>"
