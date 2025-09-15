# Use the official Postgres image
FROM postgres:15-alpine

# Add GitHub source label (so GHCR links back to repo automatically)
LABEL org.opencontainers.image.source="https://github.com/nadzzdan/3tierapp"

# Set environment variables (override via docker-compose / k8s secrets)
ENV POSTGRES_USER=appuser
ENV POSTGRES_PASSWORD=apppassword
ENV POSTGRES_DB=appdb

# Copy initialization script
COPY init.sql /docker-entrypoint-initdb.d/

# Expose default Postgres port
EXPOSE 5432