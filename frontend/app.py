from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-code', methods=['GET'])
def run_code():

    flag = False
    error_message = "Checking modules\n"
    try:
        error_message += "Searching for DeepXDE...\n"
        import deepxde
        error_message += f"DeepXDE found: version {deepxde.__version__}\n"
    except ImportError:
        flag = True
        error_message += "Can't find DeepXDE.\n Please install DeepXDE.\n"
    
    try:
        error_message += "Searching for Pytorch...\n"
        import torch
        error_message += f"Pytorch found : version {(torch.__version__)}\n"
        
    except ImportError:
        flag = True
        error_message += "Can't find Pytorch.\n Please install Pytorch.\n"

    if flag:
        error_message += "Make sure you activate a correct Python environment.\n"
    else:
        error_message += "All modules have been found...\nYou are good to go :)"

    
    return jsonify({'result': error_message})


if __name__ == '__main__':
    app.run(debug=True)
