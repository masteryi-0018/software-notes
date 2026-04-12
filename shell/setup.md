## 新的Windows配置命令

```sh
## 安装wsl
wsl --install --location D:\WSL\Ubuntu

## 安装zsh
sudo apt install zsh
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

## 修改~/.zshrc
plugins=(git zsh-autosuggestions)

git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

## 修改vscode默认shell

## 设置git信息
git config --global user.name "masteryi-0018"
git config --global user.email "1536474741@qq.com"

# 基本环境
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential

## conda
wget https://github.com/conda-forge/miniforge/releases/download/26.1.1-2/Miniforge3-26.1.1-2-Linux-x86_64.sh
bash Miniforge3-26.1.1-2-Linux-x86_64.sh

# 换源
https://github.com/masteryi-0018/DL-notes/tree/main/vpn#%E5%85%B3%E4%BA%8Econda%E5%92%8Cpip
```