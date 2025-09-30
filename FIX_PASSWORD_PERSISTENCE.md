# Fix Password Persistence Issue

## The Problem
Your password changes don't persist because **Heroku is using SQLite**, which is **ephemeral** (data gets lost on each deployment/restart).

## The Solution
You need to add **PostgreSQL** to your Heroku app for persistent data storage.

## Step-by-Step Fix

### Step 1: Check Current Database Status
```bash
heroku run python check_heroku_database.py
```

### Step 2: Add PostgreSQL to Heroku
```bash
# Replace 'your-app-name' with your actual Heroku app name
heroku addons:create heroku-postgresql:hobby-dev -a your-app-name
```

### Step 3: Verify PostgreSQL is Added
```bash
# Check addons
heroku addons -a your-app-name

# Check database URL
heroku config:get DATABASE_URL -a your-app-name
```

You should see:
- A PostgreSQL addon in the addons list
- A DATABASE_URL starting with `postgres://`

### Step 4: Redeploy Your App
```bash
git commit --allow-empty -m "Switch to PostgreSQL"
git push heroku main
```

### Step 5: Set Your Custom Admin Password
```bash
# Set your new password
heroku config:set ADMIN_PASSWORD=your_new_secure_password

# Redeploy to apply the password
git commit --allow-empty -m "Set custom admin password"
git push heroku main
```

### Step 6: Verify Everything Works
```bash
# Check database status again
heroku run python check_heroku_database.py

# Test login with your new password
```

## Alternative: Quick Fix Without PostgreSQL

If you don't want to add PostgreSQL right now, you can use this workaround:

### Method 1: Set Password via Environment Variable
```bash
# Set your password as an environment variable
heroku config:set ADMIN_PASSWORD=your_new_password

# The app will use this password on each restart
```

### Method 2: Use the Password Change Script on Each Restart
```bash
# Run this after each deployment/restart
heroku run python change_admin_password.py
```

## Why This Happens

1. **SQLite on Heroku is ephemeral** - files get deleted on each deployment
2. **PostgreSQL is persistent** - data survives deployments and restarts
3. **Environment variables persist** - so ADMIN_PASSWORD will always be used

## Recommended Solution

**Add PostgreSQL** - it's free for hobby-dev tier and solves all persistence issues:

```bash
heroku addons:create heroku-postgresql:hobby-dev -a your-app-name
```

This will:
- ✅ Make all data persistent
- ✅ Fix password persistence
- ✅ Fix stress event persistence
- ✅ Make your app production-ready

## After Adding PostgreSQL

Your app will:
1. Use PostgreSQL instead of SQLite
2. Persist all data between deployments
3. Respect your ADMIN_PASSWORD environment variable
4. Work reliably in production
