from flask import Flask
from operations import add, sub, mult, div

app = Flask(__name__)
@app.route('/add')
def do_add():
    """Adds the two input a and b parameters"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)

    return str(result)

@app.route('/sub')
def do_sub():
    """Subtracts the two input a and b parameters"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)

    return str(result)

@app.route('/mult')
def do_mult():
    """Multiplies the two input a and b parameters"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)

    return str(result)

@app.route('/div')
def do_div():
    """Divides the two input a and b parameters"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)

    return str(result)
