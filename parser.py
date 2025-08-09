import argparse
import commands

parser = argparse.ArgumentParser(
    description="Ferramenta para baixar arquivos da base de dados aberta da UFRN via terminal"
)

subparsers = parser.add_subparsers(dest="command")

show_packages = subparsers.add_parser(
    "show_packages",
    help="Mostra todos os packages dos dados abertos da UFRN.",
)

package_search = subparsers.add_parser(
    "package_search",
    help="Mostra todos os arquivos dentro de um pacote ou um arquivo específico dentro do pacote a partir de uma substring",
)

package_search.add_argument(
    "package_search",
    nargs="+",
    help="Nome do pacote + substring",
)

download_file = subparsers.add_parser(
    "download_file", help="Baixa um arquivo de dentro de um pacote"
)

download_file.add_argument(
    "download_file", nargs="+", help="Nome do pacote + nome do arquivo"
)

args = parser.parse_args()


def run_parser(args):
    if args.command == "show_packages":
        commands.show_packages()
    if args.command == "package_search":
        commands.package_search(args.package_search)
    if args.command == "download_file":
        commands.download_file(args.download_file)
