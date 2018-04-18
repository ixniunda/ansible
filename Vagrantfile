# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box_check_update = false
  config.vm.define "fedora26" do |fedora26|
    fedora26.vm.box = "hashicorp/precise32"
    fedora26.vm.network  "forwarded_port", guest: 80, host: 9900
    fedora26.vm.network  "forwarded_port", guest: 22, host: 9999
    fedora26.vm.provider "virtualbox" do |vb|
      vb.name = "nginx_tom"
    end
  end
end

