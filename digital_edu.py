#создай здесь свой индивидуальный
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session


df = pd.read_csv('train.csv')
df['has_mobile'] = df['has_mobile'].apply(int)
df['graduation'] = df['graduation'].apply(int)
df['followers_count'] = df['followers_count'].apply(int)
df['relation'] = df['relation'].apply(int)
df['life_main'] = df['life_main'].replace('False', 0)
df['people_main'] = df['people_main'].replace('False', 0)
df['life_main'] = df['life_main'].apply(int)
df['people_main'] = df['people_main'].apply(int)
df['education_form'].fillna(0, inplace = True)
def edu_form(form):
    if form == 'Full-time':
        return 1
    elif form == 'Distance Learning':
        return 2
    elif form == 'Part-time':
        return 3
    elif form == 'External':
        return 4
    return 0
df['education_form'] = df['education_form'].apply(edu_form)
def get_main(main):
    if main == 'False':
        return 0
    return main
df['life_main'] = df['life_main'].apply(get_main)
df['people_main'] = df['people_main'].apply(get_main)
def get_bdate(date):
    date = str(date)
    if date != 'NaN':
        date_list = date.split('.')
        if len(date_list) == 5:
            return int(date_list[2])
        elif len(date_list) ==6:
            return 0
        return 0
    return 0       
df['bdate'] = df['bdate'].apply(get_bdate)
def get_russian(lang):
    if lang.find('Русский')==0:
        return 1
    return 0
def get_english(lang):
    if lang.find('English')==0:
        return 1
    return 0
df['Russian'] = df['langs'].apply(get_russian)
df['English'] = df['langs'].apply(get_english)
df['result'] = df['Russian'].apply(get_english)
df = df.reindex(columns = ['id', 'sex', 'bdate', 'has_photo', 'has_mobile',
                'followers_count','graduation','education_form','relation',
                'education_status','life_main','people_main','Russian','English',
                'occupation_type','result'])
df.drop([ 'has_photo', 
'followers_count','education_form','Russian'],axis=1,inplace=True)
df['bdate'] = df['graduation'] - 15
def get_occupation(occu_type):
    if occu_type != 'NaN':
        if occu_type == 'university':
            return 1
        if occu_type == 'work':
            return 2
    return 0
df['occupation_type'] = df['occupation_type'].apply(get_occupation)
def get_edu_status(status):
    if status == "Undergraduate applicant":
        return 1
    elif status == "Student (Bachelor's)":
        return 2
    elif status == "Alumnus (Bachelor's)":
        return 3
    elif status == "Student (Master's)":
        return 4
    elif status == "Alumnus (Master's)":
        return 5
    elif status == "Student (Specialist)":
        return 6
    elif status == "Alumnus (Specialist)":
        return 7
    elif status == "Phd":
        return 8
    elif status == "Candidate of Sciences":
        return 9
    return 0
df['education_status'] = df['education_status'].apply(get_edu_status)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
x = df.drop('result', axis = 1)
y = df['result']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
classifier = KNeighborsClassifier(n_neighbors = 7)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
percent = accuracy_score(y_test, y_pred) * 100
print(round(percent, 3))
 