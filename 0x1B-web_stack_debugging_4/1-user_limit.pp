
# Define vars
$nofil_limit = 97816
$limit_conf_file = '/etc/security/limits.conf'

# Ensure the holberton user exists
user { 'holberton':
  ensure => present,
}

# Configure limits.conf only if holberton exists
file { $limit_conf_file:
  content => "holberton hard nofile ${nofil_limit}\nholberton soft nofile ${nofil_limit}\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  require => User['holberton'], # Ensure user exists before modifying the file
}

# Reload PAM if changes
exec { 'reload_pam':
  command     => "/bin/pkill -HUP -u holberton bash",
  refreshonly => true,
  subscribe   => File[$limit_conf_file],
}
