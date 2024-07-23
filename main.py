from create_data import create_data
from create_tables import create_tables
import logging

logging.basicConfig(
    level=logging.INFO,
    format='line_num: %(lineno)s > %(message)s'
)

def main():

    create_data()
    logging.info('Data was created.')
    create_tables()
    logging.info('Tables was generated.')


if __name__ == "__main__":
    main()