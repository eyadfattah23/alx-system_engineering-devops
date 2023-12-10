# puppet: do task 0 with puppet

package { 'nginx':
  ensure => installed,
}



file {'index':
  ensure  => 'present',
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}


file_line { 'redirection 301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4/ permanent;',
}
file_line { 'define server name':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'index index.html index.htm index.nginx-debian.html;',
  line   => 'server_name localhost;',
}
file_line { 'add header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'index index.html index.htm index.nginx-debian.html;',
  line   => 'add_header X-Served-By $HOSTNAME;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
