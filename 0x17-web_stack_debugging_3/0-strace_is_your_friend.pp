# find out why Apache is returning a 500 error

exec {'replace':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin','/usr/bin']
}
