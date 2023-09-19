from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    print("Hello World")
    return "hello world"

@app.route('/calc/<operation>/<int:num1>/<int:num2>')
def calculate(operation, num1, num2):
    if operation == 'add':
        result = num1+num2
    elif operation == 'subtract':
        result = num1-num2
    elif operation == 'multiply':
        result = num1*num2
    elif operation == 'divide':
        result = num1/num2
    
    return str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
