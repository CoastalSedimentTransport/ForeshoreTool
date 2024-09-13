from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    water_level = int(np.round(float(request.form['water_level'])))

    planning_duration = int(np.round(float(request.form['planning_duration'])))
    
    # Example calculation (you can replace this with your own logic)
    result = water_level * planning_duration
    result_path = r"https://raw.githubusercontent.com/CoastalSedimentTransport/ForeshoreTool/main/Images/example_" + str(water_level)  + "_" + str(planning_duration) + ".jpeg"
    return render_template('index.html', result=result_path)

if __name__ == '__main__':
    app.run(debug=True)