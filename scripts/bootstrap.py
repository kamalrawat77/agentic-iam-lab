import os
import subprocess

from scripts.config import (
    get_github_token
)


def bootstrap():

    print("=" * 60)
    print("Agentic IAM Lab Bootstrap")
    print("=" * 60)

    token = get_github_token()

    subprocess.run(
        [
            "git",
            "config",
            "--global",
            "user.name",
            "Kamal Rawat"
        ]
    )

    subprocess.run(
        [
            "git",
            "config",
            "--global",
            "user.email",
            "YOUR_GITHUB_EMAIL"
        ]
    )

    subprocess.run(
        [
            "git",
            "remote",
            "set-url",
            "origin",
            f"https://kamalrawat77:{token}@github.com/kamalrawat77/agentic-iam-lab.git"
        ]
    )

    print("✓ Git configured")
    print("✓ Secrets loaded")
    print("✓ Bootstrap complete")
