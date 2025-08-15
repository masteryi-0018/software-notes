#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

MODULE_LICENSE("GPL");                // 开源协议声明
MODULE_AUTHOR("你的名字");            // 作者信息
MODULE_DESCRIPTION("A simple Linux driver.");  // 描述
MODULE_VERSION("0.1");                // 版本号

// 模块加载时执行
static int __init hello_init(void) {
    printk(KERN_INFO "Hello, kernel driver loaded!\n");
    return 0;
}

// 模块卸载时执行
static void __exit hello_exit(void) {
    printk(KERN_INFO "Goodbye, kernel driver unloaded.\n");
}

module_init(hello_init);   // 指定加载函数
module_exit(hello_exit);   // 指定卸载函数
