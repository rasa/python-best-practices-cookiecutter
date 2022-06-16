"""
{{cookiecutter.project_name}}
{{cookiecutter.project_module}}
{{cookiecutter.project_description}}
"""

import logging

logging.getLogger("{{cookiecutter.project_module}}").addHandler(logging.NullHandler())
