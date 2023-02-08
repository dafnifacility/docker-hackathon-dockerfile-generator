import os
import pathlib
import shutil
import subprocess as sp

import jinja2

from . import parse_model_definition as parser


def env_config():
    """Get configuration passed to docker container by environment variables."""
    git_url = os.environ.get("GIT_URL")
    access_token = os.environ.get("ACCESS_TOKEN", None)
    subfolder = os.environ.get("SUBFOLDER", None)
    config_path = os.environ.get("MODEL_DEFINITION", "model_definition.yaml")

    return {
        "git_url": git_url,
        "access_token": access_token,
        "subfolder": subfolder,
        "config_path": config_path,
    }


def main():
    config = env_config()

    ## Call script to clone git repo.
    if config.get("subfolder", False):
        sp.check_call(
            ["git", "clone", config["git_url"], "/data/clone", "--depth", "1"]
        )
        shutil.move(f"/data/clone/{config['subfolder']}", "/data/source")
    else:
        sp.check_call(
            ["git", "clone", config["git_url"], "/data/source", "--depth", "1"]
        )

    ## Get the configuration
    model_config = parser.parse_full(
        pathlib.Path("/data/source/") / config["config_path"]
    )

    ## Choose correct dockerfile template.
    template_env = jinja2.Environment(
        loader=jinja2.PackageLoader("dockerfile_generator", "templates"),
        autoescape=False,
    )
    template = template_env.get_template(f"{config['language']}.jinja")

    # Render template with vars and write out.
    template.stream(**model_config).dump("/data/Dockerfile")


if __name__ == "__main__":
    main()
