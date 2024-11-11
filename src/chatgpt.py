import time

import clipboard
import pyautogui

from src.screen import Screen

class ChatGPT(Screen):

    def create_new_chat(self) -> None:
        pyautogui.click(
            *self.find_template_on_screenshot(self.new_chat_button_path)
        )
        time.sleep(2)

    def enter_prompt(self, prompt: str):
        pyautogui.click(
            *self.find_template_on_screenshot(self.prompt_field_path)
        )
        clipboard.copy(prompt)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.hotkey("enter")

    def get_result_from_prompt(self) -> str:
        self.find_template_on_screenshot(self.copy_button_path)
        time.sleep(1)
        pyautogui.click(
            *self.find_template_on_screenshot(self.copy_button_path)
        )
        return clipboard.paste()