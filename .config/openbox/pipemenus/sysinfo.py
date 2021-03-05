#!/usr/bin/env python3
#
# SYSTEMINFO by Derek Taylor (DistroTube)
# A simple script that creates an openbox pipemenu that displays system information.
# My root partition is on /dev/sda1 and my swap is /dev/sda5.  Edit these is your partitioning is different.
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
#       <menu execute="/PATH/TO/sysinfo.py" id="sysinfo" label="System Info"/>
# Be sure to change the PATH/TO to the correct path to this file.
#
# Reconfigure openbox.
#
# REQUIRES net-tools (for ifconfig) to be installed on your computer.

# SETTINGS
 
import subprocess

# SETTINGS - SYSTEM

syst1 = "whoami"
process = subprocess.Popen(syst1, stdout=subprocess.PIPE, shell=True)
user = process.communicate()[0].decode("utf-8").rstrip()

syst2 = "uname -n"
process = subprocess.Popen(syst2, stdout=subprocess.PIPE, shell=True)
host = process.communicate()[0].decode("utf-8").rstrip()

syst3 = "uname -s"
process = subprocess.Popen(syst3, stdout=subprocess.PIPE, shell=True)
system = process.communicate()[0].decode("utf-8").rstrip()

syst4 = "uname -r"
process = subprocess.Popen(syst4, stdout=subprocess.PIPE, shell=True)
release = process.communicate()[0].decode("utf-8").rstrip()

syst5 = "uname -m"
process = subprocess.Popen(syst5, stdout=subprocess.PIPE, shell=True)
arch = process.communicate()[0].decode("utf-8").rstrip()

syst6 = "uptime | sed 's/.* up //' | sed 's/[0-9]* us.*//' | sed 's/ day, / day /' | sed 's/ days, / days /' | sed 's/:/ hours /' | sed 's/ min//'|  sed 's/,/ min/' | sed 's/  / /'"
process = subprocess.Popen(syst6, stdout=subprocess.PIPE, shell=True)
uptime = process.communicate()[0].decode("utf-8").rstrip()

# SETTINGS - CPU

cpu1 = "cat /proc/cpuinfo | grep 'model name' | sed 's/.*: //' | sed -n '1p'"
process = subprocess.Popen(cpu1, stdout=subprocess.PIPE, shell=True)
CPUmodel = process.communicate()[0].decode("utf-8").rstrip()

cpu2 = "cat /proc/cpuinfo | grep -m 1 'cpu MHz' | sed 's/.*: //'"
process = subprocess.Popen(cpu2, stdout=subprocess.PIPE, shell=True)
CPUfreq = process.communicate()[0].decode("utf-8").rstrip()

cpu3 = "cat /proc/cpuinfo | grep -m 1 'cache size' | sed 's/.*: //'"
process = subprocess.Popen(cpu3, stdout=subprocess.PIPE, shell=True)
CPUcache = process.communicate()[0].decode("utf-8").rstrip()

# SETTINGS - MEM

mem1 = "echo 'scale = 2; ('$(cat /proc/meminfo | grep MemTotal: | awk '{print $2}' | sed 's/k//')' /1024)' | bc"
process = subprocess.Popen(mem1, stdout=subprocess.PIPE, shell=True)
memTotal = process.communicate()[0].decode("utf-8").rstrip()

mem2 = "echo 'scale = 2; ('$(cat /proc/meminfo | grep MemFree: | awk '{print $2}' | sed 's/k//')' /1024) + ('$(cat /proc/meminfo | grep grep -m 1 Cached: | awk '{print $2}' | sed 's/k//')' /1024)' | bc"
process = subprocess.Popen(mem2, stdout=subprocess.PIPE, shell=True)
memFree = process.communicate()[0].decode("utf-8").rstrip()

mem3 = "echo 'scale = 2; ('$(cat /proc/meminfo | grep MemTotal: | awk '{print $2}' | sed 's/k//')' /1024) - (('$(cat /proc/meminfo | grep MemFree: | awk '{print $2}' | sed 's/k//')' /1024) + ('$(cat /proc/meminfo | grep -m 1 Cached: | awk '{print $2}' | sed 's/k//')' /1024))' | bc"
process = subprocess.Popen(mem3, stdout=subprocess.PIPE, shell=True)
memUsed = process.communicate()[0].decode("utf-8").rstrip()

mem4 = "echo 'scale = 2; (('$(cat /proc/meminfo | grep MemTotal: | awk '{print $2}' | sed 's/k//')' /1024) - (('$(cat /proc/meminfo | grep MemFree: | awk '{print $2}' | sed 's/k//')' /1024) + ('$(cat /proc/meminfo | grep -m 1 Cached: | awk '{print $2}' | sed 's/k//')' /1024))) / ('$(cat /proc/meminfo | grep MemTotal: | awk '{print $2}' | sed 's/k//')' /1024) *100' | bc"
process = subprocess.Popen(mem4, stdout=subprocess.PIPE, shell=True)
memUsedPercent = process.communicate()[0].decode("utf-8").rstrip()

# SETTINGS - DISKS

disk1 = "df -HlT | grep /dev/sda1 | sed -r 's/   / /g' | sed -r 's/  / /g' | cut -d ' '  -f 1"
process = subprocess.Popen(disk1, stdout=subprocess.PIPE, shell=True)
rootPart = process.communicate()[0].decode("utf-8").rstrip()

disk2 = "df -HlT | grep /dev/sda1 | sed -r 's/   / /g' | sed -r 's/  / /g' | cut -d ' '  -f 2"
process = subprocess.Popen(disk2, stdout=subprocess.PIPE, shell=True)
fileSys = process.communicate()[0].decode("utf-8").rstrip()

disk3 = "df -HlT | grep /dev/sda1 | sed -r 's/   / /g' | sed -r 's/  / /g' | cut -d ' '  -f 3"
process = subprocess.Popen(disk3, stdout=subprocess.PIPE, shell=True)
diskTotal = process.communicate()[0].decode("utf-8").rstrip()

disk4 = "df -HlT | grep /dev/sda1 | sed -r 's/   / /g' | sed -r 's/  / /g' | cut -d ' '  -f 4"
process = subprocess.Popen(disk4, stdout=subprocess.PIPE, shell=True)
diskUsed = process.communicate()[0].decode("utf-8").rstrip()

disk5 = "df -HlT | grep /dev/sda1 | sed -r 's/   / /g' | sed -r 's/  / /g' | cut -d ' '  -f 5"
process = subprocess.Popen(disk5, stdout=subprocess.PIPE, shell=True)
diskFree = process.communicate()[0].decode("utf-8").rstrip()

# SETTINGS - SWAP

swap1 = "cat /proc/swaps | grep /dev/sda5 | sed -r 's/   / /g' | sed -r 's/  / /g' | cut -d ' '  -f 1"
process = subprocess.Popen(swap1, stdout=subprocess.PIPE, shell=True)
swapPart = process.communicate()[0].decode("utf-8").rstrip()

swap2 = "echo 'scale = 2; ('$(cat /proc/meminfo | grep SwapTotal: | awk '{print $2}' | sed 's/k//')' /1024)' | bc"
process = subprocess.Popen(swap2, stdout=subprocess.PIPE, shell=True)
swapTotal = process.communicate()[0].decode("utf-8").rstrip()

swap3 = "echo 'scale = 2; ('$(cat /proc/meminfo | grep SwapFree: | awk '{print $2}' | sed 's/k//')' /1024)' | bc"
process = subprocess.Popen(swap3, stdout=subprocess.PIPE, shell=True)
swapFree = process.communicate()[0].decode("utf-8").rstrip()

swap4 = "echo 'scale = 2; ('$(cat /proc/meminfo | grep SwapTotal: | awk '{print $2}' | sed 's/k//')' /1024) - ('$(cat /proc/meminfo | grep SwapFree: | awk '{print $2}' | sed 's/k//')' /1024)' | bc"
process = subprocess.Popen(swap4, stdout=subprocess.PIPE, shell=True)
swapUsed = process.communicate()[0].decode("utf-8").rstrip()

swap5 = "echo 'scale = 2; (('$(cat /proc/meminfo | grep SwapTotal: | awk '{print $2}' | sed 's/k//')' /1024) - ('$(cat /proc/meminfo | grep SwapFree: | awk '{print $2}' | sed 's/k//')' /1024)) / ('$(cat /proc/meminfo | grep SwapTotal: | awk '{print $2}' | sed 's/k//')' /1024) *100' | bc"
process = subprocess.Popen(swap5, stdout=subprocess.PIPE, shell=True)
swapUsedPercent = process.communicate()[0].decode("utf-8").rstrip()

# SETTINGS - NET

net1 = "/sbin/ifconfig 'enp3s0' | grep 'inet ' | sed 's/.*inet //' | sed 's/netmask.*//'"
process = subprocess.Popen(net1, stdout=subprocess.PIPE, shell=True)
netIP = process.communicate()[0].decode("utf-8").rstrip()

net2 = "/sbin/ifconfig 'enp3s0' | grep 'RX packets' | sed 's/.*bytes [0-9]* (//'  | sed 's/iB).*)*//' | sed 's/b).*)*//' | sed 's/).*)*//'"
process = subprocess.Popen(net2, stdout=subprocess.PIPE, shell=True)
netDown = process.communicate()[0].decode("utf-8").rstrip()

net3 = "/sbin/ifconfig 'enp3s0' | grep 'TX packets' | sed 's/.*bytes [0-9]* (//'  | sed 's/iB).*)*//' | sed 's/b).*)*//' | sed 's/).*)*//'"
process = subprocess.Popen(net3, stdout=subprocess.PIPE, shell=True)
netUp = process.communicate()[0].decode("utf-8").rstrip()

# OPENBOX PIPEMENU

print ('<?xml version=\"1.0\" encoding=\"UTF-8\"?>')
print ('<openbox_pipe_menu>')
print ('<separator />')
print ('<item label="SYSTEM" />')
print ('<separator />')
print ('<item label="'+'User @ Host: '+user+' @ '+host+'"/>')
print ('<item label="'+'Kernel: '+system+' '+release+' '+arch+'"/>')
print ('<item label="'+'Uptime: '+uptime+'"/>')
print ('<separator />')
print ('<item label="CPU" />')
print ('<separator />')
print ('<item label="'+'CPU: '+CPUmodel+'"/>')
print ('<item label="'+'CPU FREQ: '+CPUfreq+' MHz"/>')
print ('<item label="'+'CPU Cache: '+CPUcache+'"/>')
print ('<separator />')
print ('<item label="MEM" />')
print ('<separator />')
print ('<item label="'+'RAM USED: '+memUsed+' MiB/'+memTotal+' MiB'+' ('+memUsedPercent+'%)'+'"/>')
print ('<separator />')
print ('<item label="DISKS" />')
print ('<separator />')
print ('<item label="'+'Root: '+rootPart+' ('+fileSys+')"/>')
print ('<item label="'+'Swap: '+swapPart+' ('+swapUsed+ ' MiB/'+swapTotal+' MiB)\"/>')
print ('<item label="'+'SSD: '+diskTotal+' ('+diskUsed+ ' USED/'+diskFree+' FREE)\"/>')
print ('<separator />')
print ('<item label="NET" />')
print ('<separator />')
print ('<item label="'+'NET IP: '+netIP+'"/>')
print ('<item label="'+'RX bytes: '+netDown+'"/>')
print ('<item label="'+'TX bytes: '+netUp+'"/>')
print ('</openbox_pipe_menu>')
