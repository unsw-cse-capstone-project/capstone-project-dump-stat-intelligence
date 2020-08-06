.PHONY: backend frontend all
# You will need all dependencies installed and be within the python virtualenv for the backend
# You will also need concurrently installed (> yarn global add concurrently)

backend:
	cd backend/pantrypirate && python manage.py runserver
#frontend:
#	cd frontend && yarn run dev
frontend:
	cd frontend && yarn run build && yarn run start

all:
	concurrently "make frontend" "make backend"