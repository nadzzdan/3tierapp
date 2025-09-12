# ===============================
# Stage 1: Build React frontend
# ===============================
FROM node:20-bullseye-slim AS build

# Install build tools (needed for native npm modules)
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 make g++ \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only package files first (better cache for deps)
COPY package*.json ./

# Install dependencies (prefer npm ci, fallback to npm install)
RUN npm ci || npm install

# Copy all frontend source
COPY . .

# Build production assets
RUN npm run build

# ===============================
# Stage 2: Serve with Nginx
# ===============================
FROM nginx:alpine

# Copy built frontend from build stage
COPY --from=build /app/build /usr/share/nginx/html

# Expose container port
EXPOSE 80

# Run nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
#test