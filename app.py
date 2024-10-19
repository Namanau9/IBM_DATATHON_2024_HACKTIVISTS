from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Route: Home Page (User Input Form)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        gender = request.form['gender']
        age = request.form['age']
        marital_status = request.form['marital_status']
        depression = request.form['depression']
        anxiety = request.form['anxiety']
        panic_attack = request.form['panic_attack']
        seek_specialist = request.form['seek_specialist']

        # Insert user input into the database
        with sqlite3.connect('mental_health.db') as conn:
            cur = conn.cursor()
            cur.execute('''
                INSERT INTO mental_health (gender, age, marital_status, depression, anxiety, panic_attack, seek_specialist)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (gender, age, marital_status, depression, anxiety, panic_attack, seek_specialist))
            conn.commit()

        return redirect(url_for('dashboard'))

    return render_template('index.html')

# Route: Dashboard to View All User Entries
@app.route('/dashboard')
def dashboard():
    with sqlite3.connect('mental_health.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM mental_health")
        data = cur.fetchall()

    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=8085)
