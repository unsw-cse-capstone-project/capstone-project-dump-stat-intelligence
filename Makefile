.PHONY: backend frontend all
# You will need all dependencies installed and be within the python virtualenv for the backend
# You will also need concurrently installed (> yarn global add concurrently)

backend:
	cd backend/pantrypirate && python manage.py runserver
frontend:
	cd frontend && yarn run dev
all:
	concurrently "make frontend" "make backend"