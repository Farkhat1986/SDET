from pages.base_page import BasePage


class AddCustomer(BasePage):
    """Страница добавления клиента.

    Attributes:
        FIRST_NAME_FIELD (tuple): Локатор поля ввода имени.
        LAST_NAME_FIELD (tuple): Локатор поля ввода фамилии.
        POST_CODE_FIELD (tuple): Локатор поля ввода почтового индекса.
        ADD_CUSTOMER_SUBMIT_BTN (tuple): Локатор кнопки отправки формы добавления клиента.
    """
    FIRST_NAME_FIELD = ("xpath", "//form[@name='myForm']//input[@ng-model='fName']")
    LAST_NAME_FIELD = ("xpath", "//form[@name='myForm']//input[@ng-model='lName']")
    POST_CODE_FIELD = ("xpath", "//form[@name='myForm']//input[@ng-model='postCd']")
    ADD_CUSTOMER_SUBMIT_BTN = ("xpath", "//form[@name='myForm']//button[@type='submit']")

    def enter_first_name(self, first_name: str) -> None:
        """Вводим имя в поле First Name.

        Args:
            first_name (str): Имя клиента.
        """
        self.element_to_be_clickable(self.FIRST_NAME_FIELD).send_keys(first_name)

    def enter_last_name(self, last_name: str) -> None:
        """Вводим фамилию в поле Last Name.

        Args:
            last_name (str): Фамилия клиента.
        """
        self.element_to_be_clickable(self.LAST_NAME_FIELD).send_keys(last_name)

    def enter_post_code(self, post_code: str) -> None:
        """Вводим Post Code в поле для ввода Post Code.

        Args:
            post_code (str): Post Code.
        """
        self.element_to_be_clickable(self.POST_CODE_FIELD).send_keys(post_code)

    def click_add_customer_submit_btn(self) -> None:
        """Нажимаем на кнопку отправки формы добавления клиента."""
        self.element_to_be_clickable(self.ADD_CUSTOMER_SUBMIT_BTN).click()

    def get_alert_message(self) -> str:
        """Получаем текст сообщения из алерта."""
        self.alert_is_present()
        return self.driver.switch_to.alert.text[:-1]

    def click_alert(self) -> None:
        """Принимаем алерт."""
        self.alert_is_present()
        self.driver.switch_to.alert.accept()