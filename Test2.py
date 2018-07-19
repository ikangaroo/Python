#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from AND import Perceptron

def f(x):
    return x

def get_training_dateset():
    '''
    input and output
    '''
    input_vecs = [[5],[3],[8],[1.4],[10.1]]
    labels = [5500,2300,7600,1800,11400]
    return input_vecs,labels

def train_and_perceptron():
    '''
    '''
    P = Perceptron(1,f)
    input_vecs,labels = get_training_dateset()
    P.train(input_vecs,labels,10,0.01)
    return P

def main():
    and_perceptron = train_and_perceptron()
    print and_perceptron

    print 'Work 3.4 years, monthly salary = %.2f' % and_perceptron.predict([3.4])

if __name__ == '__main__':
    main()
