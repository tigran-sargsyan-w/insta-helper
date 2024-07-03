###############################################################################
# Note:
# Update the XPath expressions with a generic structure to ensure robustness, avoiding specific paths like
# "/html/body/div[2]/div/div[2]/div[1]/div[2]", which may break if the DOM structure changes after updates.
#
# Absolute paths: These provide a direct location for an element, starting with "/html" for example.
# Relative paths: Begin with "//", allowing searches from any point in the DOM, such as "//div[@class='form-group']".
###############################################################################

xpath = {}

xpath["cookies"] = {
    "allow_button": "//button[contains(@class, '_a9--') and contains(text(), 'Allow')]",
    "decline_button": "//button[contains(@class, '_a9--') and contains(text(), 'Decline')]",
}

xpath["login"] = {
    "username": "//input[@name='username']",
    "password": "//input[@name='password']",
    "incorrect_password": "//div[contains(text(), 'password was incorrect')]",
}
