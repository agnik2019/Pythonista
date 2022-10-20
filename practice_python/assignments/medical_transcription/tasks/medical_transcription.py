# /**
#  * @author Vinay Ummadi
#  * @email ummadi.vinay2000@gmail.com
#  * @create date 2022-09-16 11:53:03
#  * @modify date 2022-09-16 11:53:03
#  * @desc [description]
#  */
# ----------------------------------------------------
import pandas as pd
from time import time

data = pd.read_csv('tasks/data/mtsamples.csv')

def get_medical_specalities():
    """Returns the unique set of alphabetically ordered medical specialities from the data/mtsamples file.
    Input file: data/mtsamples.csv
    Output: Return a list of strings containing the unique set of alphabetically ordered medical specialities.
    Hint : Use th column 'medical_specialty' in the input csv file. The coulumn might have more than one speciality, in that case, split the string and add each speciality to the list.
    """
    lst = data['medical_specialty'].tolist()
    lst = set(lst)
    lst1 = []
    for l in lst:
        if '/' in l:
            l1 = l.split('/')
            for val in l1:
                lst1.append(val.strip())
        else:
            lst1.append(l.strip())
    lst1.sort()
    return lst1
    
 


def get_medical_specialities_count():
    """Returns the count of medical specialities in the data/mtsamples file.
    Input file: data/mtsamples.csv
    Output: Return a dictionary with key as the medical speciality and value as the count of the speciality. The dictionary should be sorted by the count in descending order.
    Hint : Use th column 'medical_specialty' in the input csv file. The coulumn might have more than one speciality, in that case, split the string and add each speciality to the list.
    """
    lst = data['medical_specialty'].tolist()
    lst1 = []
    for l in lst:
        if '/' in l:
            l1 = l.split('/')
            for val in l1:
                lst1.append(val.strip())
        else:
            lst1.append(l.strip())
    mp = {}
    for l in lst1:
        mp[l] = mp.get(l,0)+1
    
    mp = {val[0] : val[1] for val in sorted(mp.items(), key = lambda x: (-x[1], x[0]))}

    # a = sorted(mp.items(), key=lambda x: x[1],reverse= True)    
    # mp = {}
    # for k,v in a:
    #     mp[k] = v   
    
    return mp

def get_medical_speciality_sample_names():
    """This function returns a dictionary with key as the medical speciality and value as a list of sample names for that speciality.
    Input file: data/mtsamples.csv
    Output: Return a dictionary with key as the medical speciality and value as a list of sample names for that speciality.
    Hint : Use th column 'medical_specialty' in the input csv file. The coulumn might have more than one speciality, in that case, split the string and add each speciality to the list.
    """
    mp = data.groupby('medical_specialty')['sample_name'].apply(list).to_dict()
    mp = {val[0] : val[1] for val in sorted(mp.items(), key = lambda x: x[0])}
    
    return mp


if __name__ == "__main__":
    start = time()
    get_medical_specalities()
    get_medical_specialities_count()
    get_medical_speciality_sample_names()
    print(f"Time taken: {time() - start :.2f} seconds")