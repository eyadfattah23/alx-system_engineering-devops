# puppet script that solves the problem of many requests


file_line { 'update_ulimit':
  path  => '/etc/default/nginx',
  match => '^ULIMIT=',
  line  => 'ULIMIT="-n 2048"',
}


exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
