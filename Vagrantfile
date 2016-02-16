# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "puppetlabs/centos-7.0-64-puppet"
  config.vm.box_version = "1.0.1"

  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # config.vm.synced_folder "../data", "/vagrant_data"

  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #

  #
  # Add the required puppet modules before provisioning is run by puppet
  #
  config.vm.provision :shell do |shell|
      shell.inline = "puppet module install puppetlabs-stdlib;
                      puppet module install stahnma-epel;
                      puppet module install stankevich-python;
		      touch /etc/puppet/hiera.yaml;
                      exit 0"
  end

  config.vm.provision "puppet" do |puppet|
      puppet.manifests_path = "manifests"
      puppet.manifest_file  = "site.pp"
      puppet.facter = {
          "api_token" => ENV["API_TOKEN"]
      }
  end

end