from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    operation = request.form['operation']
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    
    if operation == 'add':
        result = num1 + num2
        operation_name = 'ADD'
    elif operation == 'sub':
        result = num1 - num2
        operation_name = 'SUBTRACT'
    elif operation == 'mult':
        result = num1 * num2
        operation_name = 'MULTIPLY'
    elif operation == 'div':
        if num2 == 0:
            return "Error!! Division by zero is INVALID"
        result = num1 / num2
        operation_name = 'DIVIDE'
    else:
        return "Invalid operation"

    return render_template('result.html', operation=operation_name, num1=num1, num2=num2, result=result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
