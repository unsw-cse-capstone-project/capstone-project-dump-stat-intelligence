
# Pantry Pirate
COMP3900 Group Project - Dump Stat Intelligence

## Getting Started

### Using Make

Ensure you have concurrently installed (`yarn global add concurrently`) and are in the python virtual environment for backend (`pipenv shell` in `/backend/pantrypirate`). You can use these commands to run the project:

- `make backend`: run the backend on port 8000
- `make frontend`: run the frontend on port 3000
- `make all`: simultaneously make frontend and backend

### Frontend

See [The API Spec](API_SPEC.md) for details on what the frontend expects

#### Running the project**

- Ensure nodejs and yarn are installed
- Install required packages: `yarn install`

Dev server (hot reloading): `yarn run dev`

Build for production: `yarn run build`



#### Frontend File Structure
```
/components
/lib
  /api
  /redux
  /utils
/pages
/public
/styles
```

- `/components` contains shared React components used in various routes
- `/lib` library of helper scripts
  - `/api` scripts associated with making calls to and from the backend
  - `/redux` files associated with the state management of the site, including the redux actions and reducers
  - `/utils` remaining helper scripts, mainly are localstate management
- `/pages` contains views for routes. Routes for the frontend are created based on the file structure underneath this folder (https://nextjs.org/docs/routing/introduction)
- `/styles` contains **GLOBAL** styles. For most Sass work you should create a module for each component in the same directory as the component. I.e. create `components/Button.js` and then also create `components/Button.module.scss` and import the scss file in the component.

#### Backend File Structure
```
/pantrypirate
    db.sqlite3
    manage.py
/pantrypirate/backend
    /migrations
    admin.py
    apps.py
    models.py
    serializers.py
    tests.py
    urls.py
    views.py
/pantrypirate/pantrypirate
```

- `/pantrypirate` 
  - `db.sqlite3` database for backend
  - `manage.py` backend interaction entry point
  - `/backend`
    - `/migrations` Django Sqlite database temporary migration folder
    - `admin.py` registering models for editing on Django admin page
    - `apps.py` registering backend as an application for the admin
    - `models.py` contains Django models for database interaction
    - `serializers.py` contains REST serializers for interaction between
     frontend and database
    - `tests.py` contains tests for the backend
    - `urls.py` contains routes for backend views
    - `views.py` contains scripts to deal with each route
  - `/pantrypirate` contains high level application configuration for Django