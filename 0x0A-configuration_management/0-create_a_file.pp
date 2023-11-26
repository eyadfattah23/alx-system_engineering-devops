# create a file in /tmp.
file { 'Create a file':
  path    => '/tmp/school',
  ensure  => 'present',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
