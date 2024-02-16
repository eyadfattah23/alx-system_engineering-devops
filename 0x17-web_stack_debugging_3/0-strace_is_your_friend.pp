# script to kill a process named kill me now

exec { 'fix_php_typo':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/bin'],
}
