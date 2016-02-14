import os
import shutil
import pytest
from cookiecutter.main import cookiecutter

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


@pytest.fixture
def del_gen_project(request):
    def teardown():
        shutil.rmtree(os.path.join(parent_dir, 'project_name'))
    request.addfinalizer(teardown)


def test_with_default_values(del_gen_project):
    ''' Successful generation with the default values '''
    cookiecutter(parent_dir, no_input=True)
