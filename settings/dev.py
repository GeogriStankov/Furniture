from base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_wjNPTQXilOB1sDUyIYtBCM86')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_v4yOXsBlRs9W2ccALtOy5U8L')

# Paypal environment variables
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'http://a6ddeb18.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'stankov.test.acc@gmail.com'