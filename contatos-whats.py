"""
AUTOMAÇÃO DE TAREFAS

Passo-a-passo do projeto

Passo 1: Copiar número do contato na planilha;
  Passo 2: Colar número de contato na página do WhatsApp;
  Passo 3: Apertar na caixa para selecionar o contato;
  Passo 4: Apertar no X para recomeçar o processo.
"""
# biblioteca pyautogui controla o mouse, o teclado e o monitor para a programação.

import pandas as pd  # pip install pandas numpy openpyxl
import pyautogui  # pip install pyautogui
import time

# pyautogui.click: clicar com o mouse
# pyautogui.write: escrever um texto
# pyautogui.press: apertar uma tecla do teclado
# pyautogui.hotkey: atralho para comandos no teclado
# pyautogui.hotkey("control","v"): para apertar dois botões

# PASSO 1
pyautogui.PAUSE = 0.6  # Pausa entre cada comando executado.
# 1: Copiar número do contato na planilha;
# 2: Importar a base da dados de produtos.
# biblioteca pandas permite importar tabela de banco de dados.
tabela = pd.read_excel("grupowhats.xlsx")

for linha in tabela.index:  # index são as linhas da tabela.
    pyautogui.click(x=552, y=196)
    # codigo = tabela.loc[linha,"nome_da_coluna"]
    pyautogui.write(str(tabela.loc[linha, "phone"]))
    pyautogui.press("enter")
    pyautogui.press("backspace")
