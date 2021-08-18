# client SSH configuration file that we can connect to the server without a pass.
file_line { 'Declare identify file':
    ensure  => present;
    path    => '/etc/ssh/ssh_config',
    line    => ' IdentifyFile ~/.ssh/holberton',
    replace => true,
}

file_line { 'Turn off passwd auth':
    ensure  => 'present',
    path    => '/etc/ssh/ssh_config,
    line    => 'PasswordAuthentication no',
    replace => true,
}
