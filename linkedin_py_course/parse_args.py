from argparse import ArgumentParser

parser = ArgumentParser()

output_help = 'Example of printing out the file name entered in the command line arguments.'
text_help = 'The text to write to a file.'

parser.add_argument('--output', '-o', required=True, help=output_help)
parser.add_argument('--text','-t',required=True, help=text_help)

args = parser.parse_args()

with open(args.output, 'w') as file:
    file.write(args.text+'\n')

print(f'Wrote "{args.text}" to file "{args.output}"')


## To run:
# python .\parse_args.py -o .\resources\example_write.txt -t "This is an example"
# python .\parse_args.py --output .\resources\example_write.txt -t "This is an example"
# python .\parse_args.py -o .\resources\example_write.txt --text "This is an example"
# python .\parse_args.py -output .\resources\example_write.txt --text "This is an example"