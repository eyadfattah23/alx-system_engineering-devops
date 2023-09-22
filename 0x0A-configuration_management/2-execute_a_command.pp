# Define an exec resource to kill the process
exec { 'killmenow':
  command     => 'pkill -f killmenow',
}
