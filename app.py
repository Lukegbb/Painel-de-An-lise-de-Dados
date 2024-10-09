from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Função para carregar e processar os dados
def carregar_dados():
    df = pd.read_csv('data/dados.csv')  # Certifique-se de ter um arquivo CSV de exemplo
    return df

# Função para gerar gráfico
def gerar_grafico():
    df = carregar_dados()
    plt.figure(figsize=(10,6))
    plt.bar(df['categoria'], df['valor'], color='lightblue')
    plt.title('Distribuição de Valores por Categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Valor')
    
    # Salvar o gráfico como imagem
    if not os.path.exists('static/images'):
        os.makedirs('static/images')
    plt.savefig('static/images/grafico.png')
    plt.close()

@app.route('/')
def index():
    gerar_grafico()  # Gera o gráfico toda vez que a página é carregada
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
