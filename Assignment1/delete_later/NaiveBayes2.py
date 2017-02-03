import numpy as np
import collections
import json
import pickle 
import nbClassify

labels_index_dict = dict()
set_of_unique_words = []
word_dict = dict()
NB_models_param_dict = dict()


"""

    Creates a Naive Bayes model for the given list of documents and their labels
    Class_prior_probability : Prior probability of each class : Array , with its label index dictionary in the variable : labels_index_dict
    Probability of each word in each class : wordwiseprob_eachclass Array, with its index mapping in dictionary word_dict
    
"""
def create_NB_model(bow_reviews_list,labels_arr):
    
    global labels_index_dict
    
    wordWise_count_eachclass = categorise_words_classwise(bow_reviews_list, labels_arr)
    wordwiseprob_eachclass = np.zeros((len(labels_index_dict), np.shape(set_of_unique_words)[0]))
    tot_word_eachClass = get_classwise_wordcount(np.zeros((len(labels_index_dict))), wordWise_count_eachclass)
    
    class_prior_probability = calculate_class_priorProbability(bow_reviews_list, labels_arr)
    wordwiseprob_eachclass = calculate_wordwise_probability(wordwiseprob_eachclass, tot_word_eachClass, wordWise_count_eachclass)
    
    print "class_prior_probability:::", class_prior_probability
    print "wordwiseprob_eachclass[:,0]:::", wordwiseprob_eachclass[:,0]
    print "tot_word_eachClass::", tot_word_eachClass
    
    output = open('NBModel.pkl', 'wb')
    print wordwiseprob_eachclass[0][word_dict['considered,']]
    print wordwiseprob_eachclass[1][word_dict['considered,']]
    print wordwiseprob_eachclass[2][word_dict['considered,']]
    print wordwiseprob_eachclass[3][word_dict['considered,']]

    NB_models_param_dict['class_prior_probability'] = class_prior_probability
    NB_models_param_dict['labels_index_dict'] = labels_index_dict
    NB_models_param_dict['word_dict'] = word_dict
    #nbClassify.classify_data(class_prior_probability, labels_index_dict, word_dict, wordwiseprob_eachclass)
    
    np.save('obj', NB_models_param_dict)
    #pickle.dump(NB_models_param_dict, open('obj.txt', 'wb'))
    ##json.dump(NB_models_param_dict, open("text.txt",'w'))
    
    

    
def calculate_class_priorProbability(bow_reviews_list, labels_arr):
    class_prior_probability = np.zeros((len(labels_index_dict)))
    global labels_index_dict
    for i in range(0, np.shape(labels_arr)[1]):
        counter_arr = collections.Counter(labels_arr[:,i])
        total_count = 0
        for key in counter_arr:
            class_prior_probability[labels_index_dict[key]] = counter_arr[key]
            total_count += counter_arr[key]
            
        print "counter_arr", counter_arr
        print "total_count", total_count
        for key in counter_arr:
            class_prior_probability[labels_index_dict[key]] = class_prior_probability[labels_index_dict[key]]/total_count
        print "counter_arr", counter_arr
    print labels_index_dict         
    return class_prior_probability

    
       
def calculate_wordwise_probability(probability_wordwise_arr, total_count_classwise, labelwise_word_arr):
    
    global set_of_unique_words
    vocab_size = len(set_of_unique_words)
    
    for i in range(0, np.shape(labelwise_word_arr)[0]):
        for j in range(0, np.shape(labelwise_word_arr)[1]):
            probability_wordwise_arr[i][j] = (labelwise_word_arr[i][j] + 1)/(total_count_classwise[i] + vocab_size)
            
    return  probability_wordwise_arr

   
def get_classwise_wordcount(total_count_classwise, labelwise_word_arr):
    count = 0

    for row in labelwise_word_arr:
        total_count_classwise[count]= np.sum(row)
        count += 1
    return total_count_classwise


def categorise_words_classwise(bow_reviews_list,labels_arr):
    global labels_index_dict
    global set_of_unique_words
    
    set_of_unique_words, word_index_dict = get_unique_words(bow_reviews_list)
    labels_index_dict = get_labelindex_dict(labels_arr)
    unique_words_size = np.shape(set_of_unique_words)[0]
    print "unique_words_size size ::::", unique_words_size
    lables_size = len(labels_index_dict)
    #num_of_doc = np.shape(bow_reviews_list)[0]
    
    labelwise_word_arr = np.zeros((lables_size, unique_words_size))
    
    for i in range(0,len(bow_reviews_list)):
        for j in range(0, len(bow_reviews_list[i])):
            if bow_reviews_list[i][j] != '':
                index = word_index_dict[bow_reviews_list[i][j]]
                for label in labels_arr[i]:
                    labelwise_word_arr[labels_index_dict[label]][index] += 1

    return labelwise_word_arr
    
def get_labelindex_dict(lables_arr):
    
    unique_labels = np.unique(lables_arr)
    labels_index_dict = dict()
    
    count = 0
    for label in unique_labels:
        labels_index_dict[label] = count
        count +=1 
       
    return labels_index_dict


def get_unique_words(bow_reviews_list):
    
    global word_dict
    count = 0
    unique_words = []
    for review in bow_reviews_list: unique_words.extend(review)
    
    unique_words = np.unique(unique_words)
    unique_words = np.delete(unique_words,0)

    for word in unique_words:
        if word != '':
            word_dict[word] = count
            count += 1
    return unique_words, word_dict