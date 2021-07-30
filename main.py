from flask import request, redirect
from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/mypage/me', methods=['GET'])
def mypage():
    print("We received GET")
    return render_template("main.html")
# http://127.0.0.1:5000/mypage/me

@app.route ('/mypage/contact', methods=['GET', 'POST'])
def mypage2():
    if request.method == 'GET':
       print("We received GET")
       return render_template("contact.html")
    elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return render_template("contact.html")
#http://127.0.0.1:5000/mypage/contact

if __name__ == "__main__":
    app.run()
