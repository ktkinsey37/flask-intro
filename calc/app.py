from flask import Flask
from flask import request
from operations import add
from operations import sub
from operations import mult
from operations import div

# is there a better way to do all these imports?

app = Flask(__name__)

@app.route('/add')
def add_nav():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a, b))

@app.route('/sub')
def sub_nav():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a, b))

@app.route('/mult')
def mult_nav():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a, b))

@app.route('/div')
def div_nav():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a, b))

calc_dict = {'add': add, 'sub': sub, 'mult': mult, 'div': div}
@app.route('/math/<operation>')
def route_calc(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(calc_dict[operation](a, b))
