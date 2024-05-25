from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        subj = request.form['subj']
        time = request.form['time']
        if username and subj and time:
            new_user = User(username=username, subj=subj,time=time)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('delete_user.html')