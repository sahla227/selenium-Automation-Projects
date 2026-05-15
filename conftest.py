import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])


    if report.when == "call":
        driver = item.funcargs['driver']


        if report.skipped or report.failed:
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(driver,file_name )


            extras.append(pytest_html.extras.image(file_name))
            report.extras = extras




def _capture_screenshot(driver, name):
    print("take screenshot")
    driver.get_screenshot_as_file(name)