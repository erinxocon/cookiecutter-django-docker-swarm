#!/usr/bin/env python
import os
import sys

from pathlib import Path

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local_settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    APPS_DIR = Path(__file__) / "{{cookiecutter.project_slug}}"
    sys.path.append(str(APPS_DIR))
    execute_from_command_line(sys.argv)