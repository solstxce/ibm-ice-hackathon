# Use a lightweight base image
FROM nginx:alpine

# Copy the static webpage files to the nginx web root directory
COPY * /usr/share/nginx/html/
# Expose the default HTTP port
EXPOSE 80

