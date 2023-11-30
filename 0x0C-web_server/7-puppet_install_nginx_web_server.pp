# puppet: do all previous tasks with puppet

package { 'nginx':
  ensure => installed,
}



file {'index':
  ensure  => 'present',
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}


file_line { 'redirection 301':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4/ permanent;',
  after  => 'index  index.html index.htm;',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
  }
