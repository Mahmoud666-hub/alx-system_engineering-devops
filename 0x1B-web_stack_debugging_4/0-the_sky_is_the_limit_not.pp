#fix that make 2000 requests, 943 requests failed
# Ensure the ULIMIT is set correctly
file_line { 'set_ulimit_for_nginx':
  path  => '/etc/default/nginx',
  line  => 'ULIMIT="-n 4096"',
  match => '^ULIMIT=',
  notify => Exec['restart_nginx'],  # Restart Nginx only if this line is changed
}

# Restart nginx if modified
exec { 'restart_nginx':
  command     => 'service nginx restart',
  refreshonly => true,  # Only restart if notified by a change
}
