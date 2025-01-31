# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import errno
from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call


VERSION = "0.0.0"
PLUGIN_VERSION = "0.0.0"

class InstallPluginCommand(install):
    def run(self):
        install.run(self)
        try:
            check_call(['pulumi', 'plugin', 'install', 'resource', 'cloud-toolkit-aws', PLUGIN_VERSION, '--server', 'github://api.github.com/cloud-toolkit/cloud-toolkit-aws'])
        except OSError as error:
            if error.errno == errno.ENOENT:
                print(f"""
                There was an error installing the cloud-toolkit-aws resource provider plugin.
                It looks like `pulumi` is not installed on your system.
                Please visit https://pulumi.com/ to install the Pulumi CLI.
                You may try manually installing the plugin by running
                `pulumi plugin install resource cloud-toolkit-aws {PLUGIN_VERSION}`
                """)
            else:
                raise


def readme():
    try:
        with open('README.md', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "cloud-toolkit-aws Pulumi Package - Development Version"


setup(name='cloud_toolkit_aws',
      version=VERSION,
      long_description=readme(),
      long_description_content_type='text/markdown',
      cmdclass={
          'install': InstallPluginCommand,
      },
      keywords='pulumi aws cloud-toolkit category/cloud kind/component',
      license='Apache-2.0',
      packages=find_packages(),
      package_data={
          'cloud_toolkit_aws': [
              'py.typed',
              'pulumi-plugin.json',
          ]
      },
      install_requires=[
          'parver>=0.2.1',
          'pulumi>=3.0.0,<4.0.0',
          'pulumi-aws>=5.10.0,<6.0.0',
          'pulumi-kubernetes>=3.20.2,<4.0.0',
          'pulumi-random>=4.8.2,<5.0.0',
          'semver>=2.8.1'
      ],
      zip_safe=False)
