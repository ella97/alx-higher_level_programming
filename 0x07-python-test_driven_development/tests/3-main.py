#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Doe")
say_my_name("David", "Sailor")
say_my_name("Junior")
try:
    say_my_name(12, "Doe")
except Exception as e:
    print(e)
