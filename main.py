import flask
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def zag():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def prom():
    return '<br>'.join(['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                        'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!'])


@app.route('/image_mars')
def image():
    return f'''<h1>Жди нас, Марс</h1>
<img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
<h3>Вот как он выглядит!</h3>'''


@app.route('/promotion_image')
def promotion_image():
    promo_spisok = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                    'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/some.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                    <body>           
                <h1>Жди нас, Марс!<h1>
        <img src="{flask.url_for('static', filename='img/mars.jpg')}" alt="здесь должна была быть картинка, 
        но не нашлась">
        <h1>Вот она, красная планета!<h1>''' \
           + '</br>'.join([f"<h1 id=f{index}>{line}</h1>" for index, line in enumerate(promo_spisok)]) + \
           '</body> </html>'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
