class Locators:

    first_name: str = "//input[@name='firstName']"
    last_name: str = "//input[@name='lastName']"
    phone: str = "//input[@name='phone']"
    email: str = "userName"

    address: str = "//input[@name='address1']"
    city: str = "//input[@name='city']"
    state: str = "//input[@name='state']"
    postal_code: str = "//input[@name='postalCode']"
    country_drop_down: str = "//input[@name='country']"

    user_name: str = "email"
    password: str = "//input[@name='password']"
    confirm_password: str = "//input[@name='confirmPassword']"
    submit_btn: str = "//input[@name='submit']"

    first_last_name: str = "//p[1]/font/b"
    user_name_res: str = "//p[3]/font/b"