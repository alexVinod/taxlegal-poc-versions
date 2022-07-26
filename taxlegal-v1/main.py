from flask import Flask, render_template, url_for, request, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        file = request.files['file_upload']
        file.save(f"./upload_files/{secure_filename(file.filename)}")
        print("POST")
        return redirect("/")
    else:
        return render_template('home.html')
    return render_template('home.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == "__main__":
    app.debug = True
    app.run(host= "0.0.0.0", port = 5000)