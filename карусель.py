from flask import Flask, url_for

app = Flask(__name__)


@app.route('/car')
def form_sample():
    return f'''<!doctype html>
                        <html lang="ru">
                          <head>
                           <meta charset="utf-8">
                           <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/Загрузка '
                                                                                                     'файла.css')}"/>
                            <title>результаты отбора</title>
                          </head>
                          <body>
                          <h1> слайдшоу;)</h1>
                          <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="static/img/марс1" class="d-block w-100" alt="первый слайд">
    </div>
    <div class="carousel-item">
      <img src="static/img/марс2" class="d-block w-100" alt="второй слайд">
    </div>
    <div class="carousel-item">
      <img src="static/img/марс3" class="d-block w-100" alt="третий слайд">
    </div>
  </div>
</div>
                          </body>
                        </html>
    
    
    '''


if __name__ == '__main__':
    app.run(port=8585, host='127.0.0.1')
