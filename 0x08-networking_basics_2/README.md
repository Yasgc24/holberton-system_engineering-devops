# 0x08. Networking basics #1
***

![image](https://user-images.githubusercontent.com/98331961/199248042-72200aaa-403d-4a86-b2e0-4ec3afa3db32.png)

## General
***
* What is localhost/127.0.0.1
* What is 0.0.0.0
* What is /etc/hosts
* How to display your machine’s active network interfaces

## Requeriments
***
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 20.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass Shellcheck (version 0.7.0 via apt-get) without any errors
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks
***
#### 0. Change your home IP
Write a Bash script that configures an Ubuntu server with the below requirements.
Requirements:
* localhost resolves to 127.0.0.2
* facebook.com resolves to 8.8.8.8.

#### 1. Show attached IPs
Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.
Obviously, the IPs displayed may be different depending on which machine you are running the script on.
Note that we can see our localhost IP :)

#### 2. Port listening on localhost
Write a Bash script that listens on port 98 on localhost.
