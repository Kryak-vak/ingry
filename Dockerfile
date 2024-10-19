FROM python:3.12-alpine3.20

ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # Poetry's configuration:
    POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=1.8.3

# Install system dependencies
RUN apk update && apk add --no-cache \
    build-base \
    postgresql15-dev \
    postgresql15-client \
    curl

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Create and set the working directory
WORKDIR /ingry

# Copy the application code
COPY ./ingry /ingry

# Install Python dependencies
RUN echo "DJANGO_ENV is set to: $DJANGO_ENV"
RUN if [ "$DJANGO_ENV" = "production" ]; then \
      echo "Installing production dependencies..."; \
      poetry install --only main --no-interaction --no-ansi --sync; \
   else \
      echo "Installing all dependencies (non-production environment)..."; \
      poetry install --no-interaction --no-ansi --sync; \
   fi

# Run collectstatic if you use Django static files (uncomment if necessary)
RUN if [ "$DJANGO_ENV" = "production" ]; then \
      poetry run python manage.py collectstatic --noinput; \
    else \
      echo "Skipping collectstatic, not in production environment."; \
    fi

# Expose port 8000 for the Django development server
EXPOSE 8000

RUN adduser --disabled-password ingry-user

USER ingry-user
