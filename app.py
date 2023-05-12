from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask!"

@app.route("/map")
def map():
    return render_template('map.html')

if __name__ == '__main__':
    print("Loading configuration....")
    # Here, you can add code to actually load a configuration if you need to.
    print("Done loading configuration")
    app.run(debug=True)

    
#  *------------------------------------------------------------------*   

