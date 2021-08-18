# Client ssh_config file that we can connect to the server without a pass
file {'Configuration File':
  ensure => file,
  name   => 'ssh_config',
  path   => '/etc/ssh/ssh_config'
}

file_line { 'Declare identity file':
  ensure => file,
  path   => '/etc/ssh/ssh_config',
  line   => '  IdentityFile ~/.ssh/holberton'
}

file_line { 'Turn off passwd auth':
  ensure => file,
  path   => '/etc/ssh/ssh_config',
  line   => '  PasswordAuthentication no'
}

