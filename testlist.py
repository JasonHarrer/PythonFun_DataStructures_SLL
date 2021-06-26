#!/usr/bin/env python

from list import List

if __name__ == '__main__':
    my_list = List()
    my_list.remove_from_back()
    my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("not").add_to_back("fun!").print_values()
    my_list.insert_at("is", 1).insert_at("am", 2).remove_val("not").print_values()
    #my_list.insert_at("is", 1).insert_at("am", 2)
    my_list.insert_at("I think", 0).insert_at("Really!!!", 6).insert_at("NOT!", 10).print_values()
