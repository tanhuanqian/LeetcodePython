from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/profile')
def profile():
    return 'test profile1'

@app.route('/list')
def list():
    page = request.args.get("page",default=1, type = int)
    return f"your{page}"

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = '80')
