# creates the /tmp/holberton file with the permissions 0744 and sets the owner
file { '/tmp/holberton':
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet',
}
