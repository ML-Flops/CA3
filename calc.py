from flask import Flask, request

app = Flask(__name__)

from calculator import Subtract,Multiply,Add,Div

@app.route('/calc/<operation>/<int:num1>/<int:num2>')
def calculate(operation, num1, num2):
    if operation == 'add':
        result = Add(num1, num2)
    elif operation == 'subtract':
        result = Subtract(num1, num2)
    elif operation == 'multiply':
        result = Multiply(num1, num2)
    elif operation == 'divide':
        result = Div(num1, num2)
    
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
