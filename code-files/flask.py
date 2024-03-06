from flask import Flask, render_template, request, redirect, url_for
from youtube_to_mp3 import download_youtube_audio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    youtube_url = request.form['youtube_url']
    output_path = './output_folder'
    download_youtube_audio(youtube_url, output_path)
    return redirect(url_for('download'))

@app.route('/download')
def download():
    return render_template('download.html')

if __name__ == '__main__':
    app.run(debug=True)