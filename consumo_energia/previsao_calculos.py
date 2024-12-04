from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def calcular_previsao_consumo(ano, regiao, arquivo_excel='consumo_geral_v2.xlsx'):
    df = pd.read_excel(arquivo_excel, header=None, names=["Ano", "Mes", "Regiao", "Valor"])
    df_regiao = df[df["Regiao"] == regiao]

    # Agrupar por ano para obter o consumo total anual por região
    df_agrupado = df_regiao.groupby("Ano")["Valor"].sum().reset_index()

    # Regressão linear
    X = df_agrupado["Ano"].values.reshape(-1, 1)
    y = df_agrupado["Valor"].values

    modelo = LinearRegression()
    modelo.fit(X, y)

    # Fazer a previsão para o ano solicitado
    previsao = modelo.predict(np.array([[ano]]))[0]
    return round(previsao, 2)
