import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from Mypack import Helper as H

H.easy("Wine Dataset", 1)
H.easy("The data is the results of a chemical analysis of wines grown in the same", 2)
H.easy("region in Italy by three different cultivators. There are thirteen different", 2)
H.easy("measurements taken for different constituents found in the three types of", 2)
H.easy("wine.", 2)

st.markdown(f'<hr style="height:2px;border:none;color:#333;background-color:#333;" />', unsafe_allow_html=True)

@st.cache
def my_slow_function():
    """
    this function returns the data after it is cached.
    """
    d = load_wine(as_frame=True)
    return d


Whole = my_slow_function()
Data = pd.DataFrame(Whole.data)
Target = pd.DataFrame(Whole.target)
frame = [Data, Target]
xx = pd.concat(frame, axis=1, sort=False)

H.easy("Basic info About the wine data", 3)
Table1 = pd.DataFrame({'Data Set Characteristics': ["Multivariate"], 'Area': ['Physical'],
                  'Associated Task': ['Classification'], 'Attribute Characteristics': ['Real Numbers']})
H.easy("Data Set Information", 4)
st.table(Table1)

H.easy("The dimensions of the dataset:", 4)
H.easy(Data.shape, 5)

H.easy("The Features of the data are:", 4)
H.easy(Data.columns, 5)

H.easy("The classes into which classification occurs:", 4)
st.table(Target['target'].value_counts())

#Dividing data wrt to classes
x1 = Data[0:59]
x2 = Data[59:130]
x3 = Data[130:]

H.easy("This describes the data", 4)
if st.checkbox("Show Description"):
    H.easy(Data.describe(include='all'), 5)

H.easy("The number of null values for each columns", 4)
st.table(Data.isnull().sum())

H.easy("The type of values for each columns", 4)
st.table(Data.dtypes)

@st.cache
def maxi():
    """
    this function returns the maximum values for each column.
    """
    st.dataframe(Data.style.highlight_max(axis=0))


if st.checkbox("Show max values for each column"):
    maxi()

st.markdown(f'<hr style="height:2px;border:none;color:#333;background-color:#333;" />', unsafe_allow_html=True)

H.easy("Shows correlation between each feature", 4)
plt.figure(figsize=(8, 6))
sns.heatmap(xx.corr(), cmap='Blues', vmax=1.0, fmt='.1f', annot=True)
st.pyplot()
H.easy("From looking at the cute chart you can clearly see the groups Total_Phenols-flavanoids, "
           "Total_Phenols-proanthocyanins, flavanoids-diluted_wines and alcohol-proline have high"
           "positive correlation.", 5)
H.easy("This might produce multicollinearity for models like Logistic Regression.", 5)
H.easy('From the chart we can see for each cultivator, he/she has distinct properties in relation to '
           'flavanoids, total_phenols, hue,etc' ,5)

H.easy("Choose from the three cultivators for their wine's info", 3)
part = st.radio("....", ('One(class 0)', 'Two(class 1)', 'Three(class 2)'))
if part == "One(class 0)":
    H.easy("Here is the summary for the first cultivator's wine", 2)
    H.easy(x1.describe(), 5)
if part == "Two(class 1)":
    H.easy("Here is the summary for the second cultivator's wine", 2)
    H.easy(x2.describe(), 5)
if part == "Three(class 2)":
    H.easy("Here is the summary for the Third cultivator's wine", 2)
    H.easy(x3.describe(), 5)

H.easy("Some insights from the data", 3)
H.easy("All numbers are relative to one another and values of individual columns are not", 2)
H.easy("to be compared with each other.", 2)

st.markdown(f'<hr style="height:2px;border:none;color:#333;background-color:#333;" />', unsafe_allow_html=True)

if st.checkbox("Flanavoid"):
    H.easy("It exhibits high biological activity and display antioxidant and anti-allergy properties.", 5)
    H.easy("According to data class 0 holds the largest amount of flanavoid while class 2 holds"
               " the least, which tells class ) is very healthy type of wine.", 5)

if st.checkbox("Hue and Athocyanin"):
    H.easy("The red color in wine comes from anthocyanin and wines with more red "
               "colored are more aged hence better", 5)
    H.easy("From the data, levels of proanthocyanin(anthocyanin) is highest in class 0 with the least in class 2",5)
    H.easy("As we see the Hue for class 1 it is pretty spread out meaning the wine hasn't been aged much,"
               " thus telling the quality is not that great relatively.", 5)

if st.checkbox("Proline"):
    H.easy("Proline too is helpful biologically and is in traces in wine.", 5)
    H.easy("From the comparision of numbers it is clear that class 0 has it in abundance which "
               "makes it worthful of your money ;)", 5)
    H.easy("Class 1 and 2 lag behind in this aspect but its no biggie considering proline doesnt "
               "contribute to taste.", 5)

if st.checkbox("Ash"):
    H.easy("Now Ash is actually all the minerals found in wine like potassium, sodium, etc.", 5)
    H.easy("A 2.5g/L is floor minimum in wines and all classes reach this levels fortunately.", 5)

st.sidebar.title("Note on the correlation")
st.sidebar.text('For more info on the graph.')

st.markdown(f'<hr style="height:2px;border:none;color:#333;background-color:#333;" />', unsafe_allow_html=True)

if st.sidebar.checkbox("Target"):
    H.easy("If you give emphasis on the correlation chart it shows high levels of correlation of some "
               "features with the target variable", 5)
    H.easy("The point here is that all these features are actually key points within wine making and"
               " a good combination of them creates a great wine which in this data is being shown by class 0.", 5)
