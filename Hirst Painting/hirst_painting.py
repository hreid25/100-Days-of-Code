import os
import colorgram
# be able to change the size of the dot on the screen
# extract colors from the image using colorgram

colors = colorgram.extract('C://Users//haydr//100 Days of Code///Hirst Painting//damien_hirst.jpg', 10)

rgb_list = [i.rgb for i in colors]
lst_of_tuples = []
for value in rgb_list:
    lst_of_tuples.append(tuple((rgb_list[0].r,rgb_list[0].g,rgb_list[0].b)))
print(lst_of_tuples)