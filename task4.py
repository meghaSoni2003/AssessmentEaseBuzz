import re

import pytest
from playwright.sync_api import Dialog, Page, expect

BaseURL = "https://rahulshettyacademy.com/AutomationPractice/"


@pytest.fixture(autouse=True)
def open_practice_page(page: Page):
    page.goto(BaseURL)
    expect(page.get_by_role("heading", name="Practice Page")).to_be_visible()


# ** radio buttons **
def test_radio_button_selection(page: Page):
    radio2 = page.locator("input[value='radio2']")
    radio2.check()
    expect(radio2).to_be_checked()
    expect(page.locator("input[value='radio1']")).not_to_be_checked()
    expect(page.locator("input[value='radio3']")).not_to_be_checked()

# ** dropdown **
@pytest.mark.parametrize("value", ["option1", "option2", "option3"])
def test_static_dropdown(page: Page, value: str):
    dropdown = page.locator("#dropdown-class-example")
    dropdown.select_option(value)
    expect(dropdown).to_have_value(value)

# ** show / hide **
def test_hide_and_show_textbox(page: Page):
    textbox = page.locator("#displayed-text")
    expect(textbox).to_be_visible()

    page.locator("#hide-textbox").click()
    expect(textbox).to_be_hidden()

    page.locator("#show-textbox").click()
    expect(textbox).to_be_visible()


# ** alert dialog and confirm **
def test_alert_contains_entered_name(page: Page):
    messages: list[str] = []

    def handle(dialog: Dialog):
        messages.append(dialog.message)
        dialog.accept()

    page.once("dialog", handle)
    page.locator("#name").fill("Megha")
    page.locator("#alertbtn").click()

    assert messages and "Megha" in messages[0]


def test_confirm_dialog_dismiss(page: Page):
    dialog_types: list[str] = []

    def handle(dialog: Dialog):
        dialog_types.append(dialog.type)
        dialog.dismiss()

    page.once("dialog", handle)
    page.locator("#name").fill("Megha")
    page.locator("#confirmbtn").click()

    assert dialog_types == ["confirm"]

# ** new tab / popup **
def test_open_tab_opens_new_page(page: Page):
    with page.expect_popup() as popup_info:
        page.locator("#opentab").click()
    new_tab = popup_info.value
    new_tab.wait_for_load_state("domcontentloaded")

    assert new_tab.url.startswith("http")
    assert new_tab.url != page.url
    assert len(page.context.pages) == 2
    new_tab.close()

