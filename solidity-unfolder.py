#!/usr/bin/env python3
import argparse
import os
import re
import sys


def parse_arguments():
  parser = argparse.ArgumentParser(description="Unfolds all local imports in a solidity file to generate a flat solidity file.\nPut the output file into out/ folders.", formatter_class=argparse.RawTextHelpFormatter)
  parser.add_argument("file", type=str, metavar="*.sol", help="target filename with imports")
  parser.add_argument("version", type=str, metavar="*.*.*", help="solidity compiler version e.g. 0.4.24")
  parser.add_argument("-o", "--output", type=str, metavar="*.sol", help="output filename (default: flat.sol)")
  args = parser.parse_args()

  return args


def is_sol_valid(infile, s):
  if ".sol" != infile[-4:]:
    print("{} file is not a solidity file!!!".format(s))
    sys.exit(-2)


def unfold_imports(imports, infile):
  buffer = []

  if infile not in imports:
    with open(infile, "r+") as f:
      for line in f:
        # Remove the pragma line in all imports
        if "pragma" in line[:6]:
          continue

        # Read the imports
        if "import" in line[:6]:
          match = re.search(r".*[\'|\"](.*)[\'|\"]", line)
          if match:
            dirname = os.path.dirname(infile)
            file = os.path.join(dirname, match.group(1))
            absfile = os.path.abspath(file)

            buffer.append(unfold_imports(imports, absfile))
            imports.append(absfile)
          else:
            print("There's syntax error of import in {}".format(infile))
            sys.exit(-3)
        else:
          buffer.append(line)

  return ''.join(buffer)


def main(args):
  # Check if the solidity compiler version format is valid
  match = re.search(r"\d+\.\d+\.\d+", args.version)
  if not match:
    print("Compiler version is not a valid format")
    sys.exit(-1)

  # Check if the input solidity filename is valid
  is_sol_valid(args.file, "Input")
  dirname = os.path.dirname(os.path.abspath(args.file))
  basename = os.path.basename(os.path.abspath(args.file))

  # Check if the output solidity filename is valid
  if not args.output:
    args.output = basename[:-4] + "-flat.sol"
  is_sol_valid(args.output, "Output")

  infile = args.file
  outfile = os.path.join(OUTPUT_FOLDER, args.output)

  imports = []
  with open(outfile, "w+") as f:
    f.write("pragma solidity ^{};\n".format(args.version))
    f.write(unfold_imports(imports, os.path.abspath(infile)))

  print("Success! Output: {} in the {} folder".format(os.path.basename(outfile), OUTPUT_FOLDER))


if __name__ == "__main__":
  args = parse_arguments()

  OUTPUT_FOLDER = "out/"
  if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

  main(args)