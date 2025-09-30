# Change Admin Password Methods

## Method 1: Using the Password Change Script

### Local Usage:
```bash
# Interactive mode
python change_admin_password.py

# Non-interactive mode
python change_admin_password.py admin newpassword123
```

### On Heroku:
```bash
# Interactive mode
heroku run python change_admin_password.py

# Non-interactive mode
heroku run python change_admin_password.py admin newpassword123
```

## Method 2: Environment Variables (Recommended for Heroku)

### Set Custom Admin Password via Heroku Config:
```bash
# Set custom admin password
heroku config:set ADMIN_PASSWORD=your_new_password

# Set custom admin username (optional)
heroku config:set ADMIN_USERNAME=your_admin_username

# Set custom admin email (optional)
heroku config:set ADMIN_EMAIL=your_admin@email.com
```

### Then redeploy:
```bash
git commit --allow-empty -m "Trigger redeploy for new admin password"
git push heroku main
```

## Method 3: Direct Database Update (Advanced)

### On Heroku Console:
```bash
heroku run python -c "
from app import create_app
from app.models import db, User
app = create_app()
with app.app_context():
    admin = User.query.filter_by(username='admin').first()
    if admin:
        admin.set_password('newpassword123')
        db.session.commit()
        print('Password updated!')
    else:
        print('Admin user not found!')
"
```

## Method 4: Using the Existing set_admin.py Script

### Update existing admin:
```bash
# This will update the existing admin user's password
heroku run python set_admin.py
# Then enter the same username but new password
```

## Recommended Approach

For **Heroku deployment**, I recommend **Method 2** (Environment Variables):

1. Set the new password: `heroku config:set ADMIN_PASSWORD=your_new_password`
2. Redeploy: `git commit --allow-empty -m "Update admin password" && git push heroku main`
3. The app will create/update the admin user with the new password

This method is:
- ✅ Secure (password not in code)
- ✅ Easy to change
- ✅ Works with the existing admin creation system
- ✅ No manual database manipulation needed
