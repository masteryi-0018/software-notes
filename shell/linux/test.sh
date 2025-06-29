# 1. 创建镜像
dd if=/dev/zero of=hd.img bs=1M count=64

# 2. 建立分区表
# 方法1，parted，MBR传统分区
parted -s hd.img mklabel msdos
parted -s hd.img mkpart primary ext4 1MiB 100%
parted -s hd.img set 1 boot on

# 方法2，gdisk，感觉略麻烦，可以参考：<https://www.bilibili.com/video/BV1bFNSeREvV/>


# 3. 格式化为ext4
sudo losetup -Pf --show hd.img
sudo mkfs.ext4 /dev/loop0p1

# 4. 安装引导程序
# 不想污染本身的/mnt
mkdir mnt
sudo mount /dev/loop0p1 mnt
sudo apt install grub2-common grub-pc-bin
sudo grub-install --target=i386-pc --boot-directory=mnt/boot /dev/loop0

sudo nano mnt/boot/grub/grub.cfg
# 写入以下内容
# menuentry "Linux" {
#     linux /boot/bzImage root=/dev/sda1 console=ttyS0
#     initrd /boot/initramfs.cpio.gz
# }

# 5. 复制内容
sudo cp linux-6.16-rc2/arch/x86/boot/bzImage mnt/boot
sudo cp initramfs.cpio.gz mnt/boot

# 6. 卸载清理
sudo umount mnt
sudo losetup -d /dev/loop0