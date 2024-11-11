from typing import Optional

import pyautogui
import cv2

from utils.decorators import trying_with_intervals


class Screen:
    def __init__(self):
        self.screenshot_path = "service_data/screenshot.png"

        self.new_chat_button_path = "service_data/new_chat_button.png"
        self.prompt_field_path = "service_data/prompt_field.png"
        self.copy_button_path = "service_data/copy_button.png"


    def make_screen_shot(self) -> None:
        pyautogui.screenshot(self.screenshot_path)

    @trying_with_intervals(1)
    def find_template_on_screenshot(self, path_to_image) -> Optional[tuple[int, int]]:
        self.make_screen_shot()
        image = cv2.imread(self.screenshot_path)
        template = cv2.imread(path_to_image)
        w, h = template.shape[0], template.shape[1]

        res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        __min_val, LocatedPrecision, __min_loc, Position = cv2.minMaxLoc(res)
        print(path_to_image, LocatedPrecision)
        if LocatedPrecision >= 0.9:
            return (
                Position[0] + h // 2,
                Position[1] + w // 2
            )
        return None

    


    