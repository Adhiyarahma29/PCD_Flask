import numpy as np
from PIL import Image
import image_processing
import os
from flask import send_from_directory
from flask import Flask, render_template, request, make_response, jsonify
from datetime import datetime
from functools import wraps, update_wrapper
from shutil import copyfile

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    return update_wrapper(no_cache, view)


@app.route("/index")
@app.route("/")
@nocache
def index():
    return render_template("home.html", file_path="img/image_here.jpg")


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route("/upload", methods=["POST"])
@nocache
def upload():
    target = os.path.join(APP_ROOT, "static/img")
    if not os.path.isdir(target):
        os.makedirs(target, exist_ok=True)
    file = request.files['file']
    if file:
        destination = os.path.join(target, "img_now.jpg")  # Selalu gunakan nama yang sama
        file.save(destination)
        return jsonify(success=True, file_path="img/img_now.jpg")  # Kembalikan path gambar yang diunggah
    return jsonify(success=False, message="No file uploaded")


@app.route("/normal", methods=["POST"])
@nocache
def normal():
    try:
        # Copy the current image to after.jpg to display as the "normal" image
        copyfile(os.path.join(APP_ROOT, "static/img/img_now.jpg"), os.path.join(APP_ROOT, "static/img/after.jpg"))
        return jsonify(success=True, file_path="img/after.jpg")
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500



@app.route("/grayscale", methods=["POST"])
@nocache
def grayscale():
    try:
        image_processing.grayscale()
        return jsonify(success=True, file_path="img/after.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route("/zoomin", methods=["POST"])
@nocache
def zoomin():
    try:
        image_processing.zoomin()
        return jsonify(success=True, file_path="img/after.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route("/zoomout", methods=["POST"])
@nocache
def zoomout():
    try:
        image_processing.zoomout()
        return jsonify(success=True, file_path="img/after.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500


@app.route("/move_left", methods=["POST"])
@nocache
def move_left():
    try:
        image_processing.move_left()
        return jsonify(success=True, file_path="img/after.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500


@app.route("/move_right", methods=["POST"])
@nocache
def move_right():
    try:
        image_processing.move_right()
        return jsonify(success=True, file_path="img/after.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route("/move_up", methods=["POST"])
@nocache
def move_up():
    try:
        image_processing.move_up()
        return jsonify(success=True, file_path="img/after.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500
   
@app.route("/move_down", methods=["POST"])
@nocache
def move_down():
    try:
        image_processing.move_down()
        return jsonify(success=True, file_path="img/after.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route("/brightness_addition", methods=["POST"])
@nocache
def brightness_addition():
    try:
        image_processing.brightness_addition()
        return jsonify(success=True, file_path="img/after.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route("/brightness_substraction", methods=["POST"])
@nocache
def brightness_substraction():
    try:
        image_processing.brightness_substraction()
        return jsonify(success=True, file_path="img/after.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route("/brightness_multiplication", methods=["POST"])
@nocache
def brightness_multiplication():
    try:
        image_processing.brightness_multiplication()
        return jsonify(success=True, file_path="img/after.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route("/brightness_division", methods=["POST"])
@nocache
def brightness_division():
    try:
        image_processing.brightness_division()
        return jsonify(success=True, file_path="img/after.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route("/histogram_equalizer", methods=["POST"])
@nocache
def histogram_equalizer():
    try:
        image_processing.histogram_equalizer()
        return jsonify(success=True, file_path="img/after.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route("/edge_detection", methods=["POST"])
@nocache
def edge_detection():
    try:
        image_processing.edge_detection()
        return jsonify(success=True, file_path="img/after.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route("/blur", methods=["POST"])
@nocache
def blur():
    try:
        image_processing.blur()
        return jsonify(success=True, file_path="img/after.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route("/sharpening", methods=["POST"])
@nocache
def sharpening():
    try:
        image_processing.sharpening()
        return jsonify(success=True, file_path="img/after.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route("/histogram_rgb", methods=["POST"])
@nocache
def histogram_rgb():
    image_processing.histogram_rgb()
    if image_processing.is_grey_scale("static/img/img_now.jpg"):
        return render_template("histogram.html", file_paths=["img/grey_histogram.jpg"])
    else:
        return render_template("histogram.html", file_paths=["img/red_histogram.jpg", "img/green_histogram.jpg", "img/blue_histogram.jpg"])


@app.route("/thresholding", methods=["POST"])
@nocache
def thresholding():
    lower_thres = int(request.form['lower_thres'])
    upper_thres = int(request.form['upper_thres'])
    try:
        image_processing.threshold(lower_thres, upper_thres)
        return jsonify(success=True, file_path="img/after.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
