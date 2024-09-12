from flask import Flask, render_template

app = Flask(__name__)

# Define the main page route
@app.route('/')
def home():
    return render_template('index.html')

# Define other routes
@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/map')
def map_page():
    return render_template('map.html')

@app.route('/serverplaces')
def serverplaces():
    return render_template('serverplaces.html')

# Astral Moderation page
@app.route('/astral-moderation')
def astral_moderation():
    return render_template('astral-moderation/astral_moderation.html')

# Terms of Service for Astral Moderation
@app.route('/astral-moderation/terms-of-service')
def terms_of_service():
    return render_template('astral-moderation/terms_of_service.html')

# Privacy Policy for Astral Moderation
@app.route('/astral-moderation/privacy-policy')
def privacy_policy():
    return render_template('astral-moderation/privacy_policy.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
