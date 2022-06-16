""" tests/unit_tests/{{cookiecutter.project_name}}_tests.py """
import logging
import sys

from {{cookiecutter.project_module}}.fib import fibx

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)


def test_fib(data_fib) -> None:
    """test_fib"""
    assert fibx(data_fib[0]) == data_fib[1]
