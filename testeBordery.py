import subprocess
import os

# Definindo as credenciais e o caminho da rede
remote_path = r'\\seniormdw\Senior_ERP\Bancos\Brasil\Processados'
username = 'Administrador'
password = 'REMOVED_FOR_GITHUB'
local_drive = 'Q:'  # Letra da unidade que você deseja mapear

# Comando para desconectar todas as conexões de rede
disconnect_all_command = 'net use /delete * /y'

# Comando para mapear a unidade de rede
map_command = f'net use {local_drive} {remote_path} /user:{username} {password}'

try:
    # Forçar a desconexão de todas as conexões de rede
    subprocess.check_call(disconnect_all_command, shell=True)
    print('Todas as conexões de rede anteriores foram desconectadas.')

    # Conectar à unidade de rede
    subprocess.check_call(map_command, shell=True)
    print(f'Conectado ao {remote_path}')
    
    # Aqui você pode adicionar o código para acessar arquivos/diretórios
    # Exemplo: Listar arquivos no diretório mapeado
    for root, dirs, files in os.walk(local_drive):
        for file in files:
            print(os.path.join(root, file))

    # Comando para desconectar a unidade de rede
    unmap_command = f'net use {local_drive} /delete'
    subprocess.check_call(unmap_command, shell=True)
    print(f'Desconectado de {remote_path}')
except subprocess.CalledProcessError as e:
    print(f'Erro ao conectar ou desconectar: {e}')