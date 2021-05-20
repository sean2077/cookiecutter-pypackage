import argparse

from . import __project_hyphen__


def subcommand1_func(args):
    print(f"subcommand1 received argument a: {args.a}")


def main():
    # create main parser
    parser = argparse.ArgumentParser(
        prog=__project_hyphen__, description="example python cli tool."
    )

    # create subcommands' main parser
    subparser = parser.add_subparsers(title="Commands", metavar="<command>")

    # add subcommands
    ## add subcommand1
    subcommand1 = subparser.add_parser("subcommand1", help="subcommand1.")
    subcommand1.add_argument("-a", help="option of subcommand1")
    subcommand1.set_defaults(func=subcommand1_func)

    # parse args
    args = parser.parse_args()

    # run command
    if hasattr(args, "func"):  # run subcommand
        args.func(args)
    else:  # run main command
        parser.print_help()


if __name__ == "__main__":
    main()
