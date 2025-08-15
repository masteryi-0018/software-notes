#include <linux/init.h>
#include <linux/module.h>
#include <linux/fs.h>
#include <linux/uaccess.h>

#define DEVICE_NAME "mychardev"

static int major;
static char message[256] = "Hello from kernel!\n";

static int my_open(struct inode *inode, struct file *file) {
    printk(KERN_INFO "mychardev: device opened\n");
    return 0;
}

static ssize_t my_read(struct file *file, char __user *buf, size_t len, loff_t *offset) {
    return simple_read_from_buffer(buf, len, offset, message, strlen(message));
}

static ssize_t my_write(struct file *file, const char __user *buf, size_t len, loff_t *offset) {
    if (len > sizeof(message) - 1)
        len = sizeof(message) - 1;
    if (copy_from_user(message, buf, len))
        return -EFAULT;
    message[len] = '\0';
    printk(KERN_INFO "mychardev: received: %s\n", message);
    return len;
}

static int my_release(struct inode *inode, struct file *file) {
    printk(KERN_INFO "mychardev: device closed\n");
    return 0;
}

static struct file_operations fops = {
    .owner = THIS_MODULE,
    .open = my_open,
    .read = my_read,
    .write = my_write,
    .release = my_release,
};

static int __init mychardev_init(void) {
    major = register_chrdev(0, DEVICE_NAME, &fops);
    if (major < 0) {
        printk(KERN_ALERT "mychardev: failed to register device\n");
        return major;
    }
    printk(KERN_INFO "mychardev: registered with major number %d\n", major);
    return 0;
}

static void __exit mychardev_exit(void) {
    unregister_chrdev(major, DEVICE_NAME);
    printk(KERN_INFO "mychardev: unregistered\n");
}

module_init(mychardev_init);
module_exit(mychardev_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("你自己");
MODULE_DESCRIPTION("Simple Char Device Driver");
