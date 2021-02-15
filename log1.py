from datetime import datetime

class FileLog():
    _instance = None

    def __new__(cls,level):
        leveldict = {
                    None:0,
                    "info": 1,
                    "warning": 2,
                    "error": 3
                    }
        if cls._instance is None:
            print("INIT: Creating Logger!")
            cls._instance = super(FileLog, cls).__new__(cls)
            cls._openLog = open("log.txt","w+")
            cls._level = leveldict[level]
            
        return cls._instance


    def info(cls,msg):
        if cls._level < 2:
            cls._openLog.write(f'{datetime.now().strftime("%H:%M:%S")}, INFO: {msg}\n')
        else:
            pass

       

    def warning(cls,msg):
        if cls._level < 3:
            cls._openLog.write(f'{datetime.now().strftime("%H:%M:%S")}, WARNING: {msg}\n')
        else:
            pass

    def error(cls,msg):
        print(cls._level < 4)
        if cls._level < 4:
            cls._openLog.write(f'{datetime.now().strftime("%H:%M:%S")}, ERROR: {msg}\n')
        else:
            pass

         


'''
The following function serves as a simple test to check
whether the id of multiple instances of Filelog remain
the same.
'''


def file_log_test():
    log = FileLog("error")
    log.info(f'One CS162 Filelog instance found with id {id(log)}')
    log2 = FileLog("error")
    log2.warning(f'Another CS162 Filelog instance Found with id {id(log2)}.')
    if id(log) != id(log2):
        log.error('The singleton implementation is buggy!')
    else:
        log.error('The singleton implementation works!')


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