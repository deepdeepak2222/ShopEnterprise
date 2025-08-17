# Environment Configuration Guide

This guide explains how to configure the Django application using environment variables.

## Quick Setup

1. Copy the example environment file:
   ```bash
   cp env.example .env
   ```

2. Edit the `.env` file with your specific configuration values.

## Environment Variables

### Database Configuration
- `DATABASE_NAME`: Database name (default: shop)
- `DATABASE_USER`: Database username (default: shop)
- `DATABASE_PASSWORD`: Database password (default: shop)
- `DATABASE_HOST`: Database host (default: shop_psql_db)
- `DATABASE_PORT`: Database port (default: 5433)

### Django Configuration
- `DEBUG`: Set to "True" for development, "False" for production
- `SECRET_KEY`: Django secret key (change in production!)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

### CORS Configuration
- `CORS_ALLOWED_ORIGINS_DEV`: Comma-separated list of allowed origins for development
- `CORS_ALLOWED_ORIGINS_PROD`: Comma-separated list of allowed origins for production

### Security Settings (Production Only)
- `SECURE_SSL_REDIRECT`: Force HTTPS redirect (default: True in production)
- `SESSION_COOKIE_SECURE`: Secure session cookies (default: True in production)
- `CSRF_COOKIE_SECURE`: Secure CSRF cookies (default: True in production)
- `SECURE_BROWSER_XSS_FILTER`: Enable XSS filter (default: True in production)
- `SECURE_CONTENT_TYPE_NOSNIFF`: Enable content type sniffing protection (default: True in production)

## Development vs Production

### Development Mode (DEBUG=True)
- Less restrictive CORS settings
- Verbose logging
- Disabled security headers
- All HTTP methods allowed
- Console and file logging

### Production Mode (DEBUG=False)
- Strict CORS settings
- Error-only logging
- All security headers enabled
- Limited HTTP methods
- File-only logging

## Example Configurations

### Development (.env)
```env
DEBUG=True
SECRET_KEY=your-dev-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1,.localhost
CORS_ALLOWED_ORIGINS_DEV=http://localhost:5031,http://127.0.0.1:5031
```

### Production (.env)
```env
DEBUG=False
SECRET_KEY=your-super-secure-production-key
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
CORS_ALLOWED_ORIGINS_PROD=https://your-domain.com,https://www.your-domain.com
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

## Security Notes

1. **Never commit your `.env` file** - it's already in `.gitignore`
2. **Change the SECRET_KEY** in production
3. **Use strong passwords** for database and other services
4. **Enable HTTPS** in production
5. **Restrict ALLOWED_HOSTS** to your actual domains

## Troubleshooting

### CORS Issues
- Ensure `CORS_ALLOWED_ORIGINS_DEV` includes your frontend URL in development
- Check that `DEBUG=True` for development mode
- Verify the frontend is making requests to the correct backend URL

### Database Connection Issues
- Verify database credentials in `.env`
- Ensure database service is running
- Check network connectivity between services

### Logging Issues
- Ensure the `logs/` directory exists
- Check file permissions for log writing
- Verify log level settings match your needs
