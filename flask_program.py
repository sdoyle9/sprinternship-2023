from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

print("Loading configuration....")
# Here, you can add code to actually load a configuration if you need to.
print("Done loading configuration")

if __name__ == '__main__':
    app.run()
