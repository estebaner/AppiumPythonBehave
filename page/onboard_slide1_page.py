from page.basepage import Base


class OnboardSlide1Page(Base):

    def __init__(self):
        super(OnboardSlide1Page, self).__init__()
        self.driver = self.base_driver

        self.next_button = {'method': 'accessibility_id', 'value': 'Siguiente'}
        self.access_button = {'method': 'accessibility_id', 'value': 'Acceder'}

    def check_onboard1_is_loaded(self):
        self.wait_for_element_visibility(self.next_button)

    def click_the_next_button(self):
        self.click_the_element(self.next_button)

    def click_the_access_button(self):
        self.click_the_element(self.access_button)
