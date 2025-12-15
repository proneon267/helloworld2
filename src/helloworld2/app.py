"""
My first application
"""

import toga
from toga.style import Pack
import asyncio


class HelloWorld(toga.App):
    async def cycle_states(self, *args, **kwargs):
        for state in [*toga.constants.WindowState, toga.constants.WindowState.NORMAL]:
            self.main_window.state = state
            status_text = f"Current State: {self.main_window.state} | Current Size: {self.main_window.size}"
            self.app.widgets["status_label"].text = status_text
            print(status_text)
            await asyncio.sleep(2)
        self.app.exit()

    async def handle_enable(self, *args, **kwargs):
        await self.webview._impl.bridge.enable_bridge()

    async def handle_disable(self, *args, **kwargs):
        await self.webview.bridge.disable_bridge()

    def handle_button(self, *args, **kwargs):
        self.webview.bridge._impl.send_message("hi")

    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.webview = toga.WebView()
        self.send_button = toga.Button(text="Send", on_press=self.handle_button)
        self.enable_btn = toga.Button(text="Enable", on_press=self.handle_enable)
        self.disable_btn = toga.Button(text="Disable", on_press=self.handle_disable)

        self.main_window.content = toga.Box(
            children=[self.enable_btn, self.send_button, self.disable_btn, self.webview]
        )
        self.main_window.show()

        # asyncio.create_task(self.cycle_states())


def main():
    return HelloWorld()
