import os
import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
  os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def packages(distro, release):
    listfile_name = "list-" + distro + '-' + release + ".txt"
    listfile = open(listfile_name, "r")
    packages = listfile.read().splitlines()
    return packages


@pytest.mark.parametrize("name", open("packages.txt","r").read().splitlines())
def test_packages(host, name):
  assert host.package(name).is_installed