# puppet: do all previous tasks with puppet

  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure     => running,
    enable     => true,
    hasstatus  => true,
    hasrestart => true,
  }

file {'index':
  ensure  => 'present',
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}


file_line { 'redirection 301':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  line    => 'index  index.html index.htm;',
  after   => 'index  index.html index.htm;',
  content =>'    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4/;
    }',
}
