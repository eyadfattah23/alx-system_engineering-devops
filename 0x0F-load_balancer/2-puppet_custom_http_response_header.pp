# puppet: do task 0 with puppet

exec { 'apt-update':
  command => '/usr/bin/apt update',
}

# Install Nginx package
package { 'nginx':
    ensure  => present,
    require => Exec['apt-update'],
}

# Add custom HTTP header directive to Nginx configuration
file_line {'Adding_Header':
    ensure  => 'present',
    path    => '/etc/nginx/sites-available/default',
    after   => 'listen 80 default_server;',
    line    => 'add_header X-Served-By $hostname;',
    require => Package['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
}
