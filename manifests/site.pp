# Explictly set to avoid warning message
Package {
  allow_virtual => false,
}

file { 'tsirc':
  path    => '/home/vagrant/.tsi',
  ensure  => file,
  content => template('tsirc.erb'),
}

file { 'bin':
   path => '/home/vagrant/bin',
   source => '/vagrant/bin',
   recurse => true,
}

exec { 'entities':
    command => '/home/vagrant/bin/install.sh',
}

file { 'bash_profile':
  path    => '/home/vagrant/.bash_profile',
  ensure  => file,
  source  => '/vagrant/manifests/bash_profile',
}

package { 'epel-release':
  ensure => 'installed'
}

package { 'python-pycurl':
  ensure => 'installed',
}

package { 'python-requests':
  ensure => 'installed',
}

package { 'jq':
  ensure => 'installed',
  require => Package['epel-release'],
}

class { '::mysql::server':
  root_password => 'root123',
}

class { '::mysql:server:monitor':
  mysql_monitor_username => 'monitor',
  mysql_monitor_password => 'monitor123',
  mysql_monitor_hostname => '127.0.0.1',
}

cron::job{
  'monitor':
    minute      => '*',
    hour        => '*',
    date        => '*',
    month       => '*',
    weekday     => '*',
    user        => 'vagrant',
    command     => '/home/vagrant/bin/monitor.py | logger',
    environment => [ "TSI_API_KEY=$api_key", "TSI_API_HOST=$api_host"  ];
}
