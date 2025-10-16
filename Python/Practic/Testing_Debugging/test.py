import logging
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    logging.debug('[DBUG]')
    logging.info('[INFO]')
    logging.warn('[WARNING]')
    logging.error('[ERROR]')
    logging.critical('[CRITICAL]')