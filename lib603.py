#!/usr/bin/env python

def make_string(listobj, glue=', '):
    print glue.join(str(x) for x in listobj)

def main():
    make_string(range(50))
    make_string(range(50), ' + ')
    make_string(('1', '2', 'abc'), ' + ')

main()
