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

def push(message):
    print("=" * 60)
    print("Agentic IAM Lab Push")
    print("=" * 60)

    subprocess.run(
        [
            "git",
            "add",
            "."
        ]
    )

    subprocess.run(
        [
            "git",
            "commit",
            "-m",
            message
        ]
    )

    result=subprocess.run(
        [
            "git",
            "push"
        ], 
        capture_output=True, 
        text=True, 
        check=True,
        timeout=10
    )

    print("✓ Git Pushed")
    print("=" * 60)
    print(f"✓ {result}")
    print(f"✓ {result.stdout}")
    print("=" * 60)



def pull():
  print("=" * 60)
  print("Agentic IAM Lab Pull")
  print("=" * 60)  

  result=subprocess.run(
        [
            "git",
            "pull"
        ], 
        capture_output=True, 
        text=True, 
        check=True,
        timeout=10
    )

  print("✓ Git Pulled")
  print("=" * 60)
  print(f"✓ {result}")
  print(f"✓ {result.stdout}")
  print("=" * 60)

