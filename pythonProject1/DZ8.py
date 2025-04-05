import logging

from datetime import datetime

logging.basicConfig(level=logging.INFO, filename = 'logs.log', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d')

today = datetime.now().strftime('%Y-%m-%d')

logging.info(f"Сьогодняшня дата : {today}")