import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "./app/static/images/upload"
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])

app = Flask(__name__)
app.secret_key = "flash_key"

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        
        if not file:
            flash("ファイルを選択してください")
            return render_template("index.html")
        else:
            if not allowed_file(file.filename):
                flash("拡張子はpng, jpg, jpegのみ使用可能です")
                return render_template("index.html")
            else:
                filename = secure_filename(file.filename)
                file_path = os.path.join(UPLOAD_FOLDER, filename)
                file.save(file_path)
                return render_template("display_img.html", file_path=file_path)
    else:
        return render_template("index.html")
        

