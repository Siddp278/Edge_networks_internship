# importing module
import logging

def LoggingNeeded(in_type, fun_input):
    """

    :param in_type: the type of logging needed(a string)
    :param fun_input: a text that needs to be logged( a string)
    :return: nothing.
    """

    log = logging.getLogger(__name__)
    file_handler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter('%(asctime)s(start point):Source Line->%(lineno)d:%(relativeCreated)d'
                                  '(ms later)::%(message)s')
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)
    if in_type is 'info':
        log.info('Just a brief info:{}'.format(fun_input))
    elif in_type is 'warning':
        log.warning('This is a warning:{}'.format(fun_input))
    else:
        log.error('An error occurred:{}'.format(fun_input))
