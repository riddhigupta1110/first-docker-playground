from flask import Flask, render_template, redirect, url_for, flash, request
from flask_mail import Mail, Message
from controllers.user_controller import user_bp
from models.user_model import create_user_table
from utils.smtp_config import get_smtp_config  # Import SMTP config function

app = Flask(__name__)
app.secret_key = 'my_secret_key_here'  # Required for flashing messages

# Register the Blueprint for user routes
app.register_blueprint(user_bp)

# Load and configure SMTP settings using smtp_config.py
app.config.update(get_smtp_config())

# Initialize Flask-Mail
mail = Mail(app)

# Create the table once before the first request is handled
create_user_table()

# Route to send an email
@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        recipient = request.form['email']
        subject = request.form['subject']
        body = request.form['body']
        
        # Create the message
        msg = Message(
            subject=subject,
            recipients=[recipient],  # List of recipients
            body=body  # Email body
        )
        
        # Send the email
        mail.send(msg)
        print(f'Email sent to {recipient}')
        flash('Email sent successfully!', 'success')
        return redirect(url_for('index'))
    except Exception as e:
        flash(f'Error sending email: {e}', 'danger')
        print(f"Error: {e}")
        return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
