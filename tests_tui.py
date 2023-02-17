from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Static


class SuiteDisplay(Static):
    """A widget to display the content of the test suite."""


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
    app = TestsTuiApp()
    app.run()
