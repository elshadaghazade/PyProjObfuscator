import argparse, obfuscator

argp = argparse.ArgumentParser(description='Python Project Obfuscator is for obfuscate any type of Python project.')
argp.add_argument('-p', '--path', type=str, help='Path of the project folder')
argp.add_argument('-d', '--dist', default='dist', type=str, help='Destination folder where obfuscated project files will be copied. By default it is ./dist')
argp.add_argument('-v', '--version', nargs='?', const='1.0.0-rc-1', help='Version')
args = argp.parse_args()

def main():
    if args.version:
        return print("Python Project Obfuscator " + args.version)
    
    if not args.path:
        argp.print_help()
    elif args.path:
        obfuscator.obfuscate(args.path, args.dist)