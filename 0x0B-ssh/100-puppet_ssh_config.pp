# set up client SSH configuration file so that we can connect to a server without typing a password.



file_line { 'point to identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true,
}

file_line { 'remove passwd authentication':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '	PasswordAuthentication no',
  replace => true,
}
