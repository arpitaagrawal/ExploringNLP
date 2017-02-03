import read_data
import tokenise_data
import NaiveBayes
import sys

#hotel_reviews_train_data = read_data.read_data()

train_filename = sys.argv[1]
train_label_filename = sys.argv[2]

hotel_reviews_train_data, train_label_data = read_data.read_data(train_filename, train_label_filename)
bow_reviews_list = tokenise_data.tokenise_data(hotel_reviews_train_data, ["space_tokenization"])


#NaiveBayes.load_from_file()
#NaiveBayes2.create_NB_model(bow_reviews_list, hotel_reviews_train_data[:,[2,-1]])
NaiveBayes.create_NB_model(bow_reviews_list, train_label_data)





