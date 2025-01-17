"""
jupyterlab-snippets setup
"""
import json
from pathlib import Path

import setuptools

HERE = Path(__file__).parent.resolve()

# The name of the project
NAME = "jupyterlab-snippets"
PY_NAME = NAME.replace('-', '_')

lab_path = (HERE / PY_NAME / "labextension")

# Representative files that should exist after a successful build
ensured_targets = [
    str(lab_path / "package.json"),
    str(lab_path / "static/style.js")
]

data_files_spec = [
    ("share/jupyter/labextensions/%s" % NAME, str(lab_path), "**"),
    ("share/jupyter/labextensions/%s" % NAME, str(HERE), "install.json"),
    ("etc/jupyter/jupyter_notebook_config.d", "jupyter-config/jupyter_notebook_config.d", "jupyterlab_snippets.json"),
    ("etc/jupyter/jupyter_server_config.d", "jupyter-config/jupyter_server_config.d", "jupyterlab_snippets.json"),
]

long_description = (HERE / "README.md").read_text()

# Get the package info from package.json
pkg_json = json.loads((HERE / "package.json").read_bytes())

setup_args = dict(
    name=NAME,
    version=pkg_json["version"],
    url=pkg_json["homepage"],
    author=pkg_json["author"]["name"],
    author_email=pkg_json["author"]["email"],
    description=pkg_json["description"],
    license=pkg_json["license"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    zip_safe=False,
    include_package_data=True,
    python_requires=">=3.6",
    platforms="Linux, Mac OS X, Windows",
    keywords=["Jupyter", "JupyterLab", "JupyterLab3"],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Jupyter",
        "Framework :: Jupyter :: JupyterLab",
        "Framework :: Jupyter :: JupyterLab :: 3",
        "Framework :: Jupyter :: JupyterLab :: Extensions",
        "Framework :: Jupyter :: JupyterLab :: Extensions :: Prebuilt",
    ],
)

try:
    from jupyter_packaging import (
        wrap_installers,
        npm_builder,
        get_data_files
    )
    post_develop = npm_builder(
        build_cmd="build:prod", source_dir="src", build_dir=lab_path
    )
    setup_args['cmdclass'] = wrap_installers(post_develop=post_develop, ensured_targets=ensured_targets)
    setup_args['data_files'] = get_data_files(data_files_spec)
except ImportError as e:
    pass

if __name__ == "__main__":
    setuptools.setup(**setup_args)
