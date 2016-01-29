__author__ = 'frikonja'


from bottle import route, run

@route('/')
def index():
    return "<h1> Don't let the bluebottles touch you!!</h1>"

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
