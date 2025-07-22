import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Upwork credentials
email = "fnaticop786@gmail.com"
password = "fnatic111"

# Categories and keywords
categories = {
    "Web Development": "web development",
    "AI": "artificial intelligence",
    "ML": "machine learning"
}

# Setup undetected Chrome
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 20)

def human_scroll():
    """Scroll slowly like a human to load React job tiles."""
    total_height = driver.execute_script("return document.body.scrollHeight")
    for y in range(0, total_height, random.randint(300, 500)):
        driver.execute_script(f"window.scrollTo(0, {y});")
        time.sleep(random.uniform(0.7, 1.2))

def login_upwork():
    print("Logging into Upwork...")
    driver.get("https://www.upwork.com/ab/account-security/login")
    wait.until(EC.presence_of_element_located((By.ID, "login_username")))

    driver.find_element(By.ID, "login_username").send_keys(email)
    driver.find_element(By.ID, "login_password_continue").click()
    wait.until(EC.presence_of_element_located((By.ID, "login_password")))
    driver.find_element(By.ID, "login_password").send_keys(password)
    driver.find_element(By.ID, "login_control_continue").click()
    time.sleep(5)

def scrape_category(category_name, search_term, limit=5):
    print(f"\n==== {category_name} Projects ====")
    search_url = f"https://www.upwork.com/nx/jobs/search/?q={search_term.replace(' ', '+')}"
    driver.get(search_url)
    time.sleep(6)  # Give React some time

    human_scroll()
    time.sleep(3)  # Let all jobs load

    try:
        # Correct selector for Upwork job cards (2025)
        job_cards = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div[data-test='job-tile-list'] article")
            )
        )
    except:
        print("No jobs found or page blocked.")
        return

    if not job_cards:
        print("No jobs found.")
        return

    print(f"Found {len(job_cards)} jobs. Extracting top {limit}...\n")
    for job in job_cards[:limit]:
        try:
            title = job.find_element(By.CSS_SELECTOR, "h4 a").text
            link = job.find_element(By.CSS_SELECTOR, "h4 a").get_attribute("href")
            summary_elem = job.find_elements(By.CSS_SELECTOR, "span[data-test='job-description-text']")
            summary = summary_elem[0].text if summary_elem else "No summary found."
            print(f"Title: {title}")
            print(f"Link: {link}")
            print(f"Summary: {summary[:200]}...")
            print("=" * 50)
        except Exception as e:
            print(f"Error extracting job: {e}")

# Main script
try:
    login_upwork()
    for name, keyword in categories.items():
        scrape_category(name, keyword)
finally:
    print("Closing browser...")
    driver.quit()
