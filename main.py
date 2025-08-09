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

parser.add_argument(
    "--package_search",
    nargs=1,
    help="Baixa algum arquivo do repositório de dados abertos da UFRN a partir do nome dele",
)
# TO-DO: fazer o parsing do argumento package_search com os subcomandos de procurar uma substring no url dos pacotes
package_search = subparsers.add_parser(
    "package_search",
    help="Baixa algum arquivo do repositório de dados abertos da UFRN a partir do nome dele",
)
package_search.add_argument(
    "-s",
    "--substring",
    help="Procura por uma substring (nome do dataset) em meio a todos os datasets",
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

if args.package_search is not None:
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
