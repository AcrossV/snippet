##### Kernel, see ../kernel/surface_book2_acpi_high_cpu.md
- /boot/vmlinuz-linux-surface-<kernel version>
- /boot/initramfs-linux-surface-<kernel version>.img
- /lib/modules/<kernel version>-surface/
- grub menu entry

##### /etc configuration files, see https://github.com/jakeday/linux-surface/tree/master/root/etc
- /etc/NetworkManager/conf.d/default-wifi-powersave-on-surface-book-2.conf
- /etc/NetworkManager/NetworkManager.conf # Backup to /etc/NetworkManager/NetworkManager.conf.default
- /etc/X11/xorg.conf.d/20-intel_example-surface-book-2.conf
- /etc/mkinitcpio.conf, use the new filename: /etc/mkinitcpio-surface.conf to add the modules from the repo (https://github.com/jakeday/linux-surface/blob/master/root/etc/initramfs-tools/modules) and `sudo mkinitcpio -k 4.18.14-surface -g /boot/initramfs-linux-surface.img -c /etc/mkinitcpio-surface.conf`, `sudo mkinitcpio -k 4.18.14-surface -g /boot/initramfs-linux-surface-fallback.img -c /etc/mkinitcpio-surface.conf -S autodetect` # already backuped to /etc/mkinitcpip.conf.resume before installing, or use the preset instead of the manual two times mkinitcpio: `mkinitcpio -p linux-surface`, see also https://github.com/atupal/snippet/blob/master/arch_and_linux/kernel/surface_book2_acpi_high_cpu.md
- /etc/modprobe.d/ath10k-surface-book-2.conf
- /etc/pulse/daemon.conf # backup to /etc/pulse/daemon.conf.default
- /etc/pulse/default.pa # backup to /etc/pulse/default.pa.default
- /etc/udev/rules.d/98-keyboardscovers-surface-book-2.rules
- /etc/udev/rules.d/99-touchscreens-surface-book-2.rules

##### firmware, see https://github.com/jakeday/linux-surface/tree/master/firmware
> If haven't change the firmware files, no need to backup. To restore the official Arch Linux firmware, remove the changed firmware files then run `pacman -Qo /lib/firmware` and reinstall or upgrade the corresponding packages. It will give warning that the files are missing and then re-add them back.
- IPTS
```shell
mkdir -p /lib/firmware/intel/ipts # new directory
# Googld "archlinux get sku model": https://unix.stackexchange.com/questions/75750/how-can-i-find-the-hardware-model-in-linux
# cat /sys/devices/virtual/dmi/id/product_sku -> Surface_Book_1793
unzip -o /home/atupal/kernel/linux-surface/firmware/ipts_firmware_v101.zip -d /lib/firmware/intel/ipts/
```
- i915
```shell
mkdir -p /lib/firmware/i915 # backup to /lib/firmware/i915.ori
unzip /home/atupal/kernel/linux-surface/firmware/i915_firmware_kbl.zip -d /lib/firmware/i915/
```
- nvidia
```shell
mkdir -p /lib/firmware/nvidia/gp108 # backup to /lib/firmware/nvidia/gp108.ori
unzip -o /home/atupal/kernel/linux-surface/firmware/nvidia_firmware_gp108.zip -d /lib/firmware/nvidia/gp108/
```
- marvell
```shell
mkdir -p /lib/firmware/mrvl/ # backup to /lib/firmware/mrvl.ori
unzip -o /home/atupal/kernel/linux-surface/firmware/mrvl_firmware.zip -d /lib/firmware/mrvl/
```

##### Others
- Hibernate (This with the NetworkManager config files will solve the problem that the wifi doen't work after resume from hibernate, dmesg error: mwifiex_pcie, Status: reset)
```shell
cd /lib/systemd/system-sleep
touch sleep # and paste https://github.com/jakeday/linux-surface/blob/master/root/lib/systemd/system-sleep/sleep
chmod a+x /lib/systemd/system-sleep/sleep
```
My additional workaround for audio device
```
add 'espeak "Welcom, $USERNAME"' to post phase of /lib/systemd/system-sleep/sleep
```
- Audio service after clearn booting or restart(not resume from hibernate, see Hibernate section).
```
# Surface Book 2's audio get nosiy after booting or resuming from hibenating. For clean boot, open any GUI winsow will stop the nosiy.
# But above doesn't work for resuming. For resume, only use the audio device works, so need add following line in sleep
add 'espeak "Welcom, $USERNAME"' to ~/.xinitrc
```
- libwacom
TODO
