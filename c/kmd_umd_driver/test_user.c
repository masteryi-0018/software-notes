#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main() {
    int fd = open("/dev/mychardev", O_RDWR);
    if (fd < 0) {
        perror("open");
        return 1;
    }

    char buffer[256];
    read(fd, buffer, sizeof(buffer));
    printf("Read from driver: %s\n", buffer);

    const char *msg = "Hi kernel, I'm user!\n";
    write(fd, msg, strlen(msg));

    close(fd);
    return 0;
}
