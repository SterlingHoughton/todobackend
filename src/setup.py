from setuptools import setup, find_packages

setup (
  name = "todobackend",
  version = "0.1.0",
  description = "Todobackend Django REST service",
  packages = find_packages(),
  include_package_data = True,
  scripts = ["manage.py"],
  install_requires =      ["astroid>=1.5.3",
                           "backports.functools-lru-cache>=1.4",
                           "configparser>=3.5.0",
                           "Django>=1.9",
                           "django-cors-headers>=1.1.0",
                           "djangorestframework>=3.3.0",
                           "enum34>=1.1.6",
                           "isort>=4.2.15",
                           "lazy-object-proxy>=1.3.1",
                           "mccabe>=0.6.1",
                           "MySQL-python>=1.2.5",
                           "pylint>=1.7.2",
                           "singledispatch>=3.4.0.3",
                           "six>=1.10.0",
                           "wrapt>=1.10.11",
                           "uwsgi>=2.0"],
  extras_require = {
                     "test": [
                       "colorama>=0.3.9",
                       "coverage>=4.4.1",
                       "django-nose>=1.4.4",
                       "nose>=1.3.7",
                       "pinocchio>=0.4.2"
                     ]
                   }
)
