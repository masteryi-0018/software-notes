# 1. 下载后解压得到img镜像

xz -d 2025-05-13-raspios-bookworm-armhf-lite.img.xz
fdisk -l 2025-05-13-raspios-bookworm-armhf-lite.img

# 2. 挂载分区

sudo losetup -fP 2025-05-13-raspios-bookworm-armhf-lite.img --show
mkdir mnt/{boot, rootfs}
sudo mount /dev/loop0p1 mnt/boot
sudo mount /dev/loop0p2 mnt/rootfs

# 3. qemu仿真

qemu-system-aarch64.exe -machine raspi4b -kernel mnt/boot/kernel8.img -dtb mnt/boot/bcm2711-rpi-4-b.dtb

# 4. 使用自己的rootfs仿真

dd if=/dev/zero of=rootfs.ext4 bs=1M count=2048
mkfs.ext4 rootfs.ext4
mkdir mnt/tmp_rootfs
sudo mount rootfs.ext4 mnt/tmp_rootfs
sudo cp -a mnt/rootfs/* mnt/tmp_rootfs/
sudo umount mnt/tmp_rootfs

qemu-system-aarch64.exe -machine raspi4b -kernel mnt/boot/kernel8.img -dtb mnt/boot/bcm2711-rpi-4-b.dtb -drive file=rootfs.ext4,format=raw,if=sd # 未知原因报错