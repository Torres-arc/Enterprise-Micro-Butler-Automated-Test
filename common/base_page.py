# -*-coding:utf-8 -*-
import json
import os
import sys
import time

from pathlib import Path
from time import sleep
from unittest import TestCase

from BeautifulReport import BeautifulReport
from BeautifulReport.BeautifulReport import HTML_IMG_TEMPLATE
from PIL import ImageDraw, Image
from pymouse import PyMouse
from pykeyboard.windows import PyKeyboard
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# from common.log import log

class BasePage(object):
    def __init__(self, selenium_driver):
        self.driver = selenium_driver