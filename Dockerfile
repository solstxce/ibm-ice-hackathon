# Use a lightweight base image
FROM nginx:alpine

# Copy the static webpage files to the nginx web root directory
# COPY index.html /usr/share/nginx/html/
# COPY images /usr/share/nginx/html/images
# COPY js /usr/share/nginx/html/js
COPY * /usr/share/nginx/html/

# Expose the default HTTP port
EXPOSE 80

