# # from flask import Flask, send_from_directory
# # import random

# # app = Flask(__name__)

# # # Path for our main Svelte page
# # @app.route("/")
# # def base():
# #     return send_from_directory('client/public', 'index.html')

# # # Path for all the static files (compiled JS/CSS, etc.)
# # @app.route("/<path:path>")
# # def home(path):
# #     return send_from_directory('client/public', path)


# # @app.route("/rand")
# # def hello():
# #     return str(random.randint(0, 100))


# # if __name__ == "__main__":
# #     app.run(debug=True)


# from flask import Flask, render_template, request, redirect, flash, Flask, send_from_directory
# from werkzeug.utils import secure_filename
# from main import getPrediction
# import os

# UPLOAD_FOLDER = 'static/'

# app = Flask(__name__)

# app.secret_key = "secret key"

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/', methods=['GET', 'POST'])
# def base():
#   if request.method == 'POST':
#     if 'file' not in request.files:
#       flash('No file part')
#       return redirect(request.url)
#     file = request.files['file']
#     if file.filename == '':
#       flash('No file selected for uploading')
#       return redirect(request.url)
#     if file:
#       filename = secure_filename(file.filename)
#       file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#       label = getPrediction(filename)
#       flash(label)
#       full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#       flash(full_filename)
#       return redirect('/')

#   return render_template('index.html', messages=flash.get_flashed_messages(with_categories=True))

# @app.route("/<path:path>")
# def home(path):
#     return send_from_directory('../', path)

# if __name__=='__main__':
#     port = int(os.environ.get('PORT', 5174))
#     app.run(host='0.0.0.0', port=port, debug=True)



from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for your Flask app

UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'message': 'No file part'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'message': 'No selected file'}), 400

        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)

            # return massage to client with file name 'FILE_NAME uploaded successfully'
            # YOU CAN FUCK HERE.................
            return jsonify({'message': file.filename + ' uploaded successfully'}), 200


    except Exception as e:
        return jsonify({'message': 'An error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1010)
