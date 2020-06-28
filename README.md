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

#### Exporting for Django

See: https://nextjs.org/docs/advanced-features/static-html-export

Run `next export` which will generate static html that will be able to be served from the django server (NB: you will need to run `build` before exporting)

#### File Structure

```
/pages
  _app.js (applies global styles)
/components
/public
/styles
/util
```


- `/pages` contains views for routes. Routes for the frontend are created based on the file structure underneath this folder (https://nextjs.org/docs/routing/introduction)
- `/components` contains shared React components used in various routes
- `/util` helper scripts used by components
- `/styles` contains **GLOBAL** styles. For most Sass work you should create a module for each component in the same directory as the component. I.e. create `components/Button.js` and then also create `components/Button.module.scss` and import the scss file in the component.
