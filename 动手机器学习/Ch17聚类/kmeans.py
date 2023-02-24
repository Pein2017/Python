'''
作者：卢沛安
时间：2023年02月15日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


class Kmeans :
    def __init__( self , k=2 , max_iterations=10 ) :
        self.k = k
        self.max_iterations = max_iterations

        self.centroids = None
        self.clusters = None

    def eu_distance( self , x , y ) :
        '''

        :param x: vector x
        :param y: vector y
        :return: np.sqrt( distance )
        '''
        distance = 0
        for i in range( len( x ) ) :
            distance += np.power( (x[ i ] - y[ i ]) , 2 )
        return np.sqrt( distance )

    def centroids_init( self , X , k ) :
        '''

        :param X: training samples , numpy array
        :param k: n_cluster
        :return: centroids matrix
        '''
        m , n = X.shape
        # 质心矩阵的大小为 质心个数*特征数
        centroids = np.zeros( (k , n) )
        for i in range( k ) :
            # 随机选择一个类的中心作为质心向量
            centroid = X[ np.random.choice( range( m ) ) ]
            # 将质心向量分配给质心矩阵
            centroids[ i ] = centroid

        return centroids

    def closest_centroid( self , x , centroids ) :
        '''
        :param x: single sample
        :param centroids: centroids matrix
        :return: closest ith centroid
        '''
        closest_i , closest_dist = 0 , float( 'inf' )
        for i , centroid in enumerate( centroids ) :
            distance = self.eu_distance( x , centroid )
            if distance < closest_dist :
                closest_i , closest_dist = i , distance
        return closest_i

    def build_clusters( self , centroids , k , X ) :
        '''
        :param centroids:
        :param k:
        :param X:
        :return: full sample indices (not sample data) group by k-clusters in list form
        '''
        clusters = [ [ ] for _ in range( k ) ]
        for x_i , x in enumerate( X ) :
            centroid_i = self.closest_centroid( x , centroids )
            clusters[ centroid_i ].append( x_i )
        return clusters

    def update_centroids( self , clusters , k , X ) :
        '''
        :param clusters: clusters in previous iteration
        :param k:
        :param X:
        :return: updated centroids matrix
        '''
        n = X.shape[ 1 ]
        centroids = np.zeros( (k , n) )
        for i , cluster in enumerate( clusters ) :
            centroid = np.mean( X[ cluster ] , axis=0 )
            centroids[ i ] = centroid
        return centroids

    def get_cluster_labels( self , X ) :
        '''
        :param clusters: current clusters
        :param X: training samples
        :return: labels
        '''
        clusters = self.clusters
        m = X.shape[ 0 ]
        y_pred = np.zeros( m )
        for cluster_i , cluster in enumerate( clusters ) :
            for sample_i in cluster :
                y_pred[ sample_i ] = cluster_i
        return y_pred

    def fit( self , X ) :
        k = self.k
        max_iterations = self.max_iterations
        centroids = self.centroids_init( X , k )
        for i in range( max_iterations ) :
            print( f'{i + 1}th iteration---' )
            clusters = self.build_clusters( centroids , k , X )
            prev_centroids = centroids
            centroids = self.update_centroids( clusters , k , X )  # new centroids
            diff = centroids - prev_centroids
            if not diff.any() :
                print( 'break out' )
                break
        print( 'centroids and clusters built ---' )
        self.centroids = centroids
        self.clusters = clusters

    def predict( self , X ) :
        '''
        :param clusters: calculated centroids
        :param X: new samples
        :return: prediction
        '''
        centroids = self.centroids
        m = X.shape[ 0 ]
        y_pred = np.zeros( m )
        for x_i , x in enumerate( X ) :
            centroid_i = self.closest_centroid( x , centroids )
            y_pred[ x_i ] = centroid_i
        return y_pred


X = np.random.randint( low=0 , high=10 , size=(200 , 2) )
X_train = X[ :170 ]
X_test = X[ 170 : ]
model = Kmeans( k=4 , max_iterations=20 )
model.fit( X_train )
pred = model.predict( X_test )

clusters = model.clusters
centers = model.centroids

colors = [ 'r' , 'g' , 'b' , 'y' ]
pred_color = 'w'

for i , center in enumerate( centers ) :
    plt.scatter( center[ 0 ] , center[ 1 ] , marker='*' , color=colors[ i ] , s = 150)
for i in range( len( clusters ) ) :
    for x_i in clusters[ i ] :
        plt.scatter( X[ x_i ][ 0 ] , X[ x_i ][ 1 ] , color=colors[ i ] ,s = 100)

for x_i , x in enumerate( X_test ) :
    cluster = int( pred[ x_i ] )
    plt.scatter( x[ 0 ] , x[ 1 ] , marker='X' , color=colors[ cluster ] ,s = 150 )

plt.show( block=True )

if __name__ == '__main__' :
    print( "finished!" )
