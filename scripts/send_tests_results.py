#!/usr/bin/env python

import argparse
import requests

URL = "https://api.github.com/repos/NHSDigital/ravs-test-reports/actions/workflows/publish_report.yml/dispatches"


def get_headers():
    return {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "Authorization": f"Bearer {arguments.token}",
    }


def trigger_run():
    body = {
        "ref": "main",
        "inputs": {"run_id": run_id},
    }

    response = requests.post(
        url=URL,
        headers=get_headers(),
        json=body,
    )

    assert (
        response.status_code == 204
    ), f"Failed to trigger test run. Expected 204, got {response.status_code}\nURL: {URL} \nBody: {response.text}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--token", required=True, help="An authorised token is required"
    )
    parser.add_argument(
        "--run_id", required=True, help="The ID of the workflow Run is Required"
    )
    arguments = parser.parse_args()
    run_id = arguments.run_id

    trigger_run()
    print("Success!")
