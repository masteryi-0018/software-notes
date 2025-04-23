section .data
    hello db 'Hello, World!', 0xA  ; 字符串加上换行符
    len equ $ - hello              ; 计算字符串长度

section .text
    global _start

_start:
    ; 系统调用号: write (4)
    mov eax, 4          ; sys_write
    mov ebx, 1          ; 文件描述符: stdout
    mov ecx, hello      ; 字符串地址
    mov edx, len        ; 字符串长度
    int 0x80            ; 调用内核

    ; 系统调用号: exit (1)
    mov eax, 1          ; sys_exit
    mov ebx, 0          ; 退出状态码 0
    int 0x80            ; 调用内核