import sys
import os
from cx_Freeze import setup, Executable

# Definir o que deve ser incluído na pasta final
arquivos = ['dados.txt','musicas/']

# Saída de arquivos
confiuracao = Executable(
    script='app.py',
    icon='robots.ico'
)

# Configurar o executável
setup(
    name='Automatizador de login',
    version='1.0',
    description='Este programa automatiza o login deste site',
    author='Isaque Rhudielli',
    options={'biuld_exe':{
        'include_files': arquivos,
        'include_msvcr': True
    }},
    executables=[confiuracao]
)