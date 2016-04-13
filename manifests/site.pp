# Explictly set to avoid warning message
Package {
  allow_virtual => false,
}


# Run comman file for configuration specific
# to TrueSight Intelligence
file { 'tsirc':
  path    => '/home/vagrant/.tsi',
  ensure  => file,
  content => template('tsirc.erb'),
}

# Run comman file for configuration specific
# to TrueSight Pulse
file { 'tsprc':
  path    => '/home/vagrant/.tsp',
  ensure  => file,
  content => template('tsprc.erb'),
}

# Create a bin directory to put local
# executables and scripts that are
# required to be in the PATH variabl
file { 'bin':
   path => '/home/vagrant/bin',
   source => '/vagrant/manifests/bin',
   recurse => true,
}

# Directory for lab exercises
#file { 'labs':
#   path => '/home/vagrant/labs',
#   source => '/vagrant/manifests/labs',
#   recurse => true,
#}

# Bash shell configuration
file { 'bash_profile':
  path    => '/home/vagrant/.bash_profile',
  ensure  => file,
  source  => '/vagrant/manifests/bash_profile',
}

file { 'vimrc':
  path    => '/home/vagrant/.vimrc',
  source => '/vagrant/manifests/vimrc',
}

file { 'db':
  path    => '/home/vagrant/.db',
  source => '/vagrant/manifests/db',
}

package { 'epel-release':
  ensure => 'installed',
}

package { 'git':
  ensure => 'installed',
  require => Package['epel-release'],
}

package { 'python-pycurl':
  ensure => 'installed',
}

package { 'python-requests':
  ensure => 'installed',
}

package { 'python-pip':
  ensure => 'installed',
  require => Package['epel-release'],
}

package { 'vim-enhanced':
  ensure => 'installed',
  require => Package['epel-release'],
}

exec { 'python-petl':
   command => '/usr/bin/pip install petl',
   require => Package['python-pip'],
}

exec { 'ipython':
   command => '/usr/bin/pip install ipython',
   require => Package['python-pip'],
}

exec { 'python-pmysql':
   command => '/usr/bin/pip install pymysql',
   require => Package['python-pip'],
}

exec { 'python-tspapi':
   command => '/usr/bin/pip install tspapi',
   require => Package['python-pip'],
}

exec { 'python-boundary-cli':
   command => '/usr/bin/pip install boundary',
   require => Package['python-pip'],
}

exec { 'python-security':
   command => '/usr/bin/pip install requests[security]',
   require => Package['python-pip'],
}

# Utility for pretty printing and querying JSON documents
package { 'jq':
  ensure => 'installed',
  require => Package['epel-release'],
}

class {'apache': }

# Install MySQL for lab exercises that require
# a database
class { '::mysql::server':
  root_password => 'root123',
}

# Create a monitor user if we want to install
# the TrueSight Pulse MySQL Plugin
class { '::mysql::server::monitor':
  mysql_monitor_username => 'monitor',
  mysql_monitor_password => 'monitor123',
  mysql_monitor_hostname => '127.0.0.1',
}

# Create a database for storing our application
# schema for lab exercises
mysql::db { 'app':
  user     => 'admin',
  password => 'admin123',
  host     => 'localhost',
  grant    => ['SELECT', 'INSERT', 'EXECUTE', 'UPDATE'],
  sql      => '/vagrant/manifests/sql/app.sql',
  import_timeout => 900,
}

# System wide cron job that inserts data into the
# application data base to simulate new data being generated
cron::job {
  'db-add':
     minute      => '*',
     hour        => '*',
     date        => '*',
     month       => '*',
     weekday     => '*',
     user        => 'vagrant',
     command     => '/home/vagrant/bin/db-add.sh | logger',
}

cron::job {
  'one-liners':
     minute      => '*',
     hour        => '*',
     date        => '*',
     month       => '*',
     weekday     => '*',
     user        => 'vagrant',
     command     => '/home/vagrant/bin/one-liners.py',
     environment => [],
}
