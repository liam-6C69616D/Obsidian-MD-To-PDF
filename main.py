import argparse
import PDFGen

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, action='store', help='The input md file', metavar='<input_file>')
    parser.add_argument('-o', '--output', action='store', help='The output pdf file name: `output.pdf` by default', default='output.pdf', metavar='<output_file>')
    args = parser.parse_args()

    inExt = args.input[len(args.input) - 3:len(args.input)]
    if inExt != '.md':
        print('main.py: error: argument -i/--input: Input file must have extension `.md`')
        exit(1)

    outExt = args.output[len(args.output) - 4:len(args.output)]
    if outExt != '.pdf':
        print('main.py: error: argument -o/--output: Output file must have extension `.pdf`')
        exit(1)

    pdf = PDFGen.PDF()
    pdf.add_page()
    pdf.color_background()

    try:
        with open(args.input) as file:
            code_block = False
            for line in file:
                if line != '\n':
                    if line.startswith('#'):
                        count = 0
                        for char in line[0:6]:
                            if char == '#':
                                count += 1
                            else:
                                break
                        pdf.headings(line[count+1:], count)
                    elif line.startswith('```'):
                        code_block = not code_block
                        if code_block:
                            running_text = ''
                        else:
                            pdf.snippet(running_text)
                    elif code_block:
                        running_text = running_text + line
                    else:
                        pdf.normal_text(line)
    except IOError:
        print('main.py: error: argument -i/--input: Input file `{0}` doesnt exist'.format(args.input))

    pdf.set_author('Obsidian MD to PDF')

    try:
        pdf.output(args.output, 'F')
    except PermissionError:
        print('main.py: error: Opening PDF: Close output file `{0}` before running'.format(args.output))
