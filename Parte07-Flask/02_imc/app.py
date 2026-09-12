from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/imc', methods=['GET', 'POST'])
def calcular_imc():
    # nome = None
    # peso = None
    # altura = None
    # imc = None
    # result = ""
    # diagnostico = None
    if request.method == 'POST':
        nome = request.form.get('nome', "").title()
        peso = float(request.form.get('peso', 0).replace(',', '.'))
        altura = float(request.form.get('altura', 0).replace(',', '.'))
        imc = peso / (altura ** 2) if altura > 0 else 0
        
        if imc < 18.5:
            diagnostico = " - Abaixo do peso"
        elif 18.5 <= imc < 25:
            diagnostico = " - Peso normal"
        elif 25 <= imc < 30:
            diagnostico = " - Sobrepeso"
        else:
            diagnostico = " - Obesidade"

        result = f"{nome}, seu IMC é: {imc:.2f} {diagnostico}"
        
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)