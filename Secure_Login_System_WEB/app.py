from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database setup
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    failed_attempts INTEGER DEFAULT 0,
                    lockout_time DATETIME
                )''')
    conn.commit()
    conn.close()

init_db()

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = c.fetchone()

        if user:
            user_id, _, hashed_password, failed_attempts, lockout_time = user

            if lockout_time and datetime.now() < datetime.fromisoformat(lockout_time):
                return 'Account is locked. Try again later.'

            if check_password_hash(hashed_password, password):
                session['user_id'] = user_id
                c.execute('UPDATE users SET failed_attempts = 0, lockout_time = NULL WHERE id = ?', (user_id,))
                conn.commit()
                conn.close()
                return redirect(url_for('dashboard'))
            else:
                failed_attempts += 1
                lockout_time = None
                if failed_attempts >= 3:
                    lockout_time = datetime.now() + timedelta(minutes=5) # Lockout for 5 minutes
                c.execute('UPDATE users SET failed_attempts = ?, lockout_time = ? WHERE id = ?', (failed_attempts, lockout_time, user_id))
                conn.commit()
                conn.close()
                return 'Invalid credentials. Try again.'
        else:
            conn.close()
            return 'User not found.' # if user does not exist

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        try:
            c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return 'Username already exists.' # if username is taken

        conn.close()
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return 'Welcome to your dashboard!' 

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return "An internal error occurred. Please try again later.", 500

if __name__ == '__main__':
    app.run(debug=True)
