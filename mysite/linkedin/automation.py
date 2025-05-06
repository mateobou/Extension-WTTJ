# linkedin/automation.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from linkedin_scraper import Person, actions
from selenium import webdriver

def get_linkedin_url_from_page(page_url):
    """Récupère le lien LinkedIn d'une page donnée"""
    options = Options()
    options.add_argument("--headless=new")  # Headless modifié pour Chrome 109+
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(page_url)
        time.sleep(3)

        element = driver.find_element(By.CSS_SELECTOR, '[data-testid="social-network-linkedin"]')
        linkedin_url = element.get_attribute("href")
        return linkedin_url
    except Exception as e:
        print(f"[Erreur] Impossible de récupérer le lien LinkedIn : {e}")
        return None
    finally:
        driver.quit()


def scrape_employees_with_arc(linkedin_url):
    """Ouvre une page LinkedIn avec l'extension Arc Instant Data Scraper pour scraper les employés"""
    arc_extension_path = "/Users/mateoboukhobza/Library/Application Support/Arc/User Data/Default/Extensions/ofaokhiedipichpaobibbnahnkdoiiah/1.2.1_0"  # 📌 à modifier avec le chemin local

    options = Options()
    options.add_argument(f"--load-extension={arc_extension_path}")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(linkedin_url)
        time.sleep(5)

        # Tu pourrais ajouter ici des clics sur les boutons de l'extension
        print("[Info] Page LinkedIn chargée, extension Arc activée.")
        return True
    except Exception as e:
        print(f"[Erreur Arc] {e}")
        return False
    finally:
        driver.quit()


def get_email_with_skrapp(linkedin_url):
    """Ouvre un profil LinkedIn et active Skrapp pour récupérer l'e-mail"""
    skrapp_extension_path = "/chemin/vers/extension/skrapp"  # 📌 à modifier avec le chemin local

    options = Options()
    options.add_argument(f"--load-extension={skrapp_extension_path}")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(linkedin_url)
        time.sleep(5)

        # Ici, tu peux ajouter des interactions avec l'extension Skrapp si elle injecte un bouton

        # En théorie, Skrapp affiche l'e-mail directement sur la page → on pourrait tenter de l'extraire :
        email_element = driver.find_element(By.XPATH, "//a[contains(@href,'mailto:')]")
        email = email_element.get_attribute("href").replace("mailto:", "")
        return email
    except Exception as e:
        print(f"[Erreur Skrapp] {e}")
        return None
    finally:
        driver.quit()

def testLinkedinScraper():
    driver = webdriver.Chrome()

    email = "some-email@email.address"
    password = "password123"
    actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
    person = Person("https://www.linkedin.com/in/joey-sham-aa2a50122", driver=driver)
    return True
