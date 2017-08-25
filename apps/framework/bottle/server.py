from bottle import route, run, template
# http://bottlepy.org/docs/dev/tutorial.html


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080, server='tornado')
