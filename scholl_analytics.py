import random
import numpy as np

school = []
letters = ['a','b','c','d']
classes = [1,2,3,4,5,6,7,8,9,10,11]
school_class_names = []

def generate_class_name():

    is_generated = False 

    while not is_generated:

        random.shuffle(letters)
        random.shuffle(classes)

        new_name = str(classes[0]) + letters[0].upper()

        if new_name not in school_class_names:
            is_generated = True 
            school_class_names.append(new_name)

    return new_name        

def get_class(num_people):

    class_info = {}

    class_info['class_name'] = generate_class_name() 
    class_info['scores'] = [int(random.randint(2,5)) for i in range(num_people)]

    return class_info

def initialize_school(num_classes, description_mode = False):

    if num_classes >= len(letters) * len(classes):
        print(' Our school is not so big for ' + str(num_classes) + " classes. Please, descrease the number. ")
        return 

    for index in range(num_classes):
        temp_class = get_class(random.randint(5,25))
        school.insert(index, temp_class)

    if description_mode == True:
        for class_index in school:
            print(class_index)


def get_analytics(school):
    all_scores = []
    scores_to_show = []
    print("============================")
    for class_index in school:
        print(class_index.get('class_name'), round(np.mean(class_index.get('scores')), 2))
        all_scores.extend(class_index.get('scores'))
    print("++++++++++++++++++++++++++++")
    print('School', round(np.mean(all_scores),2))
    print("============================")



initialize_school(20, description_mode = True)
get_analytics(school)
