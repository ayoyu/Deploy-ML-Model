from flask import Flask
from flask_restful import Resource, Api, reqparse
from vectorizer import vect
import os
import pickle
import numpy as np

app = Flask(__name__)
api = Api(app)
cur_dir = os.path.dirname(__file__)
with open(os.path.join(cur_dir,'Models','classifier.pkl'),'rb') as f:
	clf = pickle.load(f)

def classify(document):
    X=vect.transform([document])
    label={0:'negative',1:'positive'}
    y=clf.predict(X)
    proba=np.max(clf.predict_proba(X))
    return label[y[0]],str(round(proba*100,2))

parser = reqparse.RequestParser()
parser.add_argument('query', required=True)
class MovieClassifier(Resource):

	def get(self):
		args = parser.parse_args()
		doc = args['query']
		rating, proba = classify(doc)
		return {rating:proba+'%'}
api.add_resource(MovieClassifier,'/')

if __name__ == '__main__':
	app.run(debug=True)


