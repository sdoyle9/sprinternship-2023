from flask import Flask, render_template

app = Flask(__name__)
app.template_folder = 'templates'

@app.route("/")
def home():
    return render_template('home_page.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/map")
def map_page():  # Renamed function here
    return render_template('map.html')

@app.route("/savepage")
def savepage():
    return render_template('savepage.html')

if __name__ == '__main__':
    print("Loading configuration....")
    # Here, you can add code to actually load a configuration if you need to.
    print("Done loading configuration")
    app.run(debug = False)
    # app.run(debug=True)
