# script to install flask
package { 'flask_installation':
	name => 'flask',
	provider => 'pip3',
	ensure => '2.1.0',

}
