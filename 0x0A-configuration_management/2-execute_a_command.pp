# Define an exec resource to kill the process
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/bin'],
  onlyif  => 'pgrep -f killmenow', # Check if the process is running
}

