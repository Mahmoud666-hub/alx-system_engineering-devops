#fix that make 2000 requests, 943 requests failed
sed -i 's/15/1000/' /etc/default/nginx
service nginx restart