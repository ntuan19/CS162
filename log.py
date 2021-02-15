'''
Write your own version of Filelog here!

The Filelog Class opens up a file and adds log messages within.
Previous log messages, if any, should not be removed. Also, there
can be only one Filelog object at any time of this
program - that is, creating a second Filelog object should return
the exact same instance as the first one. (See testing code below.)

At least three methods are required:
info(msg), warning(msg), and error(msg).
'''
#code adapted from: https://gist.github.com/pazdera/1098129, 
# https://www.youtube.com/watch?v=qzCHtYoqh_I

class FileLog():
    #this is the single skeleton design.
    __instance = None
    def __new__(cls,level_of_error,*arg,**kwargs):
        level ={
            None:0,
            "infor":1,
            "warning:":2,
            "error":3
        } 
        if FileLog.__instance == None:
            cls.__instance = super(FileLog,cls).__new__(cls,*arg,**kwargs)
            cls._openFl = open("log.txt","w+")
            cls._level_of_error = level[level_of_error]
        return cls.__instance
    def info(cls,msg):
        if cls._level_of_error< 2:
            cls._openFl.write("Infor:"+msg+"\n")
        else:
            pass
    def warning(cls,msg):
        if cls._level_of_error< 3:
            cls._openFl.write("Warning:"+msg+"\n")
        else:
            pass
    def error(cls,msg):
        if cls._level_of_error< 4:
            cls._openFl.write("Error:"+msg+"\n")
        else:
            pass


'''
The following function serves as a simple test to check
whether the id of multiple instances of Filelog remain
the same.
'''


def file_log_test():
    log = FileLog("infor")
    log.info(f'One CS162 Filelog instance found with id {id(log)}')
    log2 = FileLog("error")
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
