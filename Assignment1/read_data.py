import utils
hotel_reviews_train_data = []
train_label_data = []


def read_data(train_text_filename, train_label_data_filename):
    global hotel_reviews_train_data
    global train_label_data
    with open(train_text_filename) as f:
        train_data = f.read().splitlines()
    
    for item in train_data: hotel_reviews_train_data.append(item.split(" ", 1))
    
    with open(train_label_data_filename) as f:
        label_data = f.read().splitlines()

    for item in label_data: train_label_data.append(item.split(" "))
    
    train_label_data = utils.remove_columns_from_array(train_label_data, [0])
    hotel_reviews_train_data = utils.extendarray_columnwise(hotel_reviews_train_data, train_label_data)
    
    return hotel_reviews_train_data, train_label_data

