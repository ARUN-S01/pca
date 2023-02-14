import numpy as np

def PCA(X, Components):

  #Step 1 (Find Mean)
  mean = X - np.mean(X,axis=0)

  #Step 2 (Covariance Matrix)
  covariance_matrix = np.cov(mean, rowvar=False)

  #Step 3 (Eigen Values and Eigen Vectors)
  eigen_values, eigen_vectors = np.linalg.eigh(covariance_matrix)

  #Step 4 (Choosing the largest one, by sorting)
  sorted_index = np.argsort(eigen_values)[::-1]

  sorted_eigen_value = eigen_values[sorted_index]

  sorted_eigen_vector = eigen_vectors[:,sorted_index]

  #Step 5 (Selecting the number of components required)
  eigen_vector_subset = sorted_eigen_vector[:,0:Components]

  #Step 6 (Transforming of data)
  reduced_dimen = np.dot(eigen_vector_subset.transpose(),mean.transpose()).transpose()

  return reduced_dimen
