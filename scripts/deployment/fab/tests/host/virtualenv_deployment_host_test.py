#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import mox, os

from testing.helpers.execution import TestSuiteLoader, TestRunner

from fab.config.rsr.virtualenv import RSRVirtualEnvInstallerConfig
from fab.environment.python.virtualenv import VirtualEnvInstaller
from fab.helpers.feedback import ExecutionFeedback
from fab.host.controller import LocalHostController, RemoteHostController
from fab.host.virtualenv import VirtualEnvDeploymentHost
from fab.os.filesystem import FileSystem


class VirtualEnvDeploymentHostTest(mox.MoxTestBase):

    def setUp(self):
        super(VirtualEnvDeploymentHostTest, self).setUp()
        self.mock_file_system = self.mox.CreateMock(FileSystem)
        self.mock_virtualenv_installer = self.mox.CreateMock(VirtualEnvInstaller)
        self.mock_feedback = self.mox.CreateMock(ExecutionFeedback)

        self.expected_virtualenvs_home = "/some/path/to/virtualenvs"
        # we don't have any additional expections on the AkvoPermission and Internet dependencies (since
        # those are already tested in the DeploymentHost base class) so we set these to None for now
        self.virtualenv_deployment_host = VirtualEnvDeploymentHost(self.expected_virtualenvs_home, self.mock_file_system,
                                                                   None, None, self.mock_virtualenv_installer, self.mock_feedback)

    def test_can_create_a_remote_host_instance(self):
        """fab.tests.host.virtualenv_deployment_host_test  Can create a remote VirtualEnvDeploymentHost instance"""

        host_instance = self._create_host_instance_with(RemoteHostController)

        self.assertIsInstance(host_instance, VirtualEnvDeploymentHost)

    def test_can_create_a_local_host_instance(self):
        """fab.tests.host.virtualenv_deployment_host_test  Can create a local VirtualEnvDeploymentHost instance"""

        host_instance = self._create_host_instance_with(LocalHostController)

        self.assertIsInstance(host_instance, VirtualEnvDeploymentHost)

    def _create_host_instance_with(self, host_controller_class):
        mock_virtualenv_installer_config = self.mox.CreateMock(RSRVirtualEnvInstallerConfig)
        mock_virtualenv_installer_config.virtualenvs_home = self.expected_virtualenvs_home
        mock_virtualenv_installer_config.rsr_env_path = os.path.join(self.expected_virtualenvs_home, "rsr_env")
        mock_host_controller = self.mox.CreateMock(host_controller_class)
        mock_host_controller.feedback = self.mox.CreateMock(ExecutionFeedback)

        self.mox.ReplayAll()

        return VirtualEnvDeploymentHost.create_instance(mock_virtualenv_installer_config, mock_host_controller)

    def test_can_create_empty_virtualenv(self):
        """fab.tests.host.virtualenv_deployment_host_test  Can create empty virtualenv"""

        self._set_expectations_to_ensure_virtualenvs_home_exists()
        self.mock_virtualenv_installer.create_empty_virtualenv()
        self.mox.ReplayAll()

        self.virtualenv_deployment_host.create_empty_virtualenv()

    def test_can_ensure_virtualenv_exists(self):
        """fab.tests.host.virtualenv_deployment_host_test  Can ensure virtualenv exists"""

        self._set_expectations_to_ensure_virtualenvs_home_exists()
        self.mock_virtualenv_installer.ensure_virtualenv_exists()
        self.mox.ReplayAll()

        self.virtualenv_deployment_host.ensure_virtualenv_exists()

    def _set_expectations_to_ensure_virtualenvs_home_exists(self):

        self.mock_file_system.directory_exists(self.expected_virtualenvs_home).AndReturn(True)
        self.mock_feedback.comment("Found expected directory: %s" % self.expected_virtualenvs_home)

    def test_can_install_virtualenv_packages(self):
        """fab.tests.host.virtualenv_deployment_host_test  Can install virtualenv packages"""

        expected_pip_requirements_file = "/some/pip/requirements.txt"

        self.mock_virtualenv_installer.install_packages(expected_pip_requirements_file)
        self.mox.ReplayAll()

        self.virtualenv_deployment_host.install_virtualenv_packages(expected_pip_requirements_file)


def suite():
    return TestSuiteLoader().load_tests_from(VirtualEnvDeploymentHostTest)

if __name__ == "__main__":
    from fab.tests.test_settings import TEST_MODE
    TestRunner(TEST_MODE).run_test_suite(suite())