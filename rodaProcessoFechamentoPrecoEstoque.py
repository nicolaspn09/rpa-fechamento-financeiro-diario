from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from logExecucaoCodigos import grava_log_execucao_sql
import subprocess
import locale
import cx_Oracle
import time
import smtplib
import apiibm
from datetime import datetime

import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(r"C:\rpa\Python")
from Classes.Postgres.Postgres.ConectaPG import ConectaPG


def envia_preco_estoque(mensagemEmail, assunto):
    pass # Logica de negocio removida por seguranca corporativa



def executa_preco_estoque(data_sql):
    pass # Logica de negocio removida por seguranca corporativa



def valida_data_execucao():
    pass # Logica de negocio removida por seguranca corporativa
