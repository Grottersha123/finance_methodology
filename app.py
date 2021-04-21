
from flask import Flask, render_template

from main import start_script_method_1

app = Flask(__name__)





@app.route('/insert_data')
def insert_data():
    insert,insert_error = start_script_method_1()
    return render_template(r'main.html', insert=insert, insert_error=insert_error)


@app.route('/main')
def hello_world():
    insert,insert_error = [],[]
    return render_template(r'main.html', insert=insert, insert_error=insert_error)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)