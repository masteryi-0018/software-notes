## 环境

> 每个linux必定都有shell程序


## 命令

```sh
./test.sh
sh ./test.sh
bash ./test.sh
source ./test.sh

# linux的发行版，sh一般链接了dash，据说比bash更快
```


## 笔记

- source是在当前的shell中执行，其他的是在子shell中执行，所以如果设置环境变量，需要用source
- 还有其他的shell，比如，zsh，tmux，csh，等等