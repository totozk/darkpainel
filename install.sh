#!/bin/bash
clear
echo "Instalando dependências..."
pkg update -y && pkg upgrade -y
pkg install python nmap curl figlet toilet ruby -y
gem install lolcat
pip install requests

clear
echo "Iniciando Dark Painel..."
python painel.py

chmod +x install.sh
