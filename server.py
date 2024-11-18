from flask import Flask, render_template
from db import get_user_id_by_uuid

app = Flask(__name__)

@app.route('/')
def home():
    """Route for the home page. Displays a message to go to the bot."""
    return "Please go to the bot and type /create to generate your unique link."

@app.route('/link/<user_uuid>', methods=['GET'])
def link(user_uuid):
    """Route to display the Telegram user ID linked to the given UUID."""
    user_id = get_user_id_by_uuid(user_uuid)
    if user_id:
        return f"Telegram User ID: {user_id[0]}"
    else:
        return "Invalid or unknown UUID.", 404

if __name__ == '__main__':
    app.run(debug=True)
