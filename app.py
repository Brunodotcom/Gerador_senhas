from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def gerador_senha(comprimento):
    caracteres = string.digits + string.ascii_letters + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha


@app.route('/', methods=["GET", "POST"])
def home():
    senha = None
    erro = None
    enviado = False
    if request.method == 'POST':
        try:
            entrada = int(request.form['INPUT'])
            senha = gerador_senha(entrada)
            enviado = True
        except ValueError:
            erro = "Insira apenas números"
        
    return render_template('index.html', enviado=enviado, erro=erro, senha=senha)

app.run(debug=True)