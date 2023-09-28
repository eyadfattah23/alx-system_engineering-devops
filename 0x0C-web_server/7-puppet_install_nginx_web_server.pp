# puppet: do all previous tasks with puppet

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'server_config':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4/ permanent;',
}
