from processamento_dados import Dados


# Leitura
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# Transformação

key_map = {
            'Nome do Item':'Nome do Produto',
            'ClassificaÃ§Ã£o do Produto':'Categoria do Produto',
            'Valor em Reais (R$)':'Preço do Produto (R$)',
            'Quantidade em Estoque':'Quantidade em Estoque',
            'Nome da Loja':'Filial',
            'Data da Venda':'Data da Venda'
        }


# Lendo
dados_empresaA = Dados(path_json, 'json')
print(dados_empresaA.path)

dados_empresaB = Dados(path_csv, 'csv')
print(dados_empresaB.path)

# print(dados_empresaA.get_colunas())
# print(dados_empresaB.get_colunas())

print("qtd linhas EmpA", dados_empresaA.qtd_linhas)
print("qtd linhas EmpB", dados_empresaB.qtd_linhas)



dados_empresaB.rename_colums(key_map)
print(dados_empresaB.nome_colunas)


# Load
dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print("ATQ fusao", dados_fusao.qtd_linhas)
print(dados_fusao.nome_colunas)
# print(dados_fusao.dados)


# path = 'data_processed/dados_final_Class.csv'
# dados_fusao.salvando_dados(path)
# print(path)