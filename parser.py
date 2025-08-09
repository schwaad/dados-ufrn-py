import argparse
import commands

parser = argparse.ArgumentParser(description="Optional app description")
subparsers = parser.add_subparsers(dest="command")

package_search = subparsers.add_parser(
    "package_search",
    help="Mostra todos os arquivos dentro de um pacote ou um arquivo específico dentro do pacote a partir de uma substring",
)

show_packages = subparsers.add_parser(
    "show_packages",
    help="Mostra todos os packages dos dados abertos da UFRN.",
)

package_search.add_argument(
    "package_search",
    nargs="+",
    help="Nome do pacote + nome do dataset dentro do pacote",
)

args = parser.parse_args()


def run_parser(args):
    if args.command == "show_packages":
        commands.show_packages()
    if args.command == "package_search":
        commands.package_search(args.package_search)
