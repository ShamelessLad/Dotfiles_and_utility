#!/bin/sh
#
# Copyright (C) 2009-2013 "isomorph"
# All Rights Reserved.
#
# BSD 3-Clause License
#
# ----
#
# OpenBox "VirtualBox" pipe-menu
# Outputs a menu roughly akin to:
#
#    VirtualBox
#    ----------
#    <Virtual Machine>
#    <Virtual Machine>
#    <Virtual Machine>
#    ...
#
# Usage:
#
# 1. Copy this file somewhere on your path and make it executable
# 2. Add the following line somewhere to your /.config/openbox/menu.xml
#
#    <menu id="vms" label="Virtual Machines" execute="cb-virtual-machines-pipemenu" />
#
# 3. Reconfigure openbox


# make sure virtualbox itself exists
which "virtualbox" > /dev/null
if [ "$?" -ne "0" ]; then
    cat <<EOF
<openbox_pipe_menu>
    <item label="Virtualbox cannot be found"></item>
    <item label="Click here to install Virtualbox">
        <action name="Execute">
            <command>x-www-browser https://www.virtualbox.org/wiki/Linux_Downloads</command>
        </action></item>
</openbox_pipe_menu>
EOF
    exit 1
fi

# output the initial menu
cat <<EOF
<openbox_pipe_menu>
    <item label="VirtualBox">
        <action name="Execute">
            <command>
                 virtualbox -style gtk 
            </command>
        </action>
    </item>
EOF

# Check for the vboxmanage binary
which "vboxmanage" > /dev/null
if [ "$?" -ne "0" ]; then
    echo "</openbox_pipe_menu>"
    exit 0
fi

# seperate the main command from the virtuals
echo "    <separator/>"

# output the list of virtual machines
vboxmanage list vms | cut -f 2 -d "\"" | sort -f | while read vm
do
    cat <<EOF
    <item label="$vm">
        <action name="Execute">
            <command>
                vboxmanage startvm "$vm"
            </command>
        </action>
    </item>
EOF
done;

# and finally...
echo "</openbox_pipe_menu>"
