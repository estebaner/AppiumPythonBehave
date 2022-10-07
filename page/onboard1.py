from page.basepage import Base


class Onboard1(Base):

    def __init__(self):
        super(Onboard1, self).__init__()
        self.driver = self.base_driver

        self.next_button = {'method': 'accessibility_id', 'value': 'Siguiente'}

    def check_onboard1_is_loaded(self):
        self.wait_for_element_visibility(self.next_button)

    def click_the_compute_sum_button(self):
        self.click_the_element(self.next_button)
