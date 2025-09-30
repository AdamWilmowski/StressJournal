# Setup PostgreSQL on Heroku

## The Problem
Your Heroku app is still using SQLite instead of PostgreSQL, which causes the "table already exists" error because SQLite files are ephemeral on Heroku.

## Solution: Add PostgreSQL Addon

### Step 1: Add PostgreSQL Addon
Run this command in your terminal (make sure you're logged into Heroku CLI):

```bash
heroku addons:create heroku-postgresql:hobby-dev -a your-app-name
```

Replace `your-app-name` with your actual Heroku app name.

### Step 2: Verify PostgreSQL is Added
Check your addons:
```bash
heroku addons -a your-app-name
```

You should see something like:
```
heroku-postgresql (hobby-dev)  postgresql-xxxxx-xxxxx
```

### Step 3: Check Database URL
```bash
heroku config:get DATABASE_URL -a your-app-name
```

This should return a PostgreSQL URL starting with `postgres://`

### Step 4: Redeploy
After adding PostgreSQL, redeploy your app:
```bash
git push heroku main
```

## Alternative: Manual Setup via Heroku Dashboard

1. Go to your Heroku app dashboard
2. Click on the "Resources" tab
3. In the "Add-ons" section, search for "Heroku Postgres"
4. Select "Heroku Postgres" and choose "Hobby Dev - Free"
5. Click "Provision"
6. Redeploy your app

## What This Fixes

- ✅ Persistent database storage
- ✅ No more "table already exists" errors
- ✅ Proper PostgreSQL support
- ✅ Admin user will be created successfully

## After Setup

Once PostgreSQL is added, your app will:
1. Use PostgreSQL instead of SQLite
2. Create tables without conflicts
3. Successfully create the admin user
4. Persist data between deployments

## Login Credentials

After successful deployment, login with:
- **Username**: `admin`
- **Password**: `admin123`
