import logging
import sys

from {{cookiecutter.project_module}}.fib import fib

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)

def fibTest(data_fib) -> None:
    assert fib(data_fib[0]) == data_fib[1]
