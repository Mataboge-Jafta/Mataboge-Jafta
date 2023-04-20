from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from gensim.models import Word2Vec
from sklearn import decomposition
import pandas as pd
import numpy as np
import sys

def getProdDesc(id):
    prod_df = pd.read_csv('products.csv')
    return prod_df[prod_df.productId==id]['description'].values.tolist()[0]

def most_similar_readable(model, product_id):
    topx = 25
    similar_list = [(product_id,1.0)]+model.wv.most_similar(str(product_id), topn = topx)
    return [( productId, getProdDesc(productId), similarity ) for (productId,similarity) in similar_list]

app = Flask(__name__)
api = Api(app)

class HomePage (Resource):
    def get(self):
        return 'This is the root of the BCX Prodcuct Similarity App V0_1'

class RunModel (Resource):
    def get(self):
        results = {"similar products": []}
        point_arr = np.empty((0,100), dtype='f')
        topx=25

        selected_product = request.args.get('product')
        model = Word2Vec.load('models/prod2vec.100d.model')
        product_id = selected_product #'MR311654'
        results = most_similar_readable(model, product_id)

        close_words = model.wv.similar_by_word(product_id,topn = topx)
        close_words.insert(0, (product_id, 1))
        
        for wrd_score in close_words:
            wrd_vector = model.wv[wrd_score[0]]
            point_arr = np.append(point_arr, np.array([wrd_vector]), axis=0)
              
        pca = decomposition.PCA(n_components=3)
        pca.fit(point_arr)
        X = pca.transform(point_arr)
        x_coords = X[:, 0].tolist()
        y_coords = X[:, 1].tolist()
        z_coords = X[:, 2].tolist()
        
        return {'topn': results, 'x_coords': x_coords, 'y_coords': y_coords, 'z_coords': z_coords}

api.add_resource(HomePage, '/')
api.add_resource(RunModel, '/predict')

if __name__ == '__main__':
    app.run('0.0.0.0', '8888', debug=True)

