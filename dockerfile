# Stage 1: Build the FastAPI backend
FROM python:3.9-slim AS fastapi
WORKDIR /app
COPY app/ /app/app
COPY requirements.txt /app
COPY .env /app/.env
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Stage 2: Nginx to serve the HTML frontend and reverse proxy to FastAPI
FROM nginx:alpine AS nginx
COPY templates/index.html /usr/share/nginx/html/index.html
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 for the web server
EXPOSE 80

# Run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
