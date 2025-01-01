import requests
import pandas as pd
import numpy as np
import plotly.graph_objs as go

# Função para coletar dados históricos da Tron (TRX)
def coletar_dados_historicos(symbol, interval='1d', limit=100):
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
    response = requests.get(url)
    data = response.json()
    
    df = pd.DataFrame(data, columns=['open_time', 'open', 'high', 'low', 'close', 'volume', 
                                      'close_time', 'quote_asset_volume', 'number_of_trades', 
                                      'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    df['close'] = df['close'].astype(float)
    df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
    return df[['open_time', 'close']]

# Função para calcular a média móvel
def media_movel(df, period):
    return df['close'].rolling(window=period).mean()

# Função para calcular o Índice de Força Relativa (RSI)
def calcular_rsi(df, period=14):
    delta = df['close'].diff(1)
    ganho = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    perda = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = ganho / perda
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Função para plotar gráficos interativos
def plotar_graficos(df):
    fig = go.Figure()

    # Preço de fechamento
    fig.add_trace(go.Scatter(x=df['open_time'], y=df['close'], mode='lines', name='Preço de Fechamento'))

    # Média Móvel de 20
    media_movel_20 = media_movel(df, 20)
    fig.add_trace(go.Scatter(x=df['open_time'], y=media_movel_20, mode='lines', name='Média Móvel 20'))

    # RSI
    rsi_series = calcular_rsi(df)
    fig.add_trace(go.Scatter(x=df['open_time'], y=rsi_series, mode='lines', name='RSI'))

    # Configurações do gráfico
    fig.update_layout(title='Análise Técnica da Tron (TRX)',
                      xaxis_title='Data',
                      yaxis_title='Preço (USD)')
    fig.show()

# Execução do script
if __name__ == "__main__":
    symbol = 'TRXUSDT'  # Par Tron para o Tether USD
    df = coletar_dados_historicos(symbol)
    plotar_graficos(df)