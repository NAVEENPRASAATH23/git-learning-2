from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return """
    <h1>Welcome to Docker Training</h1>
    <p>This application is rnning inside a Docker Container.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)