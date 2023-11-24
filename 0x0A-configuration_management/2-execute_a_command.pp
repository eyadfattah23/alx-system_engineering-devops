# script to kill a process named kill me now

exec {'kill_a_process':
	command => 'pkill -f pkill',
	path    => ['/usr/bin', '/bin'],
	onlyif  => 'pgrep -f killmenow', # Check if the process is running
}
