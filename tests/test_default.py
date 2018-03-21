import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_docker_service(host):
    s = host.service('docker')

    assert s.is_enabled
    assert s.is_running


def test_docker_helloworld(host):
    with host.sudo():
        c = host.run("docker run hello-world")
        assert c.rc == 0
