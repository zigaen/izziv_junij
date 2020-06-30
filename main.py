from flask import Flask, render_template, request, make_response, redirect, url_for


app = Flask(__name__)
# we need 2 helper mappings, from letters to ints and the inverse


@app.route("/", methods=["POST"])
def form():
    L2I = dict(zip("ABCČDEFGHIJKLMNOPQRSŠTUVZŽ", range(26)))
    I2L = dict(zip(range(26), "ABCČDEFGHIJKLMNOPQRSŠTUVZŽ"))
    ciphertext = ""
    key = request.form.get("key")
    paragraph = request.form.get("paragraph")
    for c in paragraph.upper():
        if c.isalpha():
            ciphertext += I2L[(L2I[c] + int(key)) % 26]
        else:
            ciphertext += c
    response = make_response(render_template("index.html", ciphertext=ciphertext))
    return response


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()



