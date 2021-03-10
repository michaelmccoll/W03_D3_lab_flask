from flask import render_template

from app import app
from app.models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', orders=orders)

@app.route('/orders/<single_id>')
def single_order(single_id):
    single_id = int(single_id)
    return render_template('order.html', orders=orders, single_id=single_id)