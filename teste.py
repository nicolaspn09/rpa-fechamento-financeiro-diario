import subprocess
import os

# Caminho da pasta
caminho_da_pasta = r"\\seniormdw\Senior_ERP\Bancos\Brasil\Processados"
# Nome de usuário e senha
usuario = "Administrador"
senha = 'REMOVED_FOR_GITHUB'

# Mapeia a unidade de rede com usuário e senha
subprocess.run(['net', 'use', 'Q:', caminho_da_pasta, f'/user:{usuario}', senha])

# Define as variáveis
rodou_ibm_bordero = False
inserir_fila = False

# Verifica se o mapeamento foi bem-sucedido
if os.path.ismount("Q:"):
    # Itera sobre cada arquivo no diretório especificado
    for arquivo in os.listdir("Q:"):
        print(arquivo)
else:
    print("Falha ao mapear a unidade de rede.")