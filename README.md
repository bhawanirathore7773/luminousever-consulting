# Luminousever Consulting

High-performance enterprise SAP consulting website built with Python, Django and PostgreSQL.

## Architecture
Browser → CDN/Cloudflare → Nginx → Gunicorn → Django → PostgreSQL. Redis is used for caching and optional background work.

## Principles
- Django server-side rendering for public SEO pages.
- PostgreSQL is the source of truth.
- Redis is for cache/queue use cases, not persistent business data.
- Minimal JavaScript and dependencies.
- Indexed, optimized querysets.
- Mobile-first Core Web Vitals.
- Environment-based secrets.
- Stateless web workers for horizontal scaling.

## Local development
1. Copy .env.example to .env.
2. Install requirements/development.txt.
3. Run migrations with config.settings.development.
4. Start Django with config.settings.development.

## Production
Use PostgreSQL, Redis, Nginx and Gunicorn. Tune Gunicorn workers from actual CPU/RAM and workload measurements.

## Performance acceptance
Validate N+1 queries, indexes, caching, static assets, image payloads, JS size, mobile UX, SEO, security headers, contact reliability and load performance before production.