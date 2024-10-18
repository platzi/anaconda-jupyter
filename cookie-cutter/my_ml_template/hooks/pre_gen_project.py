import sys

project_name = '{{ cookiecutter.project_name }}'

if ' ' in project_name:
    print('Error: Project name should not contain spaces')
    sys.exit(1)