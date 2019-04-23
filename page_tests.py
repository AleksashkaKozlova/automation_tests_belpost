# -*- coding: utf-8 -*-

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import locators


class MainTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_by_index(self, phrase="22003"):   # TODO: transfer test data to a separate document
        print("\nTest-case: search by index")
        driver = self.driver
        driver.get(locators.link_stage_farm)
        sleep(5)
        self.assertIn("stage", driver.title)
        """click Popover"""
        button_on_popover = driver.find_element_by_css_selector(locators.button_on_popover_css)
        button_on_popover.click()
        sleep(1)
        """Search OPS"""
        button_search_ops = driver.find_element_by_xpath(locators.button_search_OPS_by_xpath)
        button_search_ops.click()
        """Check on list"""
        sleep(2)
        button_list_ops = driver.find_element_by_css_selector(locators.button_list_OPS_css)
        button_list_ops.click()
        sleep(1)
        """Input research phrase"""
        input_auto_complete = driver.find_element_by_css_selector(locators.input_auto_complete_css)
        input_auto_complete.send_keys(phrase)
        sleep(1)
        input_auto_complete.send_keys(Keys.RETURN)
        assert "Почтовое отделение не найдено" not in driver.page_source
        sleep(5)

        elem3 = driver.find_elements_by_css_selector(".table-in-box tbody tr td:nth-child(1)")
        for option in elem3:
            assert phrase in option.text

    def test_autocomplete_search(self, phrase="Минск Кирова"):  # TODO: pass a string, divide it into words
        print("Test-case: autocomplete search")
        driver = self.driver
        driver.get(locators.link_search_OPS_list)
        sleep(5)
        self.assertIn("Найти отделения", driver.title)
        button_on_popover = driver.find_element_by_css_selector(locators.button_on_popover_search_OPS_css)
        button_on_popover.click()
        sleep(1)
        input_auto_complete = driver.find_element_by_css_selector(locators.input_auto_complete_css)
        input_auto_complete.send_keys(phrase)
        sleep(3)

        first_elem_drop_down = driver.find_element_by_css_selector(locators.first_elem_drop_down_css)
        first_elem_drop_down.click()
        sleep(2)
        assert "Почтовое отделение не найдено" not in driver.page_source
        sleep(3)
        index_address_ops = driver.find_element_by_xpath(locators.index_address_ops_by_xpath)
        assert "Минск" in index_address_ops.text  # TODO: transfer words from string
        assert "Кирова" in index_address_ops.text

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
