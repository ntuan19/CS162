
class Singleton(object):
    _instance = None
    def __new__(cls,*arg,**kwargs):
        if not cls._instance:
            cls._instance = super(Singleton,cls).__new__(cls,*arg,**kwargs)
        return cls._instance


def file_log_test():
    log = FileLog()
    log.info(f'One CS162 Filelog instance found with id {id(log)}')
    log2 = FileLog()
    log2.info(f'Another CS162 Filelog instance Found with id {id(log2)}.')
    if id(log) != id(log2):
        log.error('The singleton implementation is buggy!')
    else:
        log.info('The singleton implementation works!')


if __name__ == '__main__':
    '''
    STANDALONE TESTING:
    -------------------
    If you want to test this logging implementation separately. (ie. not relying
    on any other libraries) then you can run the following:

        $ python3 log.py

    This will run the file_log_test() code, which will verify whether or not
    you have a successful singleton implementation.
    '''
    file_log_test()
