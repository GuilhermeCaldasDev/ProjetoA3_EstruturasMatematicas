from flask import Flask, render_template, request
from consumo_calculos import calcular_consumo_por_regiao
from previsao_calculos import calcular_previsao_consumo

app = Flask(__name__)


@app.route('/')
def index():
    # Variáveis padrão quando a página é carregada pela primeira vez
    return render_template('index.html', consumo=None, regiao=None, ano=None)


@app.route('/calcular', methods=['POST'])
def calcular():
    # Capturar dados do formulário
    ano = int(request.form['ano'])
    regiao = request.form['regiao']

    # Chamar a função de cálculo
    consumo = calcular_consumo_por_regiao(ano, regiao)

    # Enviar os resultados para o template
    return render_template('index.html', ano=ano, regiao=regiao, consumo=consumo)


@app.route('/previsao', methods=['GET', 'POST'])
def previsao():
    previsao = None
    regiao = None
    ano = None

    if request.method == 'POST':
        ano = int(request.form['ano'])
        regiao = request.form['regiao']

        # Chamar a função de previsão
        previsao = calcular_previsao_consumo(ano, regiao)

    return render_template('previsao.html', previsao=previsao, regiao=regiao, ano=ano)


if __name__ == '__main__':
    app.run(debug=True)
