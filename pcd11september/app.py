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

img_directory = os.path.join(app.static_folder, 'img')

def clear_image_directory():
    for filename in os.listdir(img_directory):
        file_path = os.path.join(img_directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        # Hapus semua gambar di direktori img/ setiap kali halaman di-refresh
        
        
        # Panggil fungsi tampilan (view)
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    return update_wrapper(no_cache, view)

clear_image_directory()


@app.route("/index")
@app.route("/")
@nocache
def index():
    clear_image_directory()
    return render_template("home.html", file_path="img/image_now.jpg")


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
        copyfile(os.path.join(APP_ROOT, "static/img/img_now.jpg"), os.path.join(APP_ROOT, "static/img/img_now.jpg"))
        return jsonify(success=True, file_path="img/img_now.jpg")
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
        return jsonify(success=True, file_path="img/image_now.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500
   
@app.route("/move_down", methods=["POST"])
@nocache
def move_down():
    try:
        image_processing.move_down()
        return jsonify(success=True, file_path="img/image_now.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route("/brightness_addition", methods=["POST"])
@nocache
def brightness_addition():
    try:
        image_processing.brightness_addition()
        return jsonify(success=True, file_path="img/image_now.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route("/brightness_substraction", methods=["POST"])
@nocache
def brightness_substraction():
    try:
        image_processing.brightness_substraction()
        return jsonify(success=True, file_path="img/image_now.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route("/brightness_multiplication", methods=["POST"])
@nocache
def brightness_multiplication():
    try:
        image_processing.brightness_multiplication()
        return jsonify(success=True, file_path="img/image_now.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route("/brightness_division", methods=["POST"])
@nocache
def brightness_division():
    try:
        image_processing.brightness_division()
        return jsonify(success=True, file_path="img/image_now.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

@app.route("/histogram_equalizer", methods=["POST"])
@nocache
def histogram_equalizer():
    try:
        image_processing.histogram_equalizer()
        return jsonify(success=True, file_path="img/image_now.jpg")  # Mengembalikan JSON yang benar
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
    image_processing.threshold(lower_thres, upper_thres)
    return render_template("home.html", file_paths=["img/img_now.jpg"])  # Mengembalikan JSON yang benar

    

@app.route("/dilasi", methods=["POST"])
@nocache
def dilasi():
    try:
        image_processing.dilasi()
        return jsonify(success=True, file_path="img/img_now.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500
    

@app.route("/erosi", methods=["POST"])
@nocache
def erosi():
    try:
        image_processing.erosi()
        return jsonify(success=True, file_path="img/img_now.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500
    
@app.route("/closing", methods=["POST"])
@nocache
def closing():
    try:
        image_processing.closing()
        return jsonify(success=True, file_path="img/img_now.jpg")  # Mengembalikan JSON yang benar
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500


@app.route("/counting", methods=["POST"])
@nocache
def counting():

        # Panggil fungsi untuk menghitung jumlah objek
    jumlah_obj = image_processing.counting()
    return jsonify(success=True,file_path="img/img_now.jpg", jumlah_objek =jumlah_obj)

    
if __name__ == '__main__':

    clear_image_directory()

    app.run(debug=True, host="0.0.0.0")
