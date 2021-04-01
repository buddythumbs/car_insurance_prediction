# Classifiers
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression

GRID_SEARCH = {
    "Linear SVM": (SVC(kernel="linear", C=0.025, probability=True), {} ),
    "Decision Tree": (DecisionTreeClassifier(max_depth=5), {}), 
    "Random Forest": (
        RandomForestClassifier(max_depth=5, n_estimators=10, max_features=2), 
        {
            "model__max_features": [1, 2,5,10],
            "model__max_depth": [1,2,3,5,6],
            "model__n_estimators": [10,20,30],
        }), 
    "Neural Net": (MLPClassifier(alpha=1, max_iter=1000), {}), 
    "AdaBoost": (AdaBoostClassifier(), {}),
    "Naive Bayes": (GaussianNB(), {}),
    "XGB": (
        XGBClassifier(
            objective='binary:logistic', 
            eval_metric='auc',
            use_label_encoder=False),
        {
            'model__max_depth': [2, 3],
            # 'model__n_estimators': [10, 100, 150]
        })
}

PREDICTION_URL = "http://api:80/insurance_model/predictions/"
MODEL_POST_URL = "http://api:80/insurance_model/models/"
API_KEYS = [
    'id',
    'age',
    'job',
    'marital',
    'education',
    'default',
    'balance',
    'has_home_insurance',
    'car_loan',
    'communication',
    'last_contact_day',
    'last_contact_month',
    'num_contacts',
    'days_passed',
    'previous_attempts',
    'outcome',
    'call_start',
    'call_end'
]

DATA_KEYS = [
    'Id',
    'Age',
    'Job',
    'Marital',
    'Education',
    'Default',
    'Balance',
    'HHInsurance',
    'CarLoan',
    'Communication',
    'LastContactDay',
    'LastContactMonth',
    'NoOfContacts',
    'DaysPassed',
    'PrevAttempts',
    'Outcome',
    'CallStart',
    'CallEnd'
]

KEYS_MAP = dict(zip(DATA_KEYS, API_KEYS))