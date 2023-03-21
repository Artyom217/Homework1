from time import sleep
from functools import wraps
from datetime import datetime
import logging
logging.basicConfig(filename='performance.log', format='%(asctime)s - %(funcName)s()-%(message)s',level=logging.INFO)


def profile(func):
    @wraps(func)
    def wrapper(x):
        start=datetime.now()
        res=func(x)
        end = datetime.now() - start
        print(end)
        logging.info(f"-")
        return res


    return wrapper
@profile
def foo(x):
    sleep(2)

    return x ** 2


foo(2)
#sleep(60)
#foo(42)