from selene import browser, be, have


def test_duckduckgo_should_find_selene(open_duckduckgo):
    browser.element('[name=q]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#r1-0').should(have.text('Selene: User-Oriented Web UI Browser Tests in Python - GitHub Pages'))


def test_duckduckgo_should_find_nothing(open_duckduckgo):
    browser.element('[name=q]').should(be.blank).type('blorkznak').press_enter()
    browser.element('#react-layout').should(have.text('результаты не найдены'))