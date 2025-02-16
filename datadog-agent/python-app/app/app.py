from flask import Flask
import logging
from ddtrace import tracer, patch_all

# Enable Datadog tracing
patch_all()

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def hello():
    logger.info("Hello endpoint was hit!")
    return "Hello, Datadog!"

@app.route('/status')
def status():
    return {"status": "running"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
