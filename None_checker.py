import time
import pandas as pd
import numpy as np

def None_checker(p):
    """
    This function flags if the parameter is null or not
    returns : False if not null(can be blank)
              True for null
    """
    start = time.time()
    try:
        if p is np.nan:
            return True
        elif p and p != 0:
            return False
        elif p == 0:
            return False
        elif p is None:
            return True
        elif len(p) >= 0:
            return False
        else:
            return False
    except ValueError:
        print("Encountered DataFrame or Series")
        if p.isnull().values.any():
            return True
        else:
            return False
    finally:
        print("Time taken to execute: {}".format(time.time() - start))


#List of all types and values that are correctly defined.
d =[[], {}, (), np.nan, pd.Series({'col1': np.nan}), None, 22, None, pd.DataFrame()]
p = 0
for i in d:
    p = None_checker(i)
    print(p)
