FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
COPY manifest.webmanifest maptight-icon.svg apple-touch-icon.svg maptight-og.svg /usr/share/nginx/html/
EXPOSE 80
