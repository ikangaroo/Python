#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from AND import Perceptron

def f(x):
    '''
    激活函数
    '''
    return 1 if x>0 else 0

def get_training_dataset():
    '''
    input and output
    '''
    input_vecs = [[1,1],[1,0],[0,1],[0,0]]
    labels = [1,0,0,0]
    
    return input_vecs,labels

def train_and_perceptron():
    '''
    and
    '''
    P = Perceptron(2,f)
    input_vecs , labels = get_training_dataset()
    P.train(input_vecs,labels,20,0.1)
    return P

def main():
    and_perceptron = train_and_perceptron()
    print and_perceptron

    print '1 and 1 = %d' % and_perceptron.predict([1,1])
    print '0 and 1 = %d' % and_perceptron.predict([0,1])
    print '1 and 0 = %d' % and_perceptron.predict([1,0])
    print '0 and 0 = %d' % and_perceptron.predict([0,0])


if __name__ == '__main__':
    main()