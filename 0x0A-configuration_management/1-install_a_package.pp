# script to install flask
package { 'flask_installation':
  ensure   => '2.1.0',
  provider => 'pip3',
  name     => 'Flask',

}
