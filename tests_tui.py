#!/usr/bin/env python

import yaml

from textual.app import App, ComposeResult, RenderResult
from textual.containers import Container
from textual.widgets import Header, Footer, Static


def read_github_workflow_file():
    """Open the GitHub Actions Workflow file and return a YAML object"""
    github_workflow_file = '.github/workflows/ansible-test-plugins.yml'
    with open(github_workflow_file, 'r') as gh_file:
        try:
            return yaml.safe_load(gh_file)
        except yaml.YAMLError as exc:
            print(exc)


def extract_matrix_value(target, dict_yaml):
    """Extract the value of the target key from the received dictionnary"""
    for key, value in dict_yaml.items():
        if key == target:
            return value


def extract_matrix(workflow_yaml):
    """Unfold the YAML hierarchy until we reach the level containing the matrix"""
    jobs = extract_matrix_value('jobs', workflow_yaml)
    integration = extract_matrix_value('integration', jobs)
    strategy = extract_matrix_value('strategy', integration)
    matrix = extract_matrix_value('matrix', strategy)
    return matrix


class SuiteDisplay(Static):
    """A widget to display the content of the test suite."""

    def render(self) -> RenderResult:
        return "This is a test"


class Suite(Static):
    """A tests suite widget."""

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        yield SuiteDisplay()


class TestsTuiApp(App):
    """A Textual app to manage ansible tests."""

    TITLE = "Ansible Tests TUI"
    CSS_PATH = "tests_tui.css"
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("d", "toggle_dark", "Toggle dark mode")
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Container(Suite(), Suite(), Suite())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    workflow_yaml = read_github_workflow_file()
    tests_matrix_yaml = extract_matrix(workflow_yaml)
    app = TestsTuiApp()
    app.run()
