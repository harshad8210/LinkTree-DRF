# Linktree-app-drf

------------
Linktree is an app where user can add, update, read and delete their Links and Social icon links and also can change
their profile theme and icons by login into system by social auths.

## Project Setup

-----------------------

### Creating Migrations

With the model created, the first thing you need to do is create a migration for it. You can do this with the following
command:

```
python manage.py makemigrations
```

### Applying Migrations

You have now created the migration, but to actually make any changes in the database, you have to apply it with the
management command migrate:

```
python manage.py migrate
```

### Creating an admin user

```
python manage.py createsuperuser
```
