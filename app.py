from dotenv import dotenv_values

import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

config = dotenv_values(".env")
print("DOTENV Configuration", config)

sentry_sdk.init(
    dsn=config.get("SENTRY_DSN", ''),
    integrations=[
        FlaskIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

app = Flask(__name__)

@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
   app.run(debug = config.get("IN_PRODUCTION", True))