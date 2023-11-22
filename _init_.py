init_py:
from typing import List
import logging
import azure.functions as func

def main(events: List[func.EventHubEvent]):
    for event in events:
        # Get the body of the event
        message_body = event.get_body().decode('utf-8')

        # Log the message
        logging.info(f'Received message')

main()
