import numpy as np

hotel_reviews_train_data = []

train_label_data_filename = "data/new-train-labels.txt"
train_text_filename = "data/new-train-text.txt"


def read_data():
    global hotel_reviews_train_data
    with open(train_text_filename) as f:
        train_data = f.read().splitlines()
    
    for item in train_data: hotel_reviews_train_data.append(item.split(" ", 1))
    train_label_data = np.loadtxt(train_label_data_filename,dtype='str')
    
    hotel_reviews_train_data = np.append(hotel_reviews_train_data, train_label_data[:,[1,-1]], axis=1)
    return hotel_reviews_train_data