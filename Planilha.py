from logging import logMultiprocessing
import gspread
from google.oauth2 import service_account
from Manipula_Lista import Procura_Valor, Filtra

x = Filtra()
 
procura = Procura_Valor()

def planilha_google():
    scopes = ["https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive"]

    json_file = "key.json"
    credentials = service_account.Credentials.from_service_account_file(json_file)
    scoped_credentials = credentials.with_scopes(scopes)
    gc = gspread.authorize(scoped_credentials)
    panilha = gc.open("Resistores")
    aba = panilha.worksheet("Resistor")
    col = aba.col_values(1)
    row = aba.row_values(1)
    lista_planilha = aba.get_all_values()
    del lista_planilha[0]

    return lista_planilha

