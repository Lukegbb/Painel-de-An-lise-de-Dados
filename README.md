# Painel de Análise de Dados - README 

# Descrição:
# Este projeto implementa um Painel de Análise de Dados utilizando Flask no back-end
# e HTML/CSS no front-end. Ele processa e exibe gráficos dinâmicos gerados a partir de arquivos CSV,
# fornecendo uma interface web simples e intuitiva para análise de dados.

# Requisitos:
# - Python 3.x
# - Flask
# - Matplotlib
# - Pandas

# Instruções de Instalação:

echo "Navegando para o diretório do projeto..."
cd painel_analise_dados

echo "Criando ambiente virtual (opcional)..."
python3 -m venv venv

echo "Ativando o ambiente virtual..."
source venv/bin/activate  # Para Windows: venv\Scripts\activate

echo "Instalando dependências..."
pip install -r requirements.txt

# Instruções de Execução:

echo "Iniciando o servidor Flask..."
python app.py

echo "Abra o navegador e acesse o painel em http://127.0.0.1:5000"

# Estrutura do Projeto:
# ├── app.py              # Arquivo principal da aplicação Flask
# ├── templates/          # Arquivos HTML
# │   └── index.html      # Template HTML principal
# ├── static/             # Arquivos de estilo e imagens
# │   ├── style.css       # Arquivo CSS para estilização
# │   └── images/         # Diretório onde os gráficos gerados serão salvos
# ├── data/               # Arquivos de dados CSV
# │   └── dados.csv       # Exemplo de arquivo CSV contendo os dados
# ├── requirements.txt    # Lista de dependências do projeto

# Personalização:
# - Substitua o arquivo 'data/dados.csv' para carregar novos dados no painel.
# - Para alterar a aparência da interface, edite o arquivo 'static/style.css'.
# - Modifique a lógica de gráficos em 'app.py' para alterar a exibição dos dados.

# Tratamento de Erros:
# - Verifique se o arquivo CSV segue a estrutura correta.
# - Certifique-se de que todas as bibliotecas estão instaladas corretamente executando 'pip install -r requirements.txt'.

# Contribuições:
# Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

# Licença:
# Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

echo "Painel de Análise de Dados pronto para uso!"

# -----------------------------------------------
# Data Analysis Dashboard - README 

# Description:
# This project implements a Data Analysis Dashboard using Flask on the back-end
# and HTML/CSS on the front-end. It processes and displays dynamic charts generated
# from CSV files, providing a simple and intuitive web interface for data analysis.

# Requirements:
# - Python 3.x
# - Flask
# - Matplotlib
# - Pandas

# Installation Instructions:

echo "Navigating to the project directory..."
cd data-analysis-dashboard

echo "Creating virtual environment (optional)..."
python3 -m venv venv

echo "Activating the virtual environment..."
source venv/bin/activate  # On Windows: venv\Scripts\activate

echo "Installing dependencies..."
pip install -r requirements.txt

# Running Instructions:

echo "Starting the Flask server..."
python app.py

echo "Open the browser and access the dashboard at http://127.0.0.1:5000"

# Project Structure:
# ├── app.py              # Main Flask application file
# ├── templates/          # HTML files
# │   └── index.html      # Main HTML template
# ├── static/             # Style and image files
# │   ├── style.css       # CSS file for styling
# │   └── images/         # Directory where generated charts are saved
# ├── data/               # CSV data files
# │   └── data.csv        # Example CSV file with data
# ├── requirements.txt    # List of project dependencies

# Customization:
# - Replace the 'data/data.csv' file to load new data into the dashboard.
# - To change the interface appearance, edit the 'static/style.css' file.
# - Modify the chart logic in 'app.py' to change how data is displayed.

# Error Handling:
# - Ensure the CSV file follows the correct structure.
# - Make sure all libraries are installed correctly by running 'pip install -r requirements.txt'.

# Contributions:
# Contributions are welcome! Feel free to open issues or submit pull requests.

# License:
# This project is licensed under the MIT License. See the LICENSE file for more information.

echo "Data Analysis Dashboard ready to use!"
