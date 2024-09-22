import os

from {{cookiecutter.project_slug}}.utils.configuration import ApplicationConfigParser, get_config, app_name

if f"{app_name.upper()}_HOME" in os.environ:
    APP_HOME = os.getenv(f"{app_name.upper()}_HOME")
else:
    APP_HOME = None

config = ApplicationConfigParser()
config.read(get_config(APP_HOME))
