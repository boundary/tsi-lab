# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "puppetlabs/centos-7.0-64-puppet"
  config.vm.box_version = "1.0.1"
  config.vm.hostname = "tsi-lab-01"

  config.vm.synced_folder "manifests/templates", "/tmp/vagrant-puppet/templates"
  config.vm.synced_folder "labs", "/home/vagrant/labs"

  config.vm.network "forwarded_port", guest: 80, host: 8181

  # Add the required puppet modules before provisioning is run by puppet
  config.vm.provision :shell do |shell|
      shell.inline = "
                      puppet module install puppetlabs-stdlib;
                      puppet module install puppetlabs-concat;
                      puppet module install torrancew-cron;
                      puppet module install puppetlabs-mysql;
                      puppet module install puppetlabs-apache;
                      touch /etc/puppet/hiera.yaml;
                      exit 0"
  end

  # Provision our virtual machine with puppet
  config.vm.provision "puppet" do |puppet|
      puppet.manifests_path = "manifests"
      puppet.manifest_file  = "site.pp"
      puppet.options = ["--templatedir","/tmp/vagrant-puppet/templates"]
      puppet.facter = {
          "tsi_email" => ENV["TSI_EMAIL"],
          "tsi_api_token" => ENV["TSI_API_TOKEN"],
          "tsi_api_host" => ENV["TSI_API_HOST"],
          "tsi_app_id" => ENV["TSI_APP_ID"],
          "tsp_email" => ENV["TSP_EMAIL"],
          "tsp_api_token" => ENV["TSP_API_TOKEN"],
          "tsp_api_host" => ENV["TSP_API_HOST"],
      }
  end

end
