# Use a lightweight base image
FROM nginx:alpine

# Copy the static webpage files to the nginx web root directory
COPY index.html /usr/share/nginx/html/
COPY images /usr/share/nginx/html/images
COPY js /usr/share/nginx/html/js
COPY styles.css /usr/share/nginx/html/
COPY login /usr/share/nginx/html/login
COPY register /usr/share/nginx/html/register
COPY sKA7cm.webp /usr/share/nginx/html/
COPY yaml-build /usr/share/nginx/html/yaml-build

# Expose the default HTTP port
EXPOSE 80

