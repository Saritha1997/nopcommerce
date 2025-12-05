from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://amazon.com")
driver.maximize_window()
print("page title is", driver.title)


# Commands to run the tests

# HTML Reports
# pytest -s -v --html reports/report.html

# Desired browser
# pytest -s -v .\test_cases\test_admin_login.py --browser firefox

# Parallel execution
# pytest -s -v .\test_cases\test_admin_login.py --browser edge -n 3

# To run the test cases which have markers (pytest)
# -m "sanity"
# -m "regression"
# -m "regression and sanity"
# -m "regression or sanity"
# pytest -s -v -m "sanity" --html .\reports\report.html .\test_cases --browser chrome