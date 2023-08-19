import logging

logging.basicConfig(filename='error.log', level=logging.ERROR)
# تعیین فرمت لاگ
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
# ایجاد هندلر لاگ
file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
# ایجاد یک لاگر
logger = logging.getLogger()
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def handle_error(error_message):
    print("خطا رخ داده است. لطفا بعدا تلاش کنید.")
    logger.error(error_message)

# مثال استفاده
try:
    result = 10 / 0
except ZeroDivisionError as e:
    error_message = f"خطای تقسیم بر صفر: {str(e)}"
    handle_error(error_message)

# نمونه استفاده دیگر از لاگ
logger.debug('این یک پیغام DEBUG است.')
logger.info('این یک پیغام INFO است.')
logger.warning('این یک پیغام WARNING است.')
logger.error('این یک پیغام ERROR است.')