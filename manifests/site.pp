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

cron::job{
  'monitor':
    minute      => '*',
    hour        => '*',
    date        => '*',
    month       => '*',
    weekday     => '*',
    user        => 'vagrant',
    command     => '/home/vagrant/bin/monitor.py',
    environment => [ "TSI_API_KEY=$api_key"  ];
}
