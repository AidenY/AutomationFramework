import datetime
import io

from .logger import AutoLogger

default_try_timeout = 0.4
default_timeout = 30
max_timeout = 90

action_click = '点击'
action_sendkeys = '输入'
action_select = '选择'
action_wait_element_display = '等待元素显示'

# Screenshot
log_screenshot_folder = "result/screenshot_" + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
log_capture_string = io.StringIO()


def reset_log_capture_string():
    print("Result Log")
    global log_capture_string
    log_capture_string.close()
    log_capture_string = io.StringIO()


