# import appscript
from commonFunctions.util import Utils
from appium import webdriver
import time
from commonFunctions.session_handler import Session


class ConfigSetup:
    current_config = {}

    @staticmethod #TODO: Agregar script para levantar el servidor correctamente.
    def start_appium_server():
        if not Utils.check_appium_is_already_running():
            # appscript.app('terminal').do_script('appium --address 127.0.0.1 --port 4723')
            time.sleep(4)
            print("Appium is started")
        else:
            print("Appium is already running")

    def __init__(self):
        self.driver = None

    def launch_app(self):

        platform_name = ConfigSetup.current_config['platformName']
        device_name = ConfigSetup.current_config['deviceName']
        avd = ConfigSetup.current_config['avd']
        app = ConfigSetup.current_config['app']
        app_package = ConfigSetup.current_config['appPackage']

        print("Launching app with below config, for scenario : {}".format(ConfigSetup.current_config['scenario_name']))
        print("app {0} platformName {1} platformVersion {2} deviceName {3} udid {4}".format(platform_name, device_name,
                                                                                            avd,
                                                                                            app,
                                                                                            app_package))

        dc = {
            "platformName": "{}".format(platform_name),
            "deviceName": "{}".format(device_name),
            "avd": "{}".format(avd),
            "app": "/users/usuario/Desktop/{}".format(app),
            "appPackage": "{}".format(app_package)
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dc)
        Session.session_config_instance[self.driver] = ConfigSetup.current_config

    def get_driver(self):
        return self.driver
