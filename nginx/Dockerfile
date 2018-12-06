FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

# COPY nginx.conf /etc/nginx/sites-available/

COPY nginx.conf /etc/nginx/conf-d/

RUN cat /etc/nginx/conf-d/nginx.conf