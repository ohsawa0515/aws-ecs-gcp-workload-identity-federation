from setuptools import setup

NAME = 'aws-ecs-gcp-workload-identity-federation'
VERSION = '0.0.1'
DESCRIPTION = "aws-ecs-gcp-workload-identity-federation: This package solves Amazon ECS credential issues with AWS and GCP Workload Identity Federation."
AUTHOR = 'Shuichi Ohsawa'
AUTHOR_EMAIL = 'ohsawa0515@gmail.com'
URL = 'https://github.com/ohsawa0515/aws-ecs-gcp-workload-identity-federation'
DOWNLOAD_URL = 'https://github.com/ohsawa0515/aws-ecs-gcp-workload-identity-federation'
LICENSE = 'MIT'
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [
    'requests',
]

PACKAGES = [
    'aws_ecs_gcp_workload_identity'
]

CLASSIFIERS = [
    "License :: OSI Approved :: MIT License",
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3 :: Only',
]

with open("README.md", "r", encoding="utf-8") as fp:
    readme = fp.read()
LONG_DESCRIPTION = readme
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"

setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      packages=PACKAGES,
      classifiers=CLASSIFIERS
      )
