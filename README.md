# Pantry Pirate
COMP3900 Group Project - Dump Stat Intelligence

## Getting Started

### Frontend

**Running the project**

- Ensure nodejs and yarn are installed
- Install required packages: `yarn install`

Dev server (hot reloading): `yarn run dev`

Build for production: `yarn run build`

#### Exporting for Django

See: https://nextjs.org/docs/advanced-features/static-html-export

Run `next export` which will generate static html that will be able to be served from the django server (NB: you will need to run `build` before exporting)
