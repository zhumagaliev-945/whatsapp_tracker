from .enums import Browsers
from .enums import Status
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from PIL import Image
from io import BytesIO
import os
import time
import ast


class WhatsappClient:

    def __init__(self):
        pass

    def connect(self) -> bool:
        pass

    def minimize_window(self):
        pass

    def maximize_window(self):
        pass

    def is_logged(self) -> bool:
        pass

    def save_qrcode(self, file_name: str) -> bool:
        pass

    def save_header(self, file_name: str) -> bool:
        pass

    def get_header(self) -> bool:
        pass

    def open_chat(self, target: str) -> bool:
        pass

    def get_user_status(self, target: str) -> bool:
        pass

    def send_message(self, target, message: str) -> bool:
        pass

    def __get_img_by_variable(self, variable_name: str) -> str:
        pass

    def __get_xpath(self, file_name: str) -> str:
        pass