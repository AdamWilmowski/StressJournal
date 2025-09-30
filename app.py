"""
Main Flask application for the Stress Diary.
This is the refactored version with proper separation of concerns.
"""

from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
