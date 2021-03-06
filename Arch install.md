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
	# uncomment en_US
	locale-gen
	vim /etc/locale.conf
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
	grub-install /dev/sda
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
	pacman -S lightdm lightdm-webkit2-greeter xorg xorg-xinit openbox obconf rofi openssh xfce4-terminal pcmanfm xarchiver unzip tint2 xcompmgr nitrogen chromium git telegram-desktop code
```
2. Install yaourt
```
	sudo pacman -S --needed base-devel git wget yajl
	cd /tmp
	git clone https://aur.archlinux.org/package-query.git
	cd package-query/
	makepkg -si
	cd ..
	git clone https://aur.archlinux.org/yaourt.git
	cd yaourt/
	makepkg -si
	cd ..
	sudo rm -dR yaourt/ package-query/
```
3. SSH for github
```
	ssh-keygen -t ed25519 -C "muradovgithub@gmail.com"
	eval `ssh-agent -s`
	ssh-add ~/.ssh/id_ed25519
	xclip -sel clip < ~/.ssh/id_ed25519.pub
	# add ssh key to your github account
```
4. Git configuration
```
	git config --global user.name "ShamelessLad"
	git config --global user.email "muradovgithub@gmail.com"
	git config --global core.editor vim
```
5. Dotfiles (mainly .config)
```
	git clone git@github.com:ShamelessLad/Dotfiles_and_utility.git
	cp Dotfiles_and_utility/.config ~/
```
6. Wallpapers
```	
	git clone git@github.com:ShamelessLad/Wallpapers.git 
```
