import logging
import logging.handlers

# تنظیمات لاگ‌گیری
logging.basicConfig(level=logging.ERROR)

# تنظیمات ارسال پیغام خطا به ایمیل
email_handler = logging.handlers.SMTPHandler(
    mailhost=('smtp.example.com', 587),
    fromaddr='sender@example.com',
    toaddrs=['recipient@example.com'],
    subject='Error Log'
)
email_handler.setLevel(logging.ERROR)
logger = logging.getLogger()
logger.addHandler(email_handler)

# تنظیمات ارسال پیغام خطا به Slack
slack_handler = logging.handlers.HTTPHandler(
    'https://hooks.slack.com/services/TOKEN',
    method='POST',
    url='/your/slack/webhook/url',
    headers={'Content-Type': 'application/json'}
)
slack_handler.setLevel(logging.ERROR)
logger.addHandler(slack_handler)

def handle_error(error_message):
    print("خطا رخ داده است. لطفا بعدا تلاش کنید.")
    logger.error(error_message)

# مثال استفاده
try:
    result = 10 / 0
except ZeroDivisionError as e:
    error_message = f"خطای تقسیم بر صفر: {str(e)}"
    handle_error(error_message)