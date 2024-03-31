# securing code review task (task 3)
from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Validate input
        if not name or not email or not message:
            return 'Please fill out all fields.', 400

        # Send email
        try:
            server = smtplib.SMTP('smtp.example.com', 587)
            server.starttls()
            server.login('sender@example.com', 'password')
            msg = f'Subject: New Contact Form Submission\n\nName: {name}\nEmail: {email}\nMessage: {message}'
            server.sendmail('sender@example.com', 'recipient@example.com', msg)
            server.quit()
            return 'Message sent successfully!', 200
        except Exception as e:
            return f'An error occurred: {str(e)}', 500

if __name__ == '__main__':
    app.run(debug=True)
