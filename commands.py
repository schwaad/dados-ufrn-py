import subprocess
import json
import utils


def show_packages():
    result = subprocess.run(
        ["curl", "-s", "https://dados.ufrn.br/api/3/action/package_list"],
        capture_output=True,
        text=True,
    )
    output = result.stdout
    print(output[output.find("[") + 1 : -2])


def package_search(args):
    if len(args) == 1:
        url = (
            'https://dados.ufrn.br/api/3/action/package_search?q="'
            + str(args.package_search[0])
            + '"'
        )
        result = subprocess.run(["curl", "-s", url], capture_output=True, text=True)
        output = result.stdout
        data = json.loads(output)

        todas_urls = utils.extrair_urls(data)

        for url in todas_urls:
            print(url)
    if len(args) == 2:
        url = (
            'https://dados.ufrn.br/api/3/action/package_search?q="'
            + str(args.package_search[0])
            + '"'
        )
        result = subprocess.run(["curl", "-s", url], capture_output=True, text=True)
        output = result.stdout
        data = json.loads(output)

        todas_urls = utils.extrair_urls(data)

        for url in todas_urls:
            if args.package_search[1] in url:
                print(url)
