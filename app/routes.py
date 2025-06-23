from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from . import db
from .models import Ultraman

main = Blueprint('main', __name__)

@main.route('/')
def index():
    ultramen = Ultraman.query.all()
    return render_template('index.html', ultramen=ultramen)

@main.route('/ultraman/<int:id>')
def detail(id):
    ultra = Ultraman.query.get_or_404(id)
    return render_template('detail.html', u=ultra)

@main.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        image_file = request.files['image']
        filename = secure_filename(image_file.filename)
        image_path = os.path.join('app/static/uploads', filename)
        image_file.save(image_path)

        new_ultra = Ultraman(
            name=request.form['name'],
            human_host=request.form['human_host'],
            height=float(request.form['height']),
            weight=float(request.form['weight']),
            description=request.form['description'],
            image=filename
        )
        db.session.add(new_ultra)
        db.session.commit()
        flash('Ultraman added!')
        return redirect(url_for('main.index'))

    return render_template('form.html', action='Add')

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    ultra = Ultraman.query.get_or_404(id)
    if request.method == 'POST':
        ultra.name = request.form['name']
        ultra.human_host = request.form['human_host']
        ultra.height = float(request.form['height'])
        ultra.weight = float(request.form['weight'])
        ultra.description = request.form['description']

        image_file = request.files['image']
        if image_file:
            filename = secure_filename(image_file.filename)
            image_path = os.path.join('app/static/uploads', filename)
            image_file.save(image_path)
            ultra.image = filename

        db.session.commit()
        flash('Ultraman updated!')
        return redirect(url_for('main.index'))

    return render_template('form.html', u=ultra, action='Edit')

@main.route('/delete/<int:id>')
def delete(id):
    ultra = Ultraman.query.get_or_404(id)
    db.session.delete(ultra)
    db.session.commit()
    flash('Ultraman deleted!')
    return redirect(url_for('main.index'))
