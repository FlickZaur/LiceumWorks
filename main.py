from flask import Flask, url_for

app = Flask(__name__)


@app.route('/choice/<planet_name>')
def form_sample(planet_name='Земля'):
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" 
                            />
                            <title>про планеты</title>
                          </head>
                          <body>
                          <h1> Я думаю, что  {planet_name} -</h1>
                          <h3>Это планета:)</h3>
                          <h2> Она красивая<3 </h2>
                          <h6>тест на зрение)))</h6>
                           <link rel="stylesheet" type="text/css" 
                           href="{url_for('static', filename='css/some.css')}" />
                                        
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
