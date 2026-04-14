import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

#Reading data with pandas read_csv() method
music_data = pd.read_csv('/Users/chandu/Desktop/Python Course/music.csv')

# #Creating input and output data
# x = music_data.drop(columns=['genre'])
# y = music_data['genre']

# #Splitting data for training and testing using train_test_split() method
# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

# #Training the model
# model = DecisionTreeClassifier()
# model.fit(x_train,y_train)

# #Making predictions using testing data
# predictions = model.predict(x_test)

# #Prediction accuracy score check
# score = accuracy_score(y_test, predictions)
# score

# Storing a trained model in a joblib file
joblib.dump(model,'music-recommender.joblib')
model = joblib.load('music-recommender.joblib')
input_data = pd.DataFrame([[21,1]],columns = ['age','gender'])
predictions = model.predict(input_data)
predictions