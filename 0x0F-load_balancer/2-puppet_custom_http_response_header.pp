# Use puppet to creat a custom HTTP header response
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

file_line { 'add header':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => "\n\tadd_header X-Served-By \$hostname;",
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}