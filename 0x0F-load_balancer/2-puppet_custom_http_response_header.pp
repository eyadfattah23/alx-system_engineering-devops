# puppet: do task 0 with puppet

package { 'nginx':
  ensure => installed,
}



file {'index':
  ensure  => 'present',
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}

file {'/var/www/html/custom_404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page",
}

file_line { 'redirection 301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4/ permanent;',
}
file_line { 'add header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
