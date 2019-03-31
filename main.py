# here are some sample queries that our program should return 
# a relevant piece of code for
common_queries = [
    # loops
    "for loop",
    "while loop",
    "nested loop",
    "do...while loop",
    
    # loop control
    "break statements",
    "continue statement",
    "goto statement",
    "infinite loop",

    # file handling
    "open file",
    "read file",
    "write to file",
    "append file",
    "close file",

    # string handling
    "length of string",
    "reverse a string",
    "split a string",
    "remove item from list",
    "copy one string to another",
    "append one string to another",
    "return the length of the string",
    "compare two buffers",
    "convert a string to a floating-point value",
    "convert a string to an integer",
    "convert a string to a signed integer",
    "convert a string to an unsigned integer",
    
    # functions of lists and strings
    "function that returns the largest element in a list",
    "function that reverses a list, preferably in place",
    "function that checks whether an element occurs in a list",
    "function that returns the elements on odd positions in a list",
    "function that computes the running total of a list",
    "function that tests whether a string is a palindrome",

    # i/o
    "prompt the user",
    "print an output",   
    "write to console",
    
    # arrays
    "initialize array",
    "print shortest path",
    "resize an array",

    #JavaScript specific
    "return the response from an asynchronous call",
    "closure inside loops",
    "binding on dynamically created elements",
    "access / process (nested) objects, arrays or JSON",
    "get query string values",
    "this keyword",
    "upload files asynchronously",
    "pass variables and data from PHP to JavaScript",
    "prop() vs attr()",
    "redirect to another webpage",
    "validate an email address",
    "randomize an array",
    "replace all occurrences of a string",
    "copy to the clipboard",
    "clone an object",
    "compare two dates",
    "detect a click outside an element",
    "sorting an array of objects by property",
]
import json
# READING
json_string = open("data.json").read()
json_obj = json.loads(json_string)


for language in json_obj["data"].keys():
    for command in json_obj["data"][language].keys():
        print(command)


# WRITING
json_obj["data"]["Python"]["for loop"]="blah blah"
file_out = open("data.json", "w")
file_out.write(json.dumps(json_obj))