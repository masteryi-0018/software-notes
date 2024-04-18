## 环境

> sql是语言，依赖于具体的数据库，这里以MySQL为例
> 
> 下载地址：<https://dev.mysql.com/downloads/installer/>
> 
> 是我见过比git安装还要麻烦的东西

SQL是一种语言，需要借助特定环境，例如mysql等

## 命令

mysql实际上像另一个机器一样，需要开机之后，使用用户名与密码登录。所以实际上的语言都是在这个“机器”里面运行的。

要在命令行中执行上述SQL命令，你可以在连接到MySQL后，逐条输入这些命令，或者在外部文本编辑器中编写一个包含所有命令的SQL脚本文件（例如script.sql），然后在MySQL命令行中使用命令执行该脚本。也可以在启动数据库时就执行sql文件。

MySQL 可应用于多种语言，包括 PERL, C, C++, JAVA 和 PHP，在这些语言中，MySQL 在 PHP 的 web 开发中是应用最广泛。

```sh
# 进入mysql
mysql -u root -p

# 在mysql中执行外部的sql文件
source D:\project\language_test\sql\test.sql

# 退出
exit

# 启动时指定数据库与sql文件
mysql -u root -p testdb < path/to/your/script.sql
```


## 密码

- root：经典
- （user）gaoyi：123456


## 启动

上面说过，mysql就像一台机器一样，所以需要手动启动。在安装时如果没选择“开机时自动启动”，那之后就需要手动启动一下mysql，才能连接。