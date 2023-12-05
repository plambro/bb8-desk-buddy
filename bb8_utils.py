from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color


def rgb_test(bb8):
    with SpheroEduAPI(bb8) as api:
        api.set_main_led(Color(r=255, g=0, b=0))
    return True


def head_test(bb8):
    with SpheroEduAPI(bb8) as api:
        api.spin(360, 1)
    return True