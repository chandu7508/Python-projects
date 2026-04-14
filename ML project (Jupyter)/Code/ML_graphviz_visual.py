from sklearn import tree


#Reading data with pandas read_csv() method
music_data = pd.read_csv('/Users/chandu/Desktop/Python Course/music.csv')

# #Creating input and output data
x = music_data.drop(columns=['genre'])
y = music_data['genre']

tree.export_graphviz(model,out_file='music-recommender.dot',feature_names=['age','gender'],class_names=sorted(y.unique()),label='all',rounded=True,filled=True)