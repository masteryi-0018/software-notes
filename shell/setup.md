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
```