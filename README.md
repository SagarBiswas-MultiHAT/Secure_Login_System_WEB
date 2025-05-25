# Secure Login System

home.html
![home.html](https://imgur.com/vTlmcrM.png)

login.html
![login.html](https://imgur.com/oOQmOAL.png)

register.html 
![register.html](https://imgur.com/xKvIAcF.png)

404.html 
![404.html ](https://imgur.com/oYzXxMP.png)

Account lockout for 5 minutes
![Account lockout for 5 minutes](https://imgur.com/bOwJYVo.png)

## Overview
This project is a secure login system built using Flask, a lightweight Python web framework. It demonstrates best practices in web authentication, password storage, and brute-force attack prevention.

## Features
- **Password Hashing**: User passwords are securely hashed using `werkzeug.security`.
- **Account Lockout**: Accounts are locked temporarily after multiple failed login attempts to prevent brute-force attacks. (for 5 minutes)
- **Session Management**: Basic session handling to manage user authentication.
- **Custom Error Pages**: User-friendly error pages for 404 and 500 errors.
- **Responsive Design**: Clean and responsive UI for login, registration, and home pages.

## Project Structure
```
app.py                # Main application file
requirements.txt      # Python dependencies
users.db              # SQLite database for user data
static/               # Static files (CSS, images)
    styles.css        # Styling for the application
    pic1.jpg          # Image used in the home page
templates/            # HTML templates
    home.html         # Home page
    login.html        # Login page
    register.html     # Registration page
    404.html          # Custom 404 error page
```

## Setup Instructions
1. Clone the repository or download the project files.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage
- Navigate to the home page to access the login and registration options.
- Register a new account and log in to access the dashboard.
- If you encounter any issues, refer to the error messages displayed on the screen.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite
