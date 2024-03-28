# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
Apply some defaults and minor modifications to the jobs defined in the build
kind to run https://github.com/mozilla/addons-linter.
"""


import os

from taskgraph.transforms.base import TransformSequence
from taskgraph.util.schema import resolve_keyed_by
from taskgraph.util.keyed_by import evaluate_keyed_by


transforms = TransformSequence()


@transforms.add
def run_addons_linter(config, tasks):
    for task in tasks:
        # We only want to execute addons-linter on privileged extensions (for now).
        if os.environ.get("XPI_SIGNING_TYPE") != "privileged":
            continue

        dep = task.pop("primary-dependency")

        # Add a dependency to the build task because we want to lint the
        # generated XPI.
        task["dependencies"] = {"build": dep.label}

        artifact_prefix = dep.task["payload"]["env"]["ARTIFACT_PREFIX"].rstrip("/")
        xpi_name = dep.task["extra"]["xpi-name"]
        xpi_file = f"{xpi_name}.xpi"

        # Set task label.
        task["label"] = f"linter-{xpi_name}"

        # Replace variables in the `command` to execute. We use an `env`
        # variable for the `XPI_URL` to leverage `artifact-reference`.
        env = task.setdefault("worker", {}).setdefault("env", {})

        env["XPI_URL"] = {"artifact-reference": f"<build/{artifact_prefix}/{xpi_file}>"}
        run = task["run"]
        run["command"] = run["command"].format(xpi_file=xpi_file)

        yield task
