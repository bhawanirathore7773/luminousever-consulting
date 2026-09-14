# Luminousever Consulting

High-performance enterprise SAP consulting website built with Python, Django and PostgreSQL.

## Render deployment

1. Create a new Blueprint in Render from this repository.
2. Render reads `render.yaml`.
3. The Blueprint creates:
   - Django web service
   - PostgreSQL database
   - Redis
   - Celery worker
4. Render generates `SECRET_KEY`.
5. After the first deployment, set `DEFAULT_FROM_EMAIL` and `LEAD_NOTIFICATION_EMAIL` in the web service and worker environment.
6. If using a custom domain, replace the generated `.onrender.com` host/origin values with the real domain.
7. Confirm `/health/` returns HTTP 200 before switching DNS.

## Production architecture

Browser → CDN → Render web service → Gunicorn → Django → PostgreSQL
                                                     ↘ Redis → Celery

PostgreSQL is the source of truth. Redis is only used for caching and asynchronous work.

## Local development

1. Copy `.env.example` to `.env`.
2. Install `requirements.txt`.
3. Run migrations with development settings.
4. Start Django.

## Important

Render is the first deployment target. Hostinger VPS is the later production migration target. Do not commit real secrets, SMTP credentials, database passwords or API tokens.
