# change hard and soft limits for opening files for holberton user 

exec { 'change_hard_limit':
    command => '/bin/sed -i "s/5/1024/g" /etc/security/limits.conf',
}

exec { 'change_soft_limit':
    command => '/bin/sed -i "s/4/1024/g" /etc/security/limits.conf',
}
