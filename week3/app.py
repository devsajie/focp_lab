from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", title="Home")

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name')
        if not name.strip():
            message = "Please enter a valid name."
        else:
            message = f"Hello, {name}! Welcome to Flask Forms."
        return render_template("greet.html", title="Greeting", message=message)
    return render_template("greet.html", title="Greet Form", message=None)

if __name__ == '__main__':
    app.run(debug=True)
