from bottle import Bottle, template, static_file, run

app = Bottle()

@app.route('/joshua')
def hello():
    return "How about a nice game of chess?"

@app.route('/calculator')
def calculator():
    return template('fluid.tpl', mytitle="calcuator", project_name="molotov")

@app.route('<path:path>')
def server_static(path):
    return static_file(path, root='/Users/datapolitical/molotov')

run(app, host='localhost', port=8080)
