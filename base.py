import pandas as pd
import openpyxl, os 

#df = pd.read_excel(r"T:\CLIENTES\GRUPO H2F\CONTROLADORIA\1. RELATÓRIOS FOLHA\Férias\RELAÇÃO DE FÉRIAS 01-2023.xlsx",header=0) #o r é para não travar o caminho na hora de carregar
#print(df)
#_________________________________________________________________________________________________________________________________________________________________


class base_dados():
    def __init__(self): #init colocar no inicio sempre
        self.caminho_ferias= r"T:\CLIENTES\GRUPO H2F\CONTROLADORIA\1. RELATÓRIOS FOLHA\Férias" #em qualquer lugar do código pode ser utilizado - dentro da classe - guiando a pasta de férias
        self.caminho_rescisao= r"T:\CLIENTES\GRUPO H2F\CONTROLADORIA\1. RELATÓRIOS FOLHA\Rescisões"#em qualquer lugar do código pode ser utilizado - dentro da classe - guiando a pasta de rescisões
        self.caminho_admissao= r"T:\CLIENTES\GRUPO H2F\CONTROLADORIA\1. RELATÓRIOS FOLHA\Admissões"#em qualquer lugar do código pode ser utilizado - dentro da classe - guiando a pasta de admissões
        self.caminho_extratos= r"T:\CLIENTES\GRUPO H2F\CONTROLADORIA\1. RELATÓRIOS FOLHA\Extratos"#em qualquer lugar do código pode ser utilizado - dentro da classe - guiando a pasta de extratos
        self.caminho_rubricas= r"T:\CLIENTES\GRUPO H2F\CONTROLADORIA\1. RELATÓRIOS FOLHA\Rubricas"#em qualquer lugar do código pode ser utilizado - dentro da classe - guiando a pasta de rubricas
        self.caminho_extratosbancarios= r"T:\CLIENTES\GRUPO H2F\CONTROLADORIA\1. RELATÓRIOS FOLHA\Extratos Bancários"
        self.caminho_indicadores = r"T:\CLIENTES\GRUPO H2F\CONTROLADORIA\1. RELATÓRIOS FOLHA\Indicadores do DP"



    def ferias(self): #CONSTROI O BANCO DE DADOS FÉRIAS
        self.base_ferias=pd.DataFrame() #tudo será dentro deste data frame vazio - o self no início para transf este parametro em geral 
        listadearquivos_ferias= os.listdir(self.caminho_ferias) #acessar todos os arquivos do diretório/pasta
        for i in listadearquivos_ferias:
            dataframe_basetemporariaf = pd.read_excel(self.caminho_ferias + "\\" + i) # + (concatenar) \\ (o caminho tem barra, ou seja, ele substitui o 2° caractere especial com a \) + (concatenar) i (chamando a função for)
            self.base_ferias= pd.concat([self.base_ferias,dataframe_basetemporariaf]) #para unir todas as planilhas em uma única - concatenar ([base antiga + a base após leitura das planilhas]) 
        
        #PARA LIMPAR A BASE DE DADOS:
        #OPÇÃO 1: self.base.drop(columns= "codi_emp", inplace= True ) ----- # excluir coluna de forma mais COMPLICADA
       ##### OPÇÃO 2: para excluir colunas de forma mais simplificada: Criar um data frame (nomeado como colunasdaplanilhaFOLHA) > entre [colocar o nome de todas as colunas que serão excluídas] > criar um 
       # for i in nome do dataframe > utilizar o nome dado a nova base de dados . drop (self.base.drop) > entre (columns = i (identificando a o nome dado ao dataframe), 
       # inplace = True para preservar a base de dados)
        Colunasdaplanilhaferias = ["codi_emp", "i_depto", "i_ccustos","i_filiais","i_servicos","inicio_gozo", "i_cargos","inicio_aquisitivo", "fim_gozo", "fim_aquisitivo","inicio_abono", "fim_abono",
                              "par_quebra","sq_datafim", "cp_data_hora", "quebra","pago_abono", "sq_nome_emp", "sq_nome_filial", "servico_tipo_insc", "servico_cgc", "tins_emp", "cgce_emp"]
        for i in Colunasdaplanilhaferias:
            self.base_ferias.drop(columns=i, inplace=True)
        #para transpor as colunas, ou seja, para unir colunas > self.base = (a nova base será igual a...) pd.melt(self.base... - pandas . melt comando para transpor > dentro do parenteses estará
        #  a base antiga (self.base, id_ vars que corresponde as colunas que não serão alteradas , value_vars que corresponde as colunas que irão se unir.)
        self.base_ferias=pd.melt(self.base_ferias, id_vars=["i_empregados", "nome", "sq_dataini", "sq_nome_depto", "sq_nome_cargo", "sq_nome_ccustos", "sq_nome_servico"], 
                          value_vars=["valor_abono", "valor_ad_13", "valor_33_ferias", "valor_33_abono", "foferias_valor_inss", "valor_irrf", "valor_remuneracao", "proventos",
                                       "descontos", "cp_outros_descontos"]) 
        self.base_ferias.to_excel("férias jan-mar.xlsx", index=False) #para imprimir a nova base
#___________________________________________________________________________________________________________________________
    def Rescisao(self):#CONSTROI O BANCO DE DADOS RESCISÕES
        self.base_rescisao = pd.DataFrame() #tudo será dentro deste data frame vazio - o self no início é um parametro em geral para ser repetido dentro da classe 
        listadearquivos_rescisao= os.listdir(self.caminho_rescisao)  #acessar todos os arquivos do diretório/pasta
        for i in listadearquivos_rescisao:
            dataframe_basetemporariar = pd.read_excel(self.caminho_rescisao + "\\" + i) # + (CONCATENAR) \\ (o caminho tem barra, ou seja, ele substitui o 2° caractere especial com a \) + (concatenar) i (chamando a função for)
            self.base_rescisao=pd.concat([self.base_rescisao,dataframe_basetemporariar]) #para unir/CONCATENAR todas as planilhas em uma única - concatenar ([base antiga + a base após leitura das planilhas]) 
        #print(self.base_rescisao)
        #LIMPEZA DA PLANILHA:
        ##### OPÇÃO 2: para excluir colunas de forma mais simplificada: Criar um data frame (nomeado como colunasdaplanilhaRESCISAO) > entre [colocar o nome de todas as colunas que serão 
        # excluídas] > criar um for i in nome do dataframe > utilizar o nome dado a nova base de dados . drop (self.base.drop) > entre (columns = i (identificando a o nome dado ao dataframe), 
       # inplace = True para preservar a base de dados)
        Colunasdaplanilharescisao = ["codi_emp", "i_filiais", "i_depto", "i_ccustos", "i_servicos", "i_cargos", "admissao", "data_complemento", "aviso_indenizado", "sq_nome_emp", 
                                     "cp_tins_emp", "cp_cgce_emp", "par_quebra", "sq_datafim", "cp_data_hora", "data_aviso", "demissao", "quebra", "sq_nome_filial", "servico_tipo_insc", "servico_cgc"]
        for i in Colunasdaplanilharescisao:
            self.base_rescisao.drop(columns=i, inplace=True)
        #PARA TRANSPOR O BANCO DE DADOS:
        #para transpor as colunas, ou seja, para unir colunas > self.base = (a nova base será igual a...) pd.melt(self.base... - pandas . melt (comando para transpor) > dentro do parenteses 
        # estará a base antiga (self.base,  id_ vars que corresponde as colunas que não serão alteradas + value_vars que corresponde as colunas que irão se unir.)
        self.base_rescisao = pd.melt(self.base_rescisao, id_vars=["i_empregados", "nome", "motivo", "sq_dataini", "sq_nome_depto", "sq_nome_cargo", "sq_nome_ccustos",
                                                                   "sq_nome_servico"], value_vars=["salario", "saldo_fgts", "fgts_rescisao", "cp_liquido", "complemento_saldo_fgts", "proventos", 
                                                                                                                                 "descontos"])
        self.base_rescisao.to_excel("rescisões jan-mar.xlsx", index=False) #para imprimir a nova base
#__________________________________________________________________________________________________________________________________
    def Admissao(self):#CONSTROI O BANCO DE DADOS ADMISSAO
        self.base_admissao = pd.DataFrame() #tudo será dentro deste data frame vazio - o self no início é um parametro em geral para ser repetido dentro da classe 
        listadearquivos_admissao= os.listdir(self.caminho_admissao) #acessar todos os arquivos do diretório/pasta
        for i in listadearquivos_admissao:
            dataframe_basetemporariaa = pd.read_excel(self.caminho_admissao + "\\" + i) # + (CONCATENAR) \\ (o caminho tem barra, ou seja, ele substitui o 2° caractere especial com a \) + (concatenar) i (chamando a função for)
            self.base_admissao = pd.concat([self.base_admissao,dataframe_basetemporariaa]) #para unir/CONCATENAR todas as planilhas em uma única - concatenar ([base antiga + a base após leitura das planilhas]) 
        #LIMPEZA DA PLANILHA:
        ##### OPÇÃO 2: para excluir colunas de forma mais simplificada: Criar um data frame (nomeado como colunasdaplanilhaADMISSAO) = > entre [colocar o nome de todas as colunas que serão 
        # excluídas] > criar um for i in nome do dataframe: > utilizar o nome dado a nova base de dados . drop (self.base.drop) > entre (columns = i (identificando a o nome dado ao dataframe), 
       # inplace = True para preservar a base de dados)
        Colunasplanilhadeadmissao= ["vinculo", "categoria", "forma_pagto", "horas_mes", "i_cargos", "par_quebra", "quebra","datasituacao", "cp_now", "cp_nome_emp", "servico_tipo_insc",
                                     "servico_cgc", "codi_emp"]
        for i in Colunasplanilhadeadmissao:
            self.base_admissao.drop(columns= i, inplace=True)
        self.base_admissao.to_excel("Admissões jan-mar.xlsx", index=False)#para imprimir a nova base
#__________________________________________________________________________________________________________________________________
    def Extratos(self):#CONSTROI O BANCO DE DADOS EXTRATOS
        self.base_extratos= pd.DataFrame()#tudo será dentro deste data frame vazio - o self no início é um parametro em geral para ser repetido dentro da classe
        listadearquivos_extratos= os.listdir(self.caminho_extratos)#acessar todos os arquivos do diretório/pasta
        for i in listadearquivos_extratos:
            dataframe_basetemporariae = pd.read_excel(self.caminho_extratos + "\\" + i) # + (CONCATENAR) \\ (o caminho tem barra, ou seja, ele substitui o 2° caractere especial com a \) + (concatenar) i (chamando a função for)
            self.base_extratos = pd.concat([self.base_extratos, dataframe_basetemporariae]) #para unir/CONCATENAR todas as planilhas em uma única - concatenar ([base antiga + a base após leitura das planilhas])
           
        #LIMPEZA DA PLANILHA:
        ##### OPÇÃO 2: para excluir colunas de forma mais simplificada: Criar um data frame (nomeado como colunasdaplanilhaADMISSAO) = > entre [colocar o nome de todas as colunas que serão 
        # excluídas] > criar um for i in nome do dataframe: > utilizar o nome dado a nova base de dados . drop (self.base.drop) > entre (columns = i (identificando a o nome dado ao dataframe), 
       # inplace = True para preservar a base de dados)
       # Colunasplanilhaextratos= [""]
        Colunasplanilhadeextratos=["codi_emp", "nome_emp", "cgce_emp", "tins_emp", "cp_tipo_calc", "cp_data_hora", "cp_quebra", "cp_pagina_ini", "cp_label", "cp_codi_epr", "cp_cpf", "cp_codi_car", "cp_vinculo",
                                    "cp_cc", "cp_depto", "cp_filial", "cp_admissao", "cp_codi_eve_p", "cp_eve_pod_p", "cp_eve_pod_d", "cp_compoe_liquido_p", "cp_aparece_recibo_p", "cp_compoe_liquido_d", 
                                    "cp_aparece_recibo_d", "cp_aparece_relatorio_p","cp_aparece_relatorio_d", "cp_cbo_2002", "cp_horas_mes", "cp_tipo_linha", "quebra_pagina", "linha_ajuste", "ctrl_grupo", 
                                    "row_dados", "linha_rel", "resumo", "zebra", "cp_ponto_para_ajustes", "cp_num_dep", "cp_desr_sep_comp", "cp_desr_sep_3", "cp_titulo_resumo", "cp_no_epr", "cp_no_est", 
                                    "cp_base_inss", "cp_base_irrf", "cp_base_irrf_participacao_lucros", "cp_base_irrf_exterior", "cp_valor_irrf_participacao_lucros", "cp_valor_irrf_exterior", 
                                    "cp_valor_irrf_decimo_terceiro", "cp_situ1", "cp_situ2", "cp_valor_irrf_alugueis", "cp_val_irrf_aut", "cp_situ3", "cp_situ4", "cp_situ5", "cp_situ20_41",
                                    "cp_base_mes_anterior_grfc", "cp_situ6", "cp_valor_mes_anterior_grfc", "cp_situ7", "cp_situ8", "cp_total_inss", "cp_situ9", "cp_base_pis", "cp_situ13", "cp_sal_mat", 
                                    "cp_valor_pis","cp_situ14_15_16", "cp_dedsal_mat13", "cp_situ23", "cp_situ24", "cp_base_iss", "cp_admitidos", "cp_valor_iss", "cp_base_gilrat", "cp_valor_gilrat", 
                                    "cp_base_indenizacao", "cp_valor_indenizacao", "cp_titulo","cp_codi_eve", "cp_nome_eve", "cp_titulo_res_eve", "cp_res_codi_eve_p", "cp_res_eve_p", "cp_res_codi_eve_d", 
                                    "cp_res_eve_d", "cp_res_eve_tit_liq" ,"cp_res_compoe_liquido_p", "cp_res_aparece_recibo_p", "cp_res_aparece_relatorio_p", "cp_res_compoe_liquido_d", "cp_res_aparece_recibo_d",
                                    "cp_res_aparece_relatorio_d", "cp_liq_resumo","cp_base_calculo_inss_receita_bruta", "cp_valor_inss_receita_bruta","cp_data_inicio_afastamento", "cp_data_fim_afastamento",
                                     "cp_afastamento_interrompido_por_morte", "cp_total_contribuintes" ,"cp_complemento_calculo", "cp_grupo_complemento_calculo", "cp_demonstrar_valores_inss_receita_bruta", 
                                     "cp_situ36", "cp_valor_hora_aula_p", "cp_situ39", "percentual_terceiros", "percentual_inss_empresa", "percentual_acidente_trabalho", "percentual_autonomo", "cp_retencoes", 
                                     "cp_compensacoes", "cp_cooperativas", "cp_outras_compensacoes", "cp_situ54_55_56", "cp_texto_valor_inss_receita_bruta", "cp_terceiros_descricao_convenio", "cp_terceiros_valor_convenio"
                                     ,"cp_terceiros_total", "cp_matricula_esocial", "cp_codi_eve_d", "cp_num_fil"]
        for i in Colunasplanilhadeextratos:
            self.base_extratos.drop(columns=i, inplace=True)
 #PARA TRANSPOR O BANCO DE DADOS:
        #para transpor as colunas, ou seja, para unir colunas > self.base = (a nova base será igual a...) pd.melt(self.base... - pandas . melt (comando para transpor) > dentro do parenteses 
        # estará a base antiga (self.base,  id_ vars que corresponde as colunas que não serão alteradas + value_vars que corresponde as colunas que irão se unir.)    
        self.base_extratos= pd.melt(self.base_extratos, id_vars=["cp_competencia", "cp_nome_epr", "cp_nome_car", "cp_nome_eve_p", "cp_nome_eve_d", "cp_desr_sep", "cp_desr_sep_2", "cp_sit_epr", "cp_res_nome_eve_p",
                                                                  "cp_res_nome_eve_d", "cp_desc_afastamento"], value_vars=["cp_salario", "cp_eve_inf_p", "cp_eve_val_p", "cp_eve_inf_d", "cp_bas_inss", "cp_exc_inss"
                                                                                                                           , "cp_bas_fgts", "cp_val_fgts", "cp_bas_irrf", "cp_base_inss_empregado", 
                                                                                                                           "cp_base_inss_contribuinte", "cp_base_irrf_mensal", "cp_base_irrf_ferias","cp_base_irrf_decimo_terceiro", 
                                                                                                                           "cp_valor_irrf_mensal" ,"cp_valor_irrf_ferias","cp_exce_inss","cp_val_irrf","cp_base_total","cp_val_segurad","cp_base_fgts"
                                                                                                                           ,"cp_val_empresa","cp_valor_fgts","cp_acid_trab","cp_inss_terc","cp_inss_auto","cp_base_grfc",
                                                                                                                           "cp_valor_grfc","cp_sal_fam","cp_total_desc","cp_liq_inss","cp_prov","cp_desc", "cp_liqu","cp_prov_total"
                                                                                                                           ,"cp_desc_total","cp_liqu_total","cp_tot_geral_prov","cp_tot_geral_desc","cp_tot_geral_liq","cp_res_eve_inf_p"
                                                                                                                           ,"cp_res_eve_val_p","cp_res_eve_inf_d","cp_res_eve_val_d","cp_res_eve_liquido","cp_liquido","cp_base_fgts_aprendiz"
                                                                                                                           ,"cp_valor_fgts_aprendiz"])      
# PARA DELETAR LINHAS COM VALOR "0" ou "N/A" - Reduzir linhas da base de dados
        self.base_extratos.dropna(subset=["value"], inplace=True) 
#PARA IMPRIMIR A NOVA BASE DE DADOS
        self.base_extratos.to_excel("Extratos Jan-Mar.xlsx", index=False)
        
#__________________________________________________________________________________________________________________________________
    #PARA CONSTRUIR O BANCO DE DADOS:    
    def Rubricas(self):
        self.base_rubricas = pd.DataFrame() #Criação de um Data Frame fazio - tudo será dentro deste data frame vazio - o self no início é um parametro em geral para ser repetido dentro da classe
        listadearquivos_rubricas= os.listdir(self.caminho_rubricas) #acessar todos os arquivos do diretório/pasta
        for i in listadearquivos_rubricas:
            dataframe_basetemporariar = pd.read_excel(self.caminho_rubricas + "\\"+ i, usecols= ["cp2_prov_desc", "cp3_nome_evento", "cp3_valor_calc","cp_competencia"]) # o data frame temporário irá ler os arquivos na pasta indicada acima atraves do "self.caminho...." + as barras servem para anular as \ no endereço/caminho da pasta, substituindo o 1° pelo 2° + i que indica a lista de arquivos que ele irá concatenar, usecols [ para identificar as colunas que serão utilizadas]
            self.base_rubricas = pd.concat([self.base_rubricas, dataframe_basetemporariar]) #irá unir/concatenar todas as planilhas da pasta, transformando tudo em uma única planilha - ([base antiga, base temporaria pós leitura das planilhas])

    #LIMPEZA DA PLANILHA:
        ##### OPÇÃO 2: para excluir colunas de forma mais simplificada: Criar um data frame (nomeado como colunasdaplanilhaADMISSAO) = > entre [colocar o nome de todas as colunas que serão 
        # excluídas] > criar um for i in nome do dataframe: > utilizar o nome dado a nova base de dados . drop (self.base.drop) > entre (columns = i (identificando a o nome dado ao dataframe), 
       # inplace = True para preservar a base de dados)
       # Colunasplanilhaextratos= [""]
        #self.base_rubricas.drop_duplicates(subset=["cp3_codigo_evento", "cp3_nome_evento"])
        #self.base_rubricas.drop(index=1, inplace=True)
        '''base_rubricas = list(self.base_rubricas)
        for i in base_rubricas: 
            base_rubricas[i]= self.transformar_moeda(base_rubricas, i, "cp3_valor_calc")
            base_rubricas[i]=base_rubricas[i].replace('R$ nan', "R$ -")'''



        #self.base_rubricas.dropna(subset=["cp3_nome_evento", "cp3_valor_calc", "cp2_prov_desc"], inplace=True) 

        self.base_rubricas.to_excel("Rubricas Utilizadas Jan-Mar.xlsx", index=False)
     
    #PARA CONSTRUIR O BANCO DE DADOS:    CSV 
    def ExtratosBancarios(self):
        self.base_extratosbancarios = pd.DataFrame()
        coluna = ["a","data","c","valor","d","nome","e","f","g","h","i","j","k"] #Quantidade de colunas
        arquivoextratosbancarios = os.listdir(self.caminho_extratosbancarios)
        for i in arquivoextratosbancarios:
            dataframe_basetemporaria = pd.read_csv(self.caminho_extratosbancarios + "\\" + i, sep= "|", usecols=[2,5,7], encoding="ISO-8859-1", header=2)
            
            self.base_extratosbancarios= pd.concat([self.base_extratosbancarios,dataframe_basetemporaria])
        self.base_extratosbancarios.to_excel("Extratos Bancários Dez-Jan.xlsx", index=False)

#__________________________________________________________________________________________________________________________________

    def IndicadoresDP(self):
        self.base_indicadoresdp = pd.DataFrame()
        listadearquivos_indicadores = os.listdir(self.caminho_indicadores)
        for i in listadearquivos_indicadores:
            dataframe_basetemporariai = pd.read_excel(self.caminho_indicadores + "\\" + i, usecols= ["Competencia", "SITUAÇÃO", "TRATATIVA"])
            self.base_indicadoresdp = pd.concat([self.base_indicadoresdp, dataframe_basetemporariai])

            self.base_indicadoresdp["Competencia"] = pd.to_datetime(self.base_indicadoresdp["Competencia"],format="%d/%m/%Y")
            
            
            #PARA CRIAR UMA BASE DE DADO A PARTIR DE ABAS DE UMA BASE DE DADOS ESPECÍFICA 
           # abasdaplanilhadeindicadores = pd.ExcelFile(self.caminho_indicadores + "\\" + i, engine= "openpyxl")
           #print(abasdaplanilhadeindicadores.sheet_names)
            #for j in abasdaplanilhadeindicadores.sheet_names:
              #  indicadoresabas = pd.read_excel(self.caminho_indicadores + "\\" + i, sheet_name=j,engine= "openpyxl")
              #  if "012023" in j or "022023" in j:
              #      self.base_indicadoresdp = pd.concat([self.base_indicadoresdp, indicadoresabas])
              #  else: 
              #      pass

        self.base_indicadoresdp.to_excel("Indicadores do dp jan-dez.xlsx", index=False)
        



















Chamadordafunção=base_dados() #as próximas funções serão chamadas abaixo desta primeira. 
#Chamadordafunção.ferias()
#Chamadordafunção.Rescisao()
#Chamadordafunção.Admissao()
#Chamadordafunção.Extratos()
Chamadordafunção.Rubricas()
#Chamadordafunção.ExtratosBancarios()
#Chamadordafunção.IndicadoresDP()


