from flask import Flask, request, render_template
import os
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def index():
    logger.info("Rendering index page")
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    logger.info("Processing result")
    try:
        diameter = int(request.form['diameter'])
        if diameter >= 50000:
            exoplanet_type = f"An exoplanet with the diameter of {diameter} km is a Gas Giant."
        elif 30000 <= diameter < 50000:
            exoplanet_type = f"An exoplanet with the diameter of {diameter} km is Neptunian."
        elif 13000 <= diameter < 30000:
            exoplanet_type = f"An exoplanet with the diameter of {diameter} km is a Super-Earth."
        elif 5000 <= diameter < 13000:
            exoplanet_type = f"An exoplanet with the diameter of {diameter} km is Terrestrial."
        else:
            exoplanet_type = f"An exoplanet with the diameter of {diameter} km probably doesn't exist."
    except ValueError:
        exoplanet_type = "Invalid input. Please enter a valid number for the diameter."
    logger.info(f"Exoplanet type determined: {exoplanet_type}")
    return render_template('result.html', exoplanet_type=exoplanet_type)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"Starting application on port {port}")
    app.run(host='0.0.0.0', port=port)
else:
    logger.info("Application imported, not running directly")