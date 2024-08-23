#fix that make 2000 requests, 943 requests failed
exec { 'up_nginx_conf':
  command => "/usr/bin/env sed -i 's/15/1000/' /etc/default/nginx",
  notify  => Service['nginx'],
}
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Exec['up_nginx_conf'],
}