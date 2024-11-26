import csv, json

class Dados:

    # crianndo o construtor
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.get_colunas()
        self.qtd_linhas = self.size_data()

    def ler_json(self):
        dados_json = []
        with open(self.path, 'r') as file:
            dados_json = json.load(file)

        return dados_json


    def ler_csv(self):
        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)

        return dados_csv


    def leitura_dados(self):
        if self.tipo_dados == 'csv':
            dados = self.ler_csv()
        
        elif self.tipo_dados == 'json':
            dados = self.ler_json()
        
        elif self.tipo_dados == 'list':
            dados = self.path
            self.path = 'path em memoria'
        
        return dados

    def get_colunas(self):
         return list(self.dados[-1].keys())
    
    def rename_colums(self, key_map):
    # atualizar os nome no CSV de acordo com os dados JSON
        new_dados = []
        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_map[old_key]] = value
            new_dados.append(dict_temp)
        # não retorno atribue dados
        self.dados =  new_dados
        self.nome_colunas = self.get_colunas()

    def size_data(self):
        return len(self.dados)
    
    
    def join(dadosA, dadosB):
        combina_list = []
        combina_list.extend(dadosA.dados)
        combina_list.extend(dadosB.dados)

        return Dados(combina_list,'list') 


    def transforma_dados_tabela(self):
    # se o data da venda não tiver disponível nos dados, substituir a string "indisponível"
        dados_combinados_tabela = [self.nome_colunas]
        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'Indisponivel'))
                dados_combinados_tabela.append(linha)
        return dados_combinados_tabela



    def salvando_dados(self, path):
        dados_tranformado_tabela  = self.transforma_dados_tabela()
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_tranformado_tabela)