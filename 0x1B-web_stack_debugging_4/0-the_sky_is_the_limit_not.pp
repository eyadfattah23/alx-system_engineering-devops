# Puppet manifest to update ULIMIT in /etc/default/nginx and restart nginx

# Ensure the ULIMIT line is updated to "-n 2048"
exec { 'update_ulimit':
  command => '/bin/sed -i \'s/^ULIMIT="-n 15"/ULIMIT="-n 2048"/\' /etc/default/nginx',
  unless  => '/bin/grep -q \'^ULIMIT="-n 2048"\' /etc/default/nginx',
  notify  => Service['nginx'],
}

# Manage the nginx service
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => Exec['update_ulimit'],
}
