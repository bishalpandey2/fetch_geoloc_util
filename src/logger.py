import logging

# Let's set up our logger - nothing fancy, just the basics
logging.basicConfig(
    level=logging.DEBUG,  # We want all the details, so DEBUG it is
    format='%(asctime)s - %(levelname)s - %(message)s'  # Time, level, and what happened
)

# Grab our logger - we'll use this to log stuff
logger = logging.getLogger(__name__)