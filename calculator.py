
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Python Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef2f7;
            text-align: center;
            padding: 50px;
        }
        .calculator {
            background: white;
            padding: 30px;
            max-width: 400px;
            margin: auto;
            border-radius: 12px;
            box-shadow: 0 4px 12px #cccccc;
        }
        input, select, button {
            padding: 12px;
            margin: 8px;
            width: 85%;
            box-sizing: border-box;
        }
        button {
            background: #2563eb;
            color: white;
            border: none;
            cursor: pointer;
        }
        .result {
            color: green;
            font-size: 20px;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <h1>Python Calculator</h1>
        <p>Powered by Flask and Docker</p>

        <form method="POST">
            <input type="number" step="any" name="num1"
                   placeholder="First number" required>

            <select name="operation">
                <option value="add">Addition (+)</option>
                <option value="subtract">Subtraction (-)</option>
                <option value="multiply">Multiplication (*)</option>
                <option value="divide">Division (/)</option>
            </select>

            <input type="number" step="any" name="num2"
                   placeholder="Second number" required>

            <button type="submit">Calculate</button>
        </form>

        {% if result is not none %}
            <p class="result">Result: {{ result }}</p>
        {% endif %}

        {% if error %}
            <p style="color:red">{{ error }}</p>
        {% endif %}
    </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                error = "Cannot divide by zero!"
            else:
                result = num1 / num2

    return render_template_string(
        HTML, result=result, error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
