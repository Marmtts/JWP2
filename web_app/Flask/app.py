from flask import Flask

app = Flask(__name__)

# /: Strona główna, która zwraca "Witaj w mojej aplikacji Flask!"

@app.route("/")
def hello_flask():
    return "<p>Witaj w mojej aplikacji Flask!</p>"

# /about: Strona o tobie, która zwraca informacje o twórcy aplikacji, np. "Zaprogramowano przez [Twoje Imię]."

@app.route('/about')
def hello_name():
   return 'Zaprogramowano przez Damiana!'

# /contact: Strona kontaktowa, zwracająca fikcyjne dane kontaktowe, np. "Email:kontakt@example.com."

@app.route("/contact")
def hello_page():
    return "<p>Email:kontakt@example.com.</p>"

if __name__ == '__main__':
   app.run(debug=True)
