"""
{{cookiecutter.project_name}}
{{cookiecutter.project_module}}
{{cookiecutter.project_description}}
"""
# pylint: disable=C0103 # Module name "__main__" doesn't conform to camelCase naming style (invalid-name)

import logging

logging.getLogger("{{cookiecutter.project_module}}").addHandler(logging.NullHandler())
