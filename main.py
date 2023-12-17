from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import requests
from prediction_controller import predict_disease
from datetime import datetime
import os
from PIL import Image

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("form.html")


@app.route('/report', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        fn = f.filename
        fn = fn.replace(' ', '_')
        f.save(os.path.join('./static/', secure_filename(fn)))
        file = Image.open(f'./static/{fn}').convert('RGB')
        result = predict_disease(file)
        return render_template("report.html", result=result, leaf=fn)


if __name__ == "__main__":
    app.run(debug=True)
