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

package { 'libcurl-devel':
  ensure => 'installed',
}

package { 'jq':
  ensure => 'installed',
  require => Package['epel-release'],
}

class { 'python' :
  version    => 'system',
  pip        => 'latest',
  dev        => 'present',
  virtualenv => 'present',
}

python::virtualenv { '/home/vagrant/python' :
  ensure       => present,
  version      => 'system',
  requirements => '/vagrant/requirements.txt',
  owner        => 'vagrant',
  group        => 'vagrant',
}


