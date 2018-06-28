import sys
sys.path.append(sys.path[0] + '/modules/')

import image_generator
import HGU1_Generator
import dir_module
import string_parser

'''        

    dict = {
            "one_line
            "word_list": word_list,
            "char_list": char_list
        }
        
'''

if __name__ == "__main__":


    default_dir = "./data"
    dir_instance = dir_module.Dir_Module(default_dir)
    image_generator_instance =image_generator.Image_Generator(dir_instance)

#    HGU1_Generator.hgu1_image_generator(default_dir)
    # using HanDB


    dict = string_parser.json_file_loader()
    # parsed text using desc.json

    word_list = dict['word_list']
    image_generator_instance.generator(data_list=word_list, font_size=50, mode="word")


    one_line_string_list = dict["one_line_string_list"]
    image_generator_instance.generator(data_list=one_line_string_list, font_size=25, mode="one_line_string")



