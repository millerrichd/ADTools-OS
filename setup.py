from distutils.core import setup

setup(
  name = 'adtools',
  packages = ['adtools'],
  version = '0.2',
  description = 'Active Directory toolset, including keytab generation',
  author = "Steven O'Donnell - Locked Versions, Richard Miller",
  author_email = 'developer@steven.io - Locked Versions, rmiller@lytx.com',
  url = 'http://dctfs4:8080/tfs/Lytx/_git/ADTools',
  download_url = 'https://github.com/stevenwoah/adtools/archive/0.2.tar.gz',
  keywords = ['kerberos', 'keytab', 'gssapi', 'ldap', 'openldap', 'active', 'directory', 'ad', 'tools'],
  license = 'MIT',
  classifiers = [
      'Development Status :: 3 - Alpha',
      'Environment :: Console',
      'Intended Audience :: System Administrators',
      'License :: OSI Approved :: MIT License',
      'Operating System :: MacOS :: MacOS X',
      'Operating System :: POSIX :: Linux',
      'Programming Language :: Python :: 2',
      'Topic :: System :: Systems Administration',
      'Topic :: System :: Systems Administration :: Authentication/Directory'
    ],
  scripts = [
    "bin/adtools-join",
    ],
  install_requires = [
    "pycrypto == 2.6.1",
    "python-ldap == 2.4.45",
    "kerberos == 1.2.5",
    ],
)
