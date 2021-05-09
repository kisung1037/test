# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.define "ansible-server" do |cfg|
    config.vm.box = "centos/7"
    cfg.vm.provider "virtualbox" do |vb|
      vb.name = "Ansible_server(github_SysNet4Admin)"
    end
    cfg.vm.host_name = "ansible-server"
    cfg.vm.network "public_network" , ip: "192.168.0.200"
    cfg.vm.network "forwarded_port", guest: 22, host: 60010, auto_crrect: true, id: "ssh"
    cfg.vm.synced_folder "../data" , "/vagrant", disabled: true
    cfg.vm.provision "shell", inline: "yum install epel-release -y"
    cfg.vm.provision "shell", inline: "yum install ansible -y"
    cfg.vm.provision "file", source: "ansible_env_ready.yml",
      destination: "ansible_env_ready.yml"
    cfg.vm.provision "shell", inline: "ansible-playbook ansible_env_ready.yml"
  end
end
