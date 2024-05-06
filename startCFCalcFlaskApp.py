from flask import Flask, request, render_template
import pandas as pd
from getFixedCashFlowPV import getFixedCashFlowPV

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('input.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num_years = int(request.form['num_years'])
    pmt_freq = int(request.form['pmt_freq'])
    pmt_amt = float(request.form['pmt_amt'])
    int_rate = float(request.form['int_rate'])
    
    data = getFixedCashFlowPV(num_years, pmt_freq, pmt_amt, int_rate)
    
    return render_template('result.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)

