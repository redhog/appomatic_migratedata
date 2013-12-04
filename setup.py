#! /usr/bin/python

from setuptools.command import easy_install
from setuptools import setup, find_packages
import shutil
import os.path
import sys
import hashlib

PKG_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_NAME = os.path.basename(PKG_DIR)

# Make it possible to overide script wrapping
old_is_python_script = easy_install.is_python_script
def is_python_script(script_text, filename):
    if 'SETUPTOOLS_DO_NOT_WRAP' in script_text:
        return False
    return old_is_python_script(script_text, filename)
easy_install.is_python_script = is_python_script

setup(
    name = "appomatic_migratedata",
    description = "Shortcut for dumpdata + loaddata to migrate larger datasets between two live databases.",
    keywords = "appomatic django database dump restore migrate",
    install_requires = ['appomaticcore'],
    version = "0.0.1",
    author = "RedHog (Egil Moeller)",
    author_email = "egil@skytruth.org",
    license = "BSD",
    url = "http://github.com/redhog/appomatic_migratedata",
    packages = find_packages(),
    package_data = {'': ['*.txt', '*.css', '*.html', '*.js']},
    include_package_data = True
)
