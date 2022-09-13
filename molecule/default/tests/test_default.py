import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

def test_services(host):
    assert host.service('prometheus-node-exporter').is_running
    assert host.service('prometheus-node-exporter').is_enabled
    assert not host.service('node-exporter').is_running
    assert not host.service('node-exporter').is_enabled
