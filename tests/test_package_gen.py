"""Checks that the cookiecutter works."""

import subprocess
from pathlib import Path


def test_package_generation(
    tmp_path: Path,
    project_config: dict,
):
    """
    Creates a project cookiecutter from the template.

    Once the project is made it verifies a series of actions work.

    Args:
    ----
        tmp_path: Path
            A temporary directory path object which is unique.
        project_config: dict
            A dictionary with values for the cookiecutter template,
            as defined in the cookiecutter.json

    Note that 'tmp_path' pytest fixture is preferred over 'tmpdir'
    (see https://docs.pytest.org/en/7.3.x/how-to/tmp_path.html#the-tmpdir-and-tmpdir-factory-fixtures)
    """
    # Run cookieninja with PROJECT_SLUG for project_slug
    subprocess.run(
        [  # noqa: S607
            "cookieninja",
            ".",
            "--no-input",
            "--output-dir",
            str(tmp_path),
            f"project_slug={project_config['project_slug']}",
        ],
        shell=False,  # noqa: S603
    )

    # Check parent directory exists
    assert (tmp_path / project_config["project_slug"]).exists()

    # Check files and directories inside
    expected_files = [
        "README.md",
        ".pre-commit-config.yaml",
        "LICENCE.md",
        "pyproject.toml",
        "src",
        Path("src") / project_config["project_slug"],
        "tests",
        Path(".github"),
        Path(".github") / "workflows",
    ]
    for f in expected_files:
        assert (tmp_path / project_config["project_slug"] / f).exists()
