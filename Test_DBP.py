# Denisa F. (Discord)

import pytest

from playwright.sync_api import sync_playwright

@pytest.fixture() 
def created_page(page): 
    page.goto("https://divadlobolkapolivky.cz/")
    button = page.locator(".goout-cookie-essentials")
    button.click()
    yield page

def test_dbp_title(created_page):
     
     title = created_page.locator("title")

     assert title.inner_text() == "Divadlo Bolka Polívky"
       

def test_dbp_ShowProgram(created_page):
    
    button = created_page.get_by_role("link", name="Kompletní program zde")
    button.click()
   

def test_dbp_search(created_page):
    
    search = created_page.locator("input[name=\"q\"]")
    search.fill("DNA")
    search.press("Enter")
    
    result = created_page.get_by_role("link", name="REPRÍZA DNA")
    result.click()


def test_dbp_newsletter(created_page):

    newsletter = created_page.locator("input[name=\"mc_mv_EMAIL\"]")
    newsletter.fill("faustkova@gmail.com")
    
    gdpr = created_page.locator("input[name=\"gdpr-second\"]")
    gdpr.click()
    
    log_in = created_page.locator("input[name=\"mc_signup_submit\"]")
    log_in.click()
    


    

    
 


    
  