from behave import *
from selenium import webdriver
import XLUtils

use_step_matcher("re")
r  = 1
driver=webdriver.Chrome(executable_path="chromedriver.exe")
path = "Output.xlsx"
rows=XLUtils.getRowCount(path, "TestData")
query = XLUtils.readData(path, "TestData", r, 1)

@given("User is on Home Page")
def step_impl(context):
    driver.get("https://clinicaltrials.gov/ct2/home")
    print(driver.title)
    print("User successfully lands on Home Page")


@when("User does not enter any key and click Search")
def step_impl(context):
    driver.find_element_by_xpath("//*[@id='MainForm']/fieldset/div[7]/div/input").click()



@then("User navigates to results page displaying all results")
def step_impl(context):
    print("Showing all results")


@when("User enters key and click Search")
def step_impl(context):
    driver.find_element_by_id("home-search-condition-query").send_keys("brain")       #sending keys
    driver.find_element_by_xpath("//*[@id='MainForm']/fieldset/div[7]/div/input").click()       #clicking search
    print(driver.title)
    print("Search button working successfully")
    driver.find_element_by_link_text("Home").click()


@then("User navigates to results page and fetch trails")
def step_impl(context):
    driver.maximize_window()
    for r in range(1, rows+1):
        query = XLUtils.readData(path, "TestData", r, 1)            #reading input data from file
        driver.find_element_by_id("home-search-condition-query").send_keys(query)       #sending keys
        driver.find_element_by_xpath("//*[@id='MainForm']/fieldset/div[7]/div/input").click()       #clicking search
        XLUtils.createSheet(path, query)        #creating sheet if not already present
        XLUtils.writeData(path, query, 1, 1, 'Study Title')     #Creating headings for every new sheet
        XLUtils.writeData(path, query, 1, 2, 'Conditions')      #Creating headings for every new sheet
        XLUtils.writeData(path, query, 1, 3, 'Interventions')   #Creating headings for every new sheet
        XLUtils.writeData(path, query, 1, 4, 'Locations')       #Creating headings for every new sheet
        #fetching data from webelent (table) and writting in newly created sheets respectively
        for i in range(1, 11):
            for j in range(4, 8):
                data = driver.find_element_by_css_selector("#theDataTable > tbody > tr:nth-child(" + str(i) + ") > td:nth-child(" + str(j) + ")").text
                XLUtils.writeData(path, query, i+1, j-3, data)
        driver.find_element_by_link_text("Home").click()        #coming back to home page to enter new input data

    driver.close()


