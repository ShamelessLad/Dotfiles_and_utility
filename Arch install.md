# My guide for fast arch installation
[Donwnload .iso file here](https://archlinux.org/download/)

[Full guide](https://wiki.archlinux.org/index.php/Installation_guide)

---
## Basic Arch Linux install
1. Ping
2. Time and date
```
	timedatectl set-ntp true
```
3. Partitioning
```
	cfdisk
	# dos
	# sda1-Linux Firmware, sda2-Linux Swap(2G)
	mkfs.ext4 /dev/sda1
	mkswap /dev/sda2
	swapon /dev/sda2
	mount /dev/sda1 /mnt
```
4. Edit mirrors
```
	/etc/pacman.d/mirrorlist
```
5. Base packages
```
	pacstrap /mnt base linux linux-firmware
```
6. Fs table
```
	genfstab -U /mnt >> /mnt/etc/fstab
```
7. Chroot
```
	arch-chroot /mnt
	# useful packages:
	pacman -S dhcpcd vim
```
8. Timezone
```
	ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime
	hwclock --systohc
```
9. Localisation
```
	vim /etc/locale.gen 
	# uncomment en_US and ru_RU
	locale-gen
	vim /etc/locale.con 
	# LANG=en_US.UTF-8
```
10. Host
```
	vim /etc/hostname
	vim /etc/hosts		127.0.0.1	localhost
				::1		localhost
				127.0.1.1	&hostname&.localdomain &hostname&
```
11. Root password
```
	passwd
```
12. Sudo
```
	pacman -S sudo
	visudo 
	# uncomment %wheel ALL=(ALL) ALL
```
13. Users and groups
```
	useradd -m &username&
	passwd &username&
	usermod -aG wheel,audio,video,optical,storage &username&
```
14. Bootloader (grub -___-)
```
	pacman -S grub
	grub-install
	grub-mkconfig -o /boot/grub/grub.cfg
```
15. Finish installation
```
	exit chroot
	shutdown now
	# remove .iso
```
---
## After installation
1. Useful packages
```	
	pacman -S lightdm lightdm-webkit2-greeter openbox obconf rofi xfce4-terminal pcmanfm xarchiver tint2 xcompmgr nitrogen chromium
```
2. SSH for github
```
	ssh-keygen -t ed25519 -C "muradovgithub@gmail.com"
	eval `ssh-agent -s`
	ssh-add ~/.ssh/id_ed25519
	clip < ~/.ssh/id_ed25519.pub
	# add ssh key to your github account
```
3. Git configuration
```
	git config --global user.name "ShamelessLad"
	git config --global user.email "muradovgithub@gmail.com"
	git config --global core.editor vim
```
4. Dotfiles (mainly .config)
```
	git clone git@github.com:ShamelessLad/Dotfiles_and_utility.git
	cp /Dotfiles_and_utility/.config ~/
```
5. Wallpapers
```	
	git clone git@github.com:ShamelessLad/Wallpapers.git 
```
