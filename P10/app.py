from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Hello, from!</p>"

@app.route("/j")
def hello_world():
    return f"<p>Hello, from!</p>"

@app.route("/<nama>")
def hello_world(nama):
    return f"<p>Haloo, namaku {nama}</p>"

@app.route("/cekAngka/<int:angka>")
def CekAngka(angka):
    if angka % 2 == 0:
        return f"angka {angka} adalah angka genap"
    else:
        return f"angka {angka} adalah angka ganjil"
        
@app.route("/login/<username>/<password>")
def loginUser(username, password):
    if username == "mori" and password == "123":
        return f"{username} telah terdaftar dan {password} benar"
    else:
        return f"{username} dan {password} anda salah!"
    
# pak dwi
@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    return (username + ":" + password)
    
app.run(debug=True)