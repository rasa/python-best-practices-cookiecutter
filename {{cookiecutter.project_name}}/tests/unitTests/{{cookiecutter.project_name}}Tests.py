""" tests/unitTests/{{cookiecutter.project_name}}Tests.py """
# pylint: disable=C0103 # Module name "{{cookiecutter.project_name}}Tests" doesn't conform to camelCase naming style (invalid-name)
# pylint: disable=E0401 # Unable to import '{{cookiecutter.project_module}}' (import-error)
import logging
import sys

from {{cookiecutter.project_module}}.fib import fibx

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)

def fibTest(data_fib) -> None:
    assert fibx(data_fib[0]) == data_fib[1]
