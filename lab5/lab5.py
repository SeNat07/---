import pandas as pd

from matplotlib import pyplot as pl
from matplotlib.colors import ListedColormap
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.neighbors import KNeighborsClassifier


def decision_tree(X_train, X_test, y_train, y_test):

    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)
    pred = dt.predict(X_test)

    print("Report showing the main classification metrics by the <Decision Tree> method")
    print(classification_report(y_test, pred))

    show(X_train, X_test, y_train, y_test, pred, accuracy_score(y_test, pred), "Decision Tree")

def gradient_boosting(X_train, X_test, y_train, y_test):

    gb = GradientBoostingClassifier()
    gb.fit(X_train, y_train)
    pred = gb.predict(X_test)

    print("Report showing the main classification metrics by the <Gradient Boosting> method")
    print(classification_report(y_test, pred))

    show(X_train, X_test, y_train, y_test, pred, accuracy_score(y_test, pred), "Gradient Boosting")

def random_forest(X_train, X_test, y_train, y_test):

    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)
    pred = rf.predict(X_test)

    print("Report showing the main classification metrics using the <Random Forest> method")
    print(classification_report(y_test, pred, zero_division=0))

    show(X_train, X_test, y_train, y_test, pred, accuracy_score(y_test, pred), "Random Forest")

def k_neighbors(X_train, X_test, y_train, y_test):

    knn = KNeighborsClassifier()
    knn.fit(X_train, y_train)
    pred = knn.predict(X_test)

    print("A report showing the main classification metrics using the <K nearest neighbors> method")
    print(classification_report(y_test, pred))

    show(X_train, X_test, y_train, y_test, pred, accuracy_score(y_test, pred), "K nearest neighbors")

def show(X_train, X_test, y_train, y_test, pred, accuracy, classificator):

    y_train = y_train.map({'Y': 0, 'N': 1})
    y_test = y_test.map({'Y': 0, 'N': 1})
    pred[pred == 'Y'] = 0
    pred[pred == 'N'] = 1

    fig = pl.figure(figsize=(15, 20))
    fig.suptitle("Classifier accuracy {} : {}".format(classificator, round(accuracy, 2)))
    colors = ListedColormap(['Red', 'Blue'])

    ax = fig.add_subplot(2, 2, 1, projection='3d')
    scatter = ax.scatter3D(X_train[:, 0], X_train[:, 2], X_train[:, 1], c=y_train, cmap=colors)

    ax.set_zlabel("Amount of credit")
    ax.legend(*scatter.legend_elements(), title="Approved/Not approved")
    ax.title.set_text("Loan Approval Status - Training Set")
    ax.set_xlabel("Applicant's income")
    ax.set_ylabel("Credit history")

    ax = fig.add_subplot(2, 2, 2, projection='3d')
    ax.scatter3D(X_train[:, 0], X_train[:, 2], X_train[:, 1], c=y_train, cmap=colors)


    ax.set_xlim(0, 15000)
    ax.set_zlim(0, 350)
    ax.set_zlabel("Amount of credit")
    ax.title.set_text("Loan Approval Status - Training Set\n(most values upscaled)")
    ax.set_xlabel("Applicant's income")
    ax.set_ylabel("Credit history")

    ax = fig.add_subplot(2, 2, 3, projection='3d')
    ax.scatter3D(X_test[:, 0], X_test[:, 2], X_test[:, 1], c=y_test, marker="x", alpha=0.7, cmap=colors)

    ax.set_xlim(0, 15000)
    ax.set_zlim(0, 350)
    ax.set_zlabel("Amount of credit")
    ax.title.set_text("Loan approval status (actual values of the test sample")
    ax.set_xlabel("Applicant's income")
    ax.set_ylabel("Credit history")


    ax = fig.add_subplot(2, 2, 4, projection='3d')
    ax.scatter3D(X_test[:, 0], X_test[:, 2], X_test[:, 1], c=pred, marker="x", alpha=0.7, cmap=colors)

    ax.set_xlim(0, 15000)
    ax.set_zlim(0, 350)
    ax.set_zlabel("Amount of credit")
    ax.title.set_text("Loan approval status (classifier values)")
    ax.set_xlabel("Applicant's income")
    ax.set_ylabel("Credit history")

    pl.show()


train = pd.read_csv("Data.csv", delimiter=',')
dataset = train.copy()


# transformation of categorical features
dataset = dataset.dropna()
dataset['Gender'] = dataset['Gender'].map({'Male': 0, 'Female': 1})
dataset['Married'] = dataset['Married'].map({'No': 0, 'Yes': 1})

# transformation of the sign of the number of dependents
# (3 or more people = "3+" changed to 10 as a relatively large number of dependents compared to 0 and 1)
dataset.loc[(dataset.Dependents == '3+'), 'Dependents'] = 5
dataset['Education'] = dataset['Education'].map({'Not Graduate': 0, 'Graduate': 1})
dataset['Self_Employed'] = dataset['Self_Employed'].map({'No': 0, 'Yes': 1})
dataset['Property_Area'] = dataset['Property_Area'].map({'Urban': 0, 'Semiurban': 1, 'Rural': 2})

# explicit assignment of a categorical type
categorys = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Credit_History']
dataset[categorys] = dataset[categorys].astype("category")
label = dataset['Loan_Status']
dataset.drop(['Loan_Status'], axis=1, inplace=True)
dataset.drop(['Loan_ID'], axis=1, inplace=True)

# scaling of continuous functions
continuous_features = set(dataset.columns) - set(categorys)
scaler = MinMaxScaler()
dataset_norm = dataset.copy()
dataset_norm[(list(continuous_features))] = scaler.fit_transform(dataset[list(continuous_features)])

# feature selection using random forest
clf = RandomForestClassifier()
clf.fit(dataset_norm, label)

pl.figure(figsize=(12, 12))
pl.bar(dataset_norm.columns, clf.feature_importances_)
pl.xticks(rotation=45)
pl.show()


# removing irrelevant columns
train.drop(['Loan_ID'], axis=1, inplace=True)
train.drop(['Gender'], axis=1, inplace=True)
train.drop(['Married'], axis=1, inplace=True)
train.drop(['Dependents'], axis=1, inplace=True)
train.drop(['Education'], axis=1, inplace=True)
train.drop(['Self_Employed'], axis=1, inplace=True)
train.drop(['CoapplicantIncome'], axis=1, inplace=True)
train.drop(['Loan_Amount_Term'], axis=1, inplace=True)
train.drop(['Property_Area'], axis=1, inplace=True)

# dataset output and statistics on it
print("Dataset dimension: ", train.shape)
print(train)
print("Descriptive statistics by dataset:\n", train.describe(include="all"))
print("Number of passes initially:\n", train.isna().sum())


# entering the median instead of the missing values of the feature <loan amount>
train['LoanAmount'] = train['LoanAmount'].fillna(train['LoanAmount'].median())

train = train.dropna()
train = train.drop_duplicates()

# explicit change to categorical type
train['Credit_History'] = train['Credit_History'].astype("category")


# division into training and testing set
y = train.Loan_Status
train.drop(['Loan_Status'], axis=1, inplace=True)
X = train.iloc[::].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2)

# data standardization
scaler = StandardScaler()
scaler.fit_transform(X_train)
scaler.fit_transform(X_test)

# launching the work of classifiers and their visualization
decision_tree(X_train, X_test, y_train, y_test)
gradient_boosting(X_train, X_test, y_train, y_test)
random_forest(X_train, X_test, y_train, y_test)
k_neighbors(X_train, X_test, y_train, y_test)
