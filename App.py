from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def obtener_noticias(api_key, tema):
    url = f'https://newsapi.org/v2/everything?q={tema}&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        noticias = response.json()
        return noticias['articles']
    else:
        print("Error al obtener noticias:", response.status_code)
        return None

@app.route('/', methods=['GET', 'POST'])
def mostrar_noticias():
    if request.method == 'POST':
        tema = request.form['tema']
    else:
        tema = 'Tecnología'  # Tema predeterminado
    
    api_key = '6f9b8f19677647ea9046d2cf4006cbbb'
    noticias = obtener_noticias(api_key, tema)
    return render_template('noticias.html', noticias=noticias)

if __name__ == '__main__':
    app.run(debug=True)