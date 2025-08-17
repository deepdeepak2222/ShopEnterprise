#!/bin/bash

# Setup environment file for Django application

echo "🚀 Setting up environment configuration..."

# Check if .env file already exists
if [ -f .env ]; then
    echo "⚠️  .env file already exists. Do you want to overwrite it? (y/N)"
    read -r response
    if [[ ! "$response" =~ ^[Yy]$ ]]; then
        echo "❌ Setup cancelled."
        exit 1
    fi
fi

# Copy env.example to .env
if [ -f env.example ]; then
    cp env.example .env
    echo "✅ Created .env file from env.example"
    echo ""
    echo "📝 Please edit the .env file with your specific configuration:"
    echo "   nano .env"
    echo ""
    echo "🔧 Key settings to configure:"
    echo "   - DEBUG: Set to 'True' for development, 'False' for production"
    echo "   - SECRET_KEY: Change this in production!"
    echo "   - DATABASE_PASSWORD: Set a secure password"
    echo "   - ALLOWED_HOSTS: Add your domain names"
    echo ""
    echo "📖 See ENVIRONMENT_SETUP.md for detailed configuration guide"
else
    echo "❌ env.example file not found!"
    exit 1
fi
