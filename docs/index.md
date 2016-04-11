TrueSight Intelligence Lab
============================

Vagrant lab environment for learning about TrueSight Pulse Intelligence.

Includes:
- Virtual machine environment that includes prerequisite tools for running labs
- Demonstration scripts for running labs

## Virtual Machine

The virtual machine environment is configured using vagrant, so it requires the prerequistes listed in the next section.

### Prerequisites

- Vagrant 1.7.2 or later. Vagrant can be downloaded [here](https://www.vagrantup.com/downloads.html)
- VirtualBox 4.3.2.6 or later. VirtualBox can be downloaded [here](https://www.virtualbox.org/wiki/Downloads)
- Git 2.2 or later. If downloading the distribution via git. Git can be downloaded [here](http://git-scm.com/download)

### Downloading the Contents

Either clone (using git) or download the git repository [https://github.com/boundary/vagrant-tsi-lab](https://github.com/boundary/vagrant-tsi-lab)

#### Cloning

```
$ git clone https://github.com/boundary/vagrant-tsi-lab
```

### Starting the Virtual Machine

With the TrueSight Pulse api key perform issue the following command via Unix/Linux shell, or Windows command prompt:

```
$ TSP_API_KEY=<api key> vagrant up
```

### Stopping a Virtual Machine

```
$ vagrant halt
```

### Destroying a Virtual Machine

```
$ vagrant destroy
```

### Logging into the Virtual Machine

```
$ vagrant ssh
```

## Labs

- [Lab 1 - Meters and Plugins](labs/lab1.md)

- [Lab 2 - Introduction Rest](labs/lab2.md)

- [Lab 3 - API Overview](labs/lab3.md)

- [Lab 3 - API - Events into TrueSight Intelligence](labs/lab4.md)

- [Lab 5 - UI Overview](labs/lab5.md)

- [Lab 6 - Metrics APIs](labs/lab6.md)

- [Lab 7 - Log File to API](labs/lab7.md)

- [Lab 8 - API Integration](labs/lab8.md)

- [Lab 7 - TSI UI overview with new data](labs/lab4.md)
