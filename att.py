import flet as ft
import pandas as pd
from conect import conectar
import tkinter as tk
from tkinter import filedialog

file_path = None

def main(page: ft.Page):
    page.window_center()
    page.title = 'Atualização de Markup'
    page.window_width = 500
    page.window_height = 300
    page.window_resizable = False
    page.padding = 100
    page.theme_mode = 'dark'
    page.window_center()


    feedback_msg = ft.Text(value="Nenhum arquivo selecionado!", color=ft.colors.WHITE)
    
    def selecionar_arquivo(event=None):
        page.window_visible = False
        page.update()
        root = tk.Tk()
        root.withdraw()
        global file_path
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            print(file_path)
        root.destroy()
        page.window_visible = True
        feedback_msg.value = "Arquivo selecionado!"
        page.update()

    def atualizar_dados(caminho_arquivo_excel):
        if not file_path:
            feedback_msg.value = "Nenhum arquivo selecionado!"
            page.update()
            return

        # faz conexão
        conn = conectar()

        # teste para verificar se conectou corretamente
        if conn is None:
            page.splash = ft.ProgressBar()
            page.update()
            feedback_msg.value = "Erro ao atualizar."
            page.splash = None
            page.update()
            return

        # Cria um cursor para o banco
        cursor = conn.cursor()

        # importa dados da planilha
        dados_excel = pd.read_excel(file_path)

        # Loop pelos dados
        for indice, linha in dados_excel.iterrows():
            page.splash = ft.ProgressBar()
            submit_btn.enabled = False
            page.update()
            chave_primaria = linha['CODPROD']
            chave_secundaria = str(linha['AD_PERCMARKUP']).replace(',', '.')
            query_update = f"UPDATE PCPRODUT SET AD_PERCMARKUP = '{chave_secundaria}' WHERE CODPROD = '{chave_primaria}'"
            cursor.execute(query_update)
            feedback_msg.value = "Atualizações efetuadas!"
            page.splash = None
            submit_btn.enabled = True
            page.update()

        conn.commit()

        # fecha o cursor
        cursor.close()

        # fecha a conexão
        conn.close()

    # Componentes da tela
    btn_selecionar_arquivo = ft.ElevatedButton(text='Selecionar arquivo Excel', width=1000, on_click=selecionar_arquivo)
    submit_btn = ft.ElevatedButton(text='Atualizar', width=600, on_click=atualizar_dados)
    

    # configura os botões na tela
    page.add(btn_selecionar_arquivo, submit_btn, feedback_msg)

# Inicia a tela
ft.app(target=main)
