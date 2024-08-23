#fix that make 2000 requests, 943 requests failed
exec { 'modify_max_open_files_limit':
  command => 'sed -i "s/15/10000/" /etc/default/nginx',
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  unless  => 'grep -q "max open files limit = 10000" /etc/default/nginx',  # Check if the limit is already set
  notify  => Exec['restart_nginx'],  # Notify restart if the file is modified
}

# Restart Nginx service
exec { 'restart_nginx':
  command     => 'service nginx restart',
  refreshonly => true,  # Only restart if notified by a change
}
