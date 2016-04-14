Virtual Machine
===============

This section describes how to get your virtual machine environment up and running on
your Windows or Mac OS X laptop or Desktop.

Before proceeding ensure that you have met the prerequisites listed [here](prerequisites.md)

### Downloading the Contents

The virtual machine contents can be download by:

1. Downloading and extracting a zip file; or
2. Using git to clone the GitHub repository

#### Downloading a Zip file

1. Download the contents of the following url:
[https://github.com/boundary/tsi-lab/archive/master.zip](https://github.com/boundary/tsi-lab/archive/master.zip)

2. Extract the zip file to a suitable location for use when creating your virtual machine.

#### Cloning

Use the git command line tool in a bash shell or Windows Command prompt to clone the contents of the virtual machine
in the GitHub Repository

```
$ git clone https://github.com/boundary/tsi-lab
```



### Creating and Starting the Virtual Machine

Interaction with the APIs requires the following details:

- E-mail - The e-mail associated with your TrueSight Intelligence account.
- API Token - The token generated by the system for authenticating a call to the API
- API Host - The host which the API endpoint resides

_NOTE_: To create the virtual machine you need to use a bash shell, or Windows Command prompt.

1. Change to directory of the extracted or cloned the lab contents. example:
```
$ cd tsi-lab
```
2. From the bash shell (Terminal in OSX) or Windows Command prompt.
With the TrueSight Intelligence information above issue the command below in a bash shell,
or Windows command prompt. The environment variables proceeding the `vagrant up` command are used
to configure your environment as previously mentioned.
```
$ TSP_EMAIL="<email>" TSP_API_TOKEN="<api key>" TSP_API_HOST="api.truesight-staging.bmc.com" vagrant up
```

### Checking Credentials of your Virtual Machine

Run the following command immediately after the command above to verify the settings took.
```
$ cred

Sample Output:
TSP_EMAIL=rknaub@gmail.com
TSP_API_HOST=api.truesight-staging.bmc.com
TSP_API_TOKEN=fbecec7a-b0f7-40c4-a4cb-ec09b3b6b7cb
```

### Stopping a Virtual Machine

Run the following command before shutting down you laptop/desktop.
```
$ vagrant halt
```

### Destroying a Virtual Machine

```
$ vagrant destroy
```

### Logging into the Virtual Machine
After your VM is created login to your VM by using the command below.
```
$ vagrant ssh
```

### Change directory to your labs directory
After you login to your VM CD to your labs directory by using the command below.
```
$ cd labs
```
Click Next (upper right) when completed.