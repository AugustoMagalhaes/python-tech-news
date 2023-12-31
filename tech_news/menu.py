import sys


# Requisito 12
def analyzer_menu():
    input_option = input(
      "Selecione uma das opções a seguir:\n"
      " 0 - Popular o banco com notícias;\n"
      " 1 - Buscar notícias por título;\n"
      " 2 - Buscar notícias por data;\n"
      " 3 - Buscar notícias por tag;\n"
      " 4 - Buscar notícias por categoria;\n"
      " 5 - Listar top 5 notícias;\n"
      " 6 - Listar top 5 categorias;\n"
      " 7 - Sair.\n"
    )

    case_options = {
      "0": "Digite quantas notícias serão buscadas:",
      "1": "Digite o título:",
      "2": "Digite a data no formato aaaa-mm-dd:",
      "3": "Digite a tag:",
      "4": "Digite a categoria:"
    }

    if input_option in case_options.keys():
        print(case_options[input_option])
        return case_options[input_option]
    else:
        sys.stderr.write("Opção inválida")
