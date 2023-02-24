'''
作者：卢沛安
时间：2023年02月13日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

from Ch7决策树.CART_Final import ClassificationTree
from sklearn.metrics import accuracy_score , mean_squared_error
from sklearn import datasets
from sklearn.model_selection import train_test_split


class RandomForest :
    def __init__( self , n_estimators=5 , min_samples_split=3 , min_gini_impurity=999 , max_depth=float( 'inf' ) ,
                  max_features=None ) :
        self.n_estimators = n_estimators
        self.min_samples_split = min_samples_split
        self.min_gini_impurity = min_gini_impurity
        self.max_depth = max_depth
        self.max_features = max_features

        self.trees = [ ]
        for _ in range( self.n_estimators ) :
            tree = ClassificationTree( min_samples_split=self.min_samples_split ,
                                       min_gini_impurity=self.min_gini_impurity ,
                                       max_depth=self.max_depth )
            self.trees.append( tree )

    def boostrap_sampling( self , X , y ) :
        X_y = np.concatenate( (X , y) , axis=1 )
        np.random.shuffle( X_y )
        n_samples = X.shape[ 0 ]
        sampling_subsets = [ ]
        for _ in range( self.n_estimators ) :
            # 第一个随机性，行抽样
            idx1 = np.random.choice( n_samples , n_samples , replace=True )
            boostap_Xy = X_y[ idx1 , : ]
            boostap_X = boostap_Xy[ : , :-1 ]
            boostrap_y = boostap_Xy[ : , - 1 ]
            sampling_subsets.append( [ boostap_X , boostrap_y ] )
        return sampling_subsets

    def fit( self , X , y ) :
        n_features = X.shape[ 1 ]
        subsets = self.boostrap_sampling( X , y )
        # 设置max_features
        if self.max_features == None :
            self.max_features = int( np.sqrt( n_features ) )
        for i in range( self.n_estimators ) :
            # 第二个随机性，列抽样
            sub_X , sub_y = subsets[ i ]
            idx2 = np.random.choice( n_features , self.max_features , replace=False )
            sub_X = sub_X[ : , idx2 ]
            self.trees[ i ].fit( sub_X , sub_y )
            self.trees[ i ].feature_indices = idx2

            single_pred = self.trees[ i ].predict( sub_X )
            acc = accuracy_score( y , single_pred )
            print( f'tree {i + 1} acc is {round( acc , 2 )}' )

    def predict( self , X ) :
        y_preds = [ ]
        for i in range( self.n_estimators ) :
            idx = self.trees[ i ].feature_indices
            sub_X = X[ : , idx ]
            y_single_pred = self.trees[ i ].predict( sub_X )
            y_single_pred = y_single_pred.flatten()
            y_preds.append( y_single_pred )
        res = [ ]
        y_preds = np.array( y_preds ).T
        for j in y_preds :
            res.append( np.bincount( j.astype( 'int' ) ).argmax() )
        return res



from sklearn.datasets import load_wine

data = load_wine()
X , y = data.data , data.target
X_train , X_test , y_train , y_test = train_test_split( X , y.reshape( -1 , 1 ) , test_size=0.2 )

clf = RandomForest( n_estimators=10 , max_features=4 )
clf.fit( X_train , y_train )
pred = clf.predict( X_test )
y_pred = clf.predict( X_test )
acc_own = accuracy_score( y_test , y_pred )
print( f'accuracy of RF is {round( acc_own , 2 )}% ' )



from sklearn.ensemble import RandomForestClassifier
cclf = RandomForestClassifier( n_estimators=10 , max_depth=2 , max_features=4 )
cclf.fit( X_train , y_train.flatten() )
y_pred = clf.predict( X_test )
acc_skl = accuracy_score( y_test , y_pred )
print( f'accuracy of sklearn RF is {round( acc_skl , 2 )}% ' )

single = ClassificationTree( max_depth=2 )
single.fit( X_train , y_train )
y_single = single.predict( X_test )
acc_single = accuracy_score( y_test , y_single )
print( acc_single )



if __name__ == '__main__' :
    print( "finished!" )
