#kills the kill me now process
exec { 'pkill':
     command => 'pkill killmenow',
     path => '/usr/bin'
}
