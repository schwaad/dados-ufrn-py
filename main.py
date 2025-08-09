import argparse
import subprocess
import json


def extrair_urls(obj):
    urls = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "url":
                urls.append(v)
            else:
                urls.extend(extrair_urls(v))
    elif isinstance(obj, list):
        for item in obj:
            urls.extend(extrair_urls(item))
    return urls


# Instantiate the parser
parser = argparse.ArgumentParser(description="Optional app description")
subparsers = parser.add_subparsers(dest="command")


parser.add_argument(
    "--show_packages",
    action="store_true",
    help="Mostra todos os packages dos dados abertos da UFRN.",
)

package_search = subparsers.add_parser(
    "package_search",
    help="Mostra todos os arquivos dentro de um pacote ou um arquivo específico dentro do pacote a partir de uma substring",
)

package_search.add_argument(
    "package_search",
    nargs="+",
    help="Nome do pacote + nome do dataset dentro do pacote",
)

args = parser.parse_args()

if args.show_packages:
    result = subprocess.run(
        ["curl", "-s", "https://dados.ufrn.br/api/3/action/package_list"],
        capture_output=True,
        text=True,
    )
    output = result.stdout
    print(output[output.find("[") + 1 : -2])

if args.command == "package_search" and len(args.package_search) == 1:
    url = (
        'https://dados.ufrn.br/api/3/action/package_search?q="'
        + str(args.package_search[0])
        + '"'
    )
    result = subprocess.run(["curl", "-s", url], capture_output=True, text=True)
    output = result.stdout
    data = json.loads(output)

    todas_urls = extrair_urls(data)

    for url in todas_urls:
        print(url)

if args.command == "package_search" and len(args.package_search) == 2:
    url = (
        'https://dados.ufrn.br/api/3/action/package_search?q="'
        + str(args.package_search[0])
        + '"'
    )
    result = subprocess.run(["curl", "-s", url], capture_output=True, text=True)
    output = result.stdout
    data = json.loads(output)

    todas_urls = extrair_urls(data)

    for url in todas_urls:
        if args.package_search[1] in url:
            print(url)
