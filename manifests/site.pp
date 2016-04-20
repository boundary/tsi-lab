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
  replace => 'no',
  owner => 'vagrant',
  group => 'vagrant',
}

# Run comman file for configuration specific
# to TrueSight Pulse
file { 'tsprc':
  path    => '/home/vagrant/.tsp',
  ensure  => file,
  content => template('tsprc.erb'),
  replace => 'no',
  owner => 'vagrant',
  group => 'vagrant',
}

#
# Bash shell configuration
file { 'bash_profile_user':
  path    => '/home/vagrant/.bash_profile',
  ensure  => file,
  source  => '/vagrant/manifests/bash_profile',
  owner => 'vagrant',
  group => 'vagrant',
}

# Create a bin directory to put local
# executables and scripts that are
# required to be in the PATH variabl
file { 'bin':
   path => '/home/vagrant/bin',
   source => '/vagrant/manifests/bin',
   recurse => true,
}

file { 'vimrc':
  path    => '/home/vagrant/.vimrc',
  source => '/vagrant/manifests/vimrc',
}

file { 'db':
  path    => '/home/vagrant/.db',
  source => '/vagrant/manifests/db',
  owner => 'vagrant',
  group => 'vagrant',
}

package { 'epel-release':
  ensure => 'installed',
}

package { 'openssl-devel':
  ensure => 'installed',
  require => Package['epel-release'],
}

package { 'libffi-devel':
  ensure => 'installed',
  require => Package['epel-release'],
}

package { 'python-devel':
  ensure => 'installed',
  require => Package['epel-release'],
}

package { 'git':
  ensure => 'installed',
  require => Package['epel-release'],
}

package { 'python-requests':
  ensure => 'installed',
  require => Package['epel-release'],
}

package { 'python-pip':
  ensure => 'installed',
  require => Package['epel-release'],
}

package { 'vim-enhanced':
  ensure => 'installed',
  require => Package['epel-release'],
}

package { 'screen':
  ensure => 'installed',
  require => Package['epel-release'],
}

package { 'httpd-tools':
  ensure => 'installed',
  require => Package['epel-release'],
}

service { 'http-stressd':
    ensure => 'running',
    enable => true,
    require => Exec['http-stressd'],
}

exec { 'http-stressd':
  command => '/usr/bin/rpm -ivh https://github.com/jdgwartney/boundary-http-stressd/releases/download/RE-01.00.00/boundary-http-stressd-01.00.00-1.noarch.rpm',
  require => Package['httpd-tools'],
  unless => '/usr/bin/rpm -qi boundary-http-stressd',
}

exec { 'pip-upgrade':
   command => '/usr/bin/pip install --upgrade pip',
   require => Package['python-pip'],
   unless => '/usr/bin/pip install --upgrade pip',
}

exec { 'requests[security]':
   command => '/usr/bin/pip install requests[security]',
   require => [Package['python-pip'], Package['python-devel'], Package['libffi-devel'], Package['openssl-devel']],
   unless => '/usr/bin/pip show demjson',
}

exec { 'jsonlint':
   command => '/usr/bin/pip install demjson',
   require => Package['python-pip'],
   unless => '/usr/bin/pip show demjson',
}

exec { 'python-filelock':
   command => '/usr/bin/pip install filelock',
   require => Package['python-pip'],
   unless => '/usr/bin/pip show filelock',
}

exec { 'python-petl':
   command => '/usr/bin/pip install petl',
   require => Package['python-pip'],
   unless => '/usr/bin/pip show petl',
}

exec { 'apachelog':
   command => '/usr/bin/pip install apachelog',
   require => Package['python-pip'],
   unless => '/usr/bin/pip show apachelog',
}

exec { 'pyowm':
   command => '/usr/bin/pip install pyowm',
   require => Package['python-pip'],
   unless => '/usr/bin/pip show pyowm',
}

exec { 'tweepy':
   command => '/usr/bin/pip install tweepy',
   require => Package['python-pip'],
   unless => '/usr/bin/pip show tweepy',
}

exec { 'ipython':
   command => '/usr/bin/pip install ipython',
   require => Package['python-pip'],
   unless => '/usr/bin/pip show ipython',
}

exec { 'python-pmysql':
   command => '/usr/bin/pip install pymysql',
   require => Package['python-pip'],
   unless => '/usr/bin/pip show pymysql',
}

exec { 'python-tspapi':
   command => '/usr/bin/pip install tspapi',
   require => Package['python-pip'],
   unless => '/usr/bin/pip show tspapi',
}

exec { 'python-tsp-cli':
   command => '/usr/bin/pip install boundary',
   require => Package['python-pip'],
   unless => '/usr/bin/pip show boundary',
}

exec { 'ystockquote':
   command => '/usr/bin/pip install ystockquote',
   require => Package['python-pip'],
   unless => '/usr/bin/pip show ystockquote',
}

# Utility for pretty printing and querying JSON documents
package { 'jq':
  ensure => 'installed',
  require => Package['epel-release'],
}

class {'apache': }
class {'apache::mod::php': }

file { 'html':
  path    => '/var/www/html/index.php',
  source => '/vagrant/manifests/html/index.php',
  owner => 'root',
  group => 'root',
  require => Class['apache::mod::php'],
}

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
     command     => '/home/vagrant/bin/one-liners.py 2>&1 > /dev/null',
     environment => [],
}
