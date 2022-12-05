from flask import Flask, render_template


app = Flask(__name__, template_folder='templates',static_folder="templates/static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/helloworld')
def hello_world():
    return 'Hello, World! sldf;dlf;sdfsdlf;sdlf;sdlf;sd'

@app.route('/form')
def html_form():
  return """
  <form method="post">
  <label for="voornaam">Voornaam:</label>
  <input type="text" name="voornaam" autofocus><br><br>
  <label for="familienaam">Familienaam:</label>
  <input type="text" name="familienaam"><br><br>
  <button type="submit">Submit</button>
  </form>
  """

if __name__ == '__main__':
 app.run()
