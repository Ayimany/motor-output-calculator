import logging

RESET          = '\x1b[0m'
COLOR_ERROR    = '\x1b[31;20m'
COLOR_CRITICAL = '\x1b[31;1m'
COLOR_WARNING  = '\x1b[33;20m'
COLOR_DEBUG    = '\x1b[34;20m'
COLOR_INFO     = '\x1b[35;20m'

FORMAT  = '%(levelname)s: %(message)s'

FORMAT_STYLES = {
    logging.DEBUG   : f'{COLOR_INFO}{FORMAT}{RESET}',
    logging.INFO    : f'{COLOR_DEBUG}{FORMAT}{RESET}',
    logging.WARNING : f'{COLOR_WARNING}{FORMAT}{RESET}',
    logging.ERROR   : f'{COLOR_ERROR}{FORMAT}{RESET}',
    logging.CRITICAL: f'{COLOR_CRITICAL}{FORMAT}{RESET}'
}


def applyfmt(log):
    formatter = logging.Formatter(FORMAT_STYLES.get(log.levelno))

    return formatter.format(log)


class format_wrapper():

    def format(self, log):
        return applyfmt(log)


logger = logging.getLogger('m-out')
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(format_wrapper())

logger.addHandler(handler)

