"""
AUTOMAÇÃO DE TAREFAS

Passo-a-passo do projeto

Passo 1: Entrar no sistema da empresa;
    https://dlp.hashtagtreinamentos.com/python/intensivao/login
  Passo 2: Fazer login;
  Passo 3: Importar a base da dados de produtos;
  Passo 4: Cadastrar um produto;
  Passo 5: Repetir o cadastro para todos os produtos.
"""
# biblioteca pyautogui controla o mouse, o teclado e o monitor para a programação.

import pandas  # pip install pandas numpy openpyxl
import pyautogui  # pip install pyautogui
import time

# pyautogui.click: clicar com o mouse
# pyautogui.write: escrever um texto
# pyautogui.press: apertar uma tecla do teclado
# pyautogui.hotkey: atralho para comandos no teclado
# pyautogui.hotkey("control","v"): para apertar dois botões

# PASSO 1
pyautogui.PAUSE = 0.6  # Pausa entre cada comando executado.
# 1: Abrir o navegador;
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
# 2: Entrar no link;
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
# 3: Esperar o site carregar.
time.sleep(4)

# PASSO 2
# 1: Fazer login.
pyautogui.click(x=1862, y=380)  # button = right/left // clicks = 2
pyautogui.write("lucascsguidi@gmail.com")
pyautogui.press("tab")
pyautogui.write("123@456")
pyautogui.press("tab")
pyautogui.press("enter")
# 2: Esperar o site carregar.
time.sleep(4)

# PASSO 3
# 1: Importar a base da dados de produtos.
# biblioteca pandas permite importar tabela de banco de dados.
tabela = pandas.read_csv("produtos.csv")


# PASSO 5
# 1:Repetir o cadastro para todos os produtos.
for linha in tabela.index:  # index são as linhas da tabela.
    # PASSO 4
    # 1: Cadastrar um produto;
    pyautogui.click(x=1843, y=249)
    # codigo = tabela.loc[linha,"nome_da_coluna"]
    # 2: Preencher os campos;
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # condição para não preencher o OBS com NaN.
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):  # Se OBS não é vazio:
        pyautogui.write(str(obs))

    # 3: Apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("home")  # Scroll para o início da página.
