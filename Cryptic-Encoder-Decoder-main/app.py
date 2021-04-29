from flask import Flask, render_template, redirect, request
import logic

app = Flask(__name__)

Logic = logic.Crypto()

@app.route('/')
def display():
    return render_template("home.html", reply="Welcome!!!")

@app.route('/error')
def error():
    return render_template("home.html", reply="Error")

@app.route('/encrypt')
def encryptDisplay():
    return render_template("encrypt.html")

@app.route('/decrypt')
def decryptDisplay():
    return render_template("decrypt.html")

@app.route('/submit_for_encrytion', methods = ['POST'])
def encryptMessage():
    if request.method == 'POST':
        message = request.form['message']
        cipherText = Logic.Encryptor(message)
        cipherText = Logic.convertToString(cipherText)
        return render_template("home.html", reply="Success", flag=True, text = cipherText)
    else:
        return redirect('/error')

@app.route('/submit_for_decrytion', methods = ['POST'])
def decryptMessage():
    if request.method == 'POST':
        cipherText = request.form['cipherText']
        cipherText = Logic.ConvertToList(cipherText)
        message = Logic.Decryptor(cipherText)
        return render_template("home.html", reply="Success", flag=False, text = message)
    else:
        return redirect('/error')

if __name__ == '__main__':
    app.run(debug=True)