import numpy as np

hotel_reviews_train_data = []

train_label_data_filename = "data/train-labels.txt"
train_text_filename = "data/train-text.txt"


def read_data():
    global hotel_reviews_train_data
    with open(train_text_filename) as f:
        complete_data = f.read().splitlines()
    train_data = complete_data[0:960]
    test_data = complete_data[960:-1]
    np.savetxt("data/new-train-text.txt", train_data, '%s')
    np.savetxt("data/new-test-text.txt", test_data, '%s')
    
    label_data = np.loadtxt(train_label_data_filename,dtype='str')
    train_label_data = label_data[0:960]
    test_label_data = label_data[960:-1]
    np.savetxt("data/new-train-labels.txt", train_label_data, '%s')
    np.savetxt("data/new-test-labels.txt", test_label_data, '%s')
    
read_data()