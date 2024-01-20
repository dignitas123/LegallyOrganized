# LegallyOrganized

Welcome to Legally Organized!

# Migration (first step)

```bash
docker-compose run backend python manage.py makemigrations legal_requests
docker-compose run backend python manage.py migrate

```
# Start Docker to see dev build

```bash
docker compose up --build
```