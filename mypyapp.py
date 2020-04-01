import signal
import time
import random
import string
import logging
import os

from itrsstatsd import build_statsd
from itrsstatsd.api import Api
from itrsstatsd.units import Unit

os.environ['STATSD_SERVER'] = "localhost"
os.environ['STATSD_PORT'] = "7780"

def main():
    setup_signals()
    logger = get_logger("mypyapp")
    statsd = build_statsd(protocol='tcp')
    statsd.default_dimensions(app_name="example_app", Location="New York", component="Middleware")
    while True:
        emit_metric_or_log(statsd, logger)
        time.sleep(1)


def setup_signals():
    signal.signal(signal.SIGINT, exit_handler)
    signal.signal(signal.SIGTERM, exit_handler)
    signal.signal(signal.SIGABRT, exit_handler)


def exit_handler(signal_number, frame):
    print("Exiting due do signal {}".format(signal_number))
    exit(0)


def get_logger(name):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    formatter = logging.Formatter(fmt='%(asctime)-15s [%(threadName)s] %(levelname)s %(name)s - %(message)s')
    if not len(log.handlers):
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        log.addHandler(ch)
    return log


def emit_metric_or_log(api: Api, logger: logging.Logger):
    instruction = random.randint(0, 6)
    msg = random_str()
    api.timer("message_latency", round(random.uniform(0.5, 1.5), 6))

    if instruction == 0:
        api.increment("failed_logins")
        api.increment("failed_logins")
        api.increment("failed_logins")
    elif instruction == 1:
        api.increment("successful_logins")
        api.increment("successful_logins")
        api.increment("successful_logins")
        api.unique("unique_logins", random_str())
        api.unique("unique_logins", random_str())
        api.unique("unique_logins", random_str())
    elif instruction == 2:
        logger.error("operation %s failed", msg)
    elif instruction == 3:
        logger.info("normal %s occurred", msg)
    elif instruction == 4:
        logger.warning("approaching %s threshold", msg)
    elif instruction == 5:
        logger.debug("loop %s completed", msg)
    elif instruction == 6:
        api.gauge("message_rate", random.randint(1, 999), Unit.PerSecond)

def random_str():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))


if __name__ == "__main__":
    main()
