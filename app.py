from flask import Flask, render_template, url_for, request, flash
from forms import SimpleMessage
import json
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
teamshook = ''
header = { 
           "Content-Type": "application/json"
}

@app.route("/", methods=['POST','GET'])
@app.route("/simple-message", methods=['POST','GET'])
def simplemessage():
    form = SimpleMessage()
    if request.method == "POST":
        message = request.form['data']         

        payload = {
                "Text": message
        }

        response = requests.post(teamshook, headers=header, data=json.dumps(payload))
        if response.status_code == 200:
            flash('Success!', 'success')
        else:
            flash("Oops! Something went wrong" , 'danger')
    return render_template('simplemessage.html', title='SimpleMessage', form=form)

@app.route("/card-message", methods=['POST','GET'])
def cardmessage():
    return render_template('cardmessage.html', title='CardMessage')

if __name__ == '__main__':
    app.run(debug=True)
