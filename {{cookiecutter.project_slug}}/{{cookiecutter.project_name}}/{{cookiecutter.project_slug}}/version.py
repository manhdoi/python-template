import importlib_metadata as metadata

name = "{{cookiecutter.project_slug}}"

try:
    version = metadata.version(name)
except metadata.PackageNotFoundError as e:
    import logging

    logging.error(e)

    logging.warning(f"No module named {name}")
