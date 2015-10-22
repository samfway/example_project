#!/usr/bin/env python
import argparse

def interface():
    args = argparse.ArgumentParser()
    '''
    args = argparse.ArgumentParser(
        description='This is what this program does.',
        epilog='This is more information about how this program works.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        Note: Use default=argparse.SUPPRESS to avoid printing 'default: None' 
    '''
    args.add_argument('-i', '--input-file', help='Input file')
    args.add_argument('-o', '--output-file', help='Output file', default='output.txt')
    #args.add_argument('-n', '--some-number', help='Some integer', type=int, default=100)
    args = args.parse_args()
    return args

if __name__=="__main__":
    args = interface()

