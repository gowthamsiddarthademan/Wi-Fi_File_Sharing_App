from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os

app = Flask(__name__)

# Folder to store uploaded files
UPLOAD_FOLDER = "shared_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        files = request.files.getlist("file")
        for file in files:
            if file.filename:
                file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return redirect(url_for('upload_success'))  # Redirect to success page
    return render_template("upload.html")

@app.route('/upload_success')
def upload_success():
    return render_template('upload_success.html')  # Page showing upload success

@app.route("/download")
def download_list():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template("download.html", files=files)

@app.route("/download/<filename>")
def download_file(filename):
    try:
        return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)
    except FileNotFoundError:
        return "File not found.", 404  # Show 404 if file isn't found

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Start the server on port 5000
