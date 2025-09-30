"""
Main Flask application for the Stress Diary.
This is the refactored version with proper separation of concerns.
"""

import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    # Get port from environment variable (for cloud deployment) or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Only run in debug mode if not in production
    debug = os.environ.get('FLASK_ENV') != 'production'
    
    app.run(debug=debug, host='0.0.0.0', port=port)
