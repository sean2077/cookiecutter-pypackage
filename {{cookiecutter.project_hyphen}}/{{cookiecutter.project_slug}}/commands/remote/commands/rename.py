import logging

from {{ cookiecutter.project_slug }}.utils import demo_func
from pyclier import Command

log = logging.getLogger(__name__)

cmd = Command("rename", func=demo_func)
