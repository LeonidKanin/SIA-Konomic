from selenium.webdriver.common.by import By


class RegisterLocators:
    Remote_Component = (By.CSS_SELECTOR, ".remoteComponent")
    Title_Form = (By.CSS_SELECTOR, "h5")
    Name_Input = (By.CSS_SELECTOR, "div[data-wi = 'user-name'] input")
    Error_Name_Input = (By.CSS_SELECTOR, "div[data-wi = 'user-name'] div.v-text-field__details span")
    Mail_Input = (By.CSS_SELECTOR, "#username")
    Error_Mail_Input = (By.CSS_SELECTOR, "div[data-wi = 'identificator'] div.v-text-field__details span")
    Pass_Input = (By.CSS_SELECTOR, "#new-password")
    Pass_Viewing = (By.CSS_SELECTOR, "div[data-wi = 'preview-button'] > button")
    Error_Pass_Input = (By.CSS_SELECTOR, "div[data-wi = 'password'] div[data-wi = 'error'] span")
    Referral_Input = (By.CSS_SELECTOR, "div[data-wi = 'referral'] input")
    Error_Referral_Input = (By.CSS_SELECTOR, "div[data-wi = 'referral'] div.v-text-field__details span")
    Checkbox_Agreement = (By.CSS_SELECTOR, "div[data-wi ='user-agreement'] input")
    Submit_Btn = (By.CSS_SELECTOR, "div[data-wi ='submit-button'] > button")
    Captcha = (By.CSS_SELECTOR, "div[aria-hidden ='true']")
