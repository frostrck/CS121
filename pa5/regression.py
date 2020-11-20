'''
Linear regression

YOUR NAME HERE

Main file for linear regression and model selection.
'''

import numpy as np
from sklearn.model_selection import train_test_split
import util


class DataSet(object):
    '''
    Class for representing a data set.
    '''

    def __init__(self, dir_path):
        '''
        Class for representing a dataset, performs train/test
        splitting.

        Inputs:
            dir_path: (string) path to the directory that contains the
              file
        '''

        parameters_dict = util.load_json_file(dir_path, "parameters.json")
        self.pred_vars = parameters_dict["predictor_vars"]
        self.name = parameters_dict["name"]
        self.dependent_var = parameters_dict["dependent_var"]
        self.training_fraction = parameters_dict["training_fraction"]
        self.seed = parameters_dict["seed"]
        self.labels, data = util.load_numpy_array(dir_path, "data.csv")
        self.training_data, self.testing_data = train_test_split(data,
            train_size=self.training_fraction, test_size=None,
            random_state=self.seed)

class Model(object):
    '''
    Class for representing a model.
    '''

    def __init__(self, dataset, pred_vars):
        '''
        Construct a data structure to hold the model.
        Inputs:
            dataset: an dataset instance
            pred_vars: a list of the indices for the columns (of the
              original data array) used in the model.
        '''

        self.dep_var = dataset.dependent_var
        self.labels = dataset.labels
        self.pred_vars = pred_vars
        self.beta = util.linear_regression(util.prepend_ones_column(
                dataset.training_data[:, self.pred_vars]),
                dataset.training_data[:, self.dep_var])
        self.R2 = self.calc_R2(dataset.training_data)
        self.R2_test_d = self.calc_R2(dataset.testing_data)
        

    def __repr__(self):
        '''
        Format model as a string.
        '''

        # Replace this return statement with one that returns a more
        # helpful string representation
        return "!!! You haven't implemented the Model __repr__ method yet !!!"

    def calc_R2(self, data):
        '''
        Calculates the R^2 value of a model.

        Inputs: 
            data: a array of data
        
        Returns:
            (float) R^2 value 
        '''

        y = data[:, self.dep_var]
        y_bar = y.mean()
        y_hat = util.apply_beta(self.beta, util.prepend_ones_column(data[:, self.pred_vars]))

        return 1 - sum((y - y_hat) ** 2) / sum((y - y_bar) ** 2)


def compute_single_var_models(dataset):
    '''
    Computes all the single-variable models for a dataset

    Inputs:
        dataset: (DataSet object) a dataset

    Returns:
        List of Model objects, each representing a single-variable model
    '''

    models = []

    for var in dataset.pred_vars:
        mod = Model(dataset, [var])
        models.append(mod)
    
    return models


def compute_all_vars_model(dataset):
    '''
    Computes a model that uses all the predictor variables in the dataset

    Inputs:
        dataset: (DataSet object) a dataset

    Returns:
        A Model object that uses all the predictor variables
    '''

    mod = Model(dataset, dataset.pred_vars)

    return mod


def compute_best_pair(dataset):
    '''
    Find the bivariate model with the best R2 value

    Inputs:
        dataset: (DataSet object) a dataset

    Returns:
        A Model object for the best bivariate model
    '''

    best = None 
    R2 = 0
   
    for var1 in dataset.pred_vars:
        for var2 in dataset.pred_vars:
            if var1 != var2:
                mod = Model(dataset, [var1, var2])
                if mod.R2 > R2:
                    R2 = mod.R2
                    best = mod

    return best  


def forward_selection(dataset):
    '''
    Given a dataset with P predictor variables, uses forward selection to
    select models for every value of K between 1 and P.

    Inputs:
        dataset: (DataSet object) a dataset

    Returns:
        A list (of length P) of Model objects. The first element is the
        model where K=1, the second element is the model where K=2, and so on.
    '''
    
    best_vars = {}
    best_vars[0] = []

    R2 = 0
    p = len(dataset.pred_vars)
    best_models = []
    
    for i in range(1, p+1):
        for var in dataset.pred_vars:
            if var not in best_vars[i-1]:
                pred = list.copy(best_vars[i-1])
                pred.append(var)
                mod = Model(dataset, pred)
                if mod.R2 > R2:
                    R2 = mod.R2
                    best_vars[i] = pred

    for i in range(1, p+1):
        model = Model(dataset, best_vars[i])
        best_models.append(model)
        
        
    return best_models

def validate_model(dataset, model):
    '''
    Given a dataset and a model trained on the training data,
    compute the R2 of applying that model to the testing data.

    Inputs:
        dataset: (DataSet object) a dataset
        model: (Model object) A model that must have been trained
           on the dataset's training data.

    Returns:
        (float) An R2 value
    '''

    return model.R2_test_d