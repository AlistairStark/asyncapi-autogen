isort asyncapi_autogen/
black asyncapi_autogen/
flake8 asyncapi_autogen/
autoflake --in-place --remove-all-unused-imports --remove-unused-variables --recursive asyncapi_autogen/
mypy asyncapi_autogen/