import logging
import logging.handlers

# تنظیمات لاگ‌گیری
logging.basicConfig(level=logging.ERROR)

# تنظیمات فایل لاگ برای چرخش دوره‌ای
file_handler = logging.handlers.RotatingFileHandler('error.log', maxBytes=1024, backupCount=3)
file_handler.setLevel(logging.ERROR)
logger = logging.getLogger()
logger.addHandler(file_handler)

# تنظیمات فایل لاگ برای چرخش زمانی
timed_handler = logging.handlers.TimedRotatingFileHandler('error.log', when='midnight', interval=1, backupCount=7)
timed_handler.setLevel(logging.ERROR)
logger.addHandler(timed_handler)

def handle_error(error_message):
    print("خطا رخ داده است. لطفا بعدا تلاش کنید.")
    logger.error(error_message)

# مثال استفاده
try:
    result = 10 / 0
except ZeroDivisionError as e:
    error_message = f"خطای تقسیم بر صفر: {str(e)}"
    handle_error(error_message)