import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import pytest_html


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Block ads and popup windows from hanging page load
    options.add_argument("--disable-popup-blocking")
    
    # Crucial: 'eager' tells Selenium to proceed as soon as HTML/DOM is ready, 
    # without waiting for heavy external ad images/scripts to finish loading
    options.page_load_strategy = 'eager'

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(10)
    
    yield driver
    
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            if not os.path.exists("reports/screenshots"):
                os.makedirs("reports/screenshots")
            
            screenshot = driver.get_screenshot_as_png()
            screenshot_path = f"reports/screenshots/{item.name}.png"
            
            with open(screenshot_path, "wb") as f:
                f.write(screenshot)
            
            import base64
            screenshot_b64 = base64.b64encode(screenshot).decode('utf-8')
            
            report.extras = getattr(report, "extras", [])
            report.extras.append(pytest_html.extras.image(screenshot_b64))
