# puppet: do task 0 with puppet
package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => "
    server {
        listen 80;
        listen [::]:80 default_server;
        root   /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        server_name localhost;

        add_header X-Served-By ${HOSTNAME};

        location / {
            try_files ${uri} ${uri}/ =404;
        }

        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4/;
        }

        error_page 404 /custom_404.html;
        location = /custom_404.html {
            root /var/www/html;
            internal;
        }
    }
  ",
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
