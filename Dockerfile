FROM python:3.10.11-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

# Create app user
RUN groupadd -r shop && useradd -r -g shop shop

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /apps/shop

# Copy requirements and install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy application code
COPY shop/ /apps/shop/
COPY tenant.py /apps/shop/

# Create logs directory
RUN mkdir -p /var/log/shop && chown -R shop:shop /var/log/shop

# Change ownership of the app directory
RUN chown -R shop:shop /apps/shop

# Switch to non-root user
USER shop

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=5 \
    CMD curl -f http://localhost:8000/health/ || exit 1

# Default command - run migrations, create tenant, then start server
CMD ["bash", "-c", "python manage.py migrate_schemas --shared && python manage.py migrate_schemas && python manage.py runserver 0.0.0.0:8000"]

