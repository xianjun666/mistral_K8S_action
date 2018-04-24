from mistral.actions import base
from oslo_concurrency import processutils

class K8sAction(base.Action):

    def __init__(self, hosts, module=None, node=None, deploy=None, get=None):

        '''self.hosts = hosts'''
        self.get = get
        self.module = module
        self.node = node
        self.deploy = deploy

    def run(self):

        '''command1 = ['k8s', self.hosts, ]'''
        command2 = ['k8s-get', self.get]

        if self.module:
            command2.extend(['cluster-info', self.module])

        if self.node:
            command2.extend(['node', self.node])

        if self.deploy:
            command2.extend(['deploy', self.deploy])

        stderr, stdout = processutils.execute(
            *command2, log_errors=processutils.LogErrors.ALL)
        return {"stderr": stderr, "stdout": stdout}
