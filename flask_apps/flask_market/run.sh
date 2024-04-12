#!/bin/bash


# Set environment variables if necessary
export FLASK_APP=app.py
export FLASK_ENV=development

# Start the Flask application
flask run --debug --host=0.0.0.0 --port=5000  # Adjust host and port as needed
