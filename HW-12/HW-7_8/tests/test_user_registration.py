from RegistrationPage import RegistrationPage
import allure


@allure.title("Проверка регистрации нового пользователя")
def test_registration(driver, base_url):
    page = RegistrationPage(driver, base_url)
    page.go_to_registration_page()

    page.fill_personal_details("user", "user", "email@mail.ru", "+79999")
    page.fill_passwords("pass")
    page.fill_agreement()

    page.confirm()

    with allure.step("Проверка изменения тайтла страницы после регистрации"):
        assert page.wait_title("Your Account Has Been Created!")

