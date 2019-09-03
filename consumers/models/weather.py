"""Contains functionality related to Weather"""
import logging
import pdb

logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        #pdb.set_trace()
        logger.info("weather message")
        value = message.value()
        self.temperature = value["temperature"]
        self.status = value["status"]
        logging.info(f"temperature: {self.temperature} status: {self.status}")
        #
        #
        # TODO: Process incoming weather messages. Set the temperature and status.
        #
        #
