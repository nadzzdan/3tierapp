FROM nginx:alpine

# Add GitHub source label (so GHCR links back to repo automatically)
LABEL org.opencontainers.image.source="https://github.com/nadzzdan/3tier-web-app"

# Copy the frontend files to nginx html directory
COPY . /usr/share/nginx/html/

# (Optional) If you have a custom NGINX config, uncomment:
# COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]