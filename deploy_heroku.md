# Heroku Deployment Guide for Stress Diary

## Prerequisites
1. Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
2. Create a Heroku account: https://signup.heroku.com/

## Deployment Steps

### 1. Login to Heroku
```bash
heroku login
```

### 2. Create a new Heroku app
```bash
heroku create your-app-name
# Replace 'your-app-name' with your desired app name
```

### 3. Set environment variables (optional)
```bash
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your-secret-key-here
```

### 4. Deploy to Heroku
```bash
git push heroku main
```

### 5. Create database tables
```bash
heroku run python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all(); print('Database tables created!')"
```

### 6. Create a user account
```bash
heroku run python create_user.py
```

### 7. Open your app
```bash
heroku open
```

## Important Notes

- The app uses SQLite database which is stored in the `instance/` folder
- Heroku's filesystem is ephemeral, so data will be lost when the dyno restarts
- For production use, consider upgrading to PostgreSQL: `heroku addons:create heroku-postgresql:hobby-dev`

## Troubleshooting

- Check logs: `heroku logs --tail`
- Access Heroku shell: `heroku run bash`
- Restart app: `heroku restart`
