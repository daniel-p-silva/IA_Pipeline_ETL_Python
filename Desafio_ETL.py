# Projeto - Explorando IA Generativa em um Pipeline de ETL com Python

import openai
import pandas as pd

# Configura a chave da API do ChatGpt
openai.api_key = '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'

# Função generate_ai_news responsável por gerar mensagens/sugestões para aumentar o limite de crédito 
def generate_ai_news(user_id):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um especialista em cartão de crédito."},
                {"role": "user", "content": f"Crie uma mensagem para {user_id} orientando como aumentar o limite do cartão de credito (máximo de 100 caracteres)"}
            ]
        )
        return completion.choices[0].message['content'].strip('\"')

# Lê os dados do CSV
tabela = pd.read_csv('C:/Users/danie/Desktop/DIO/Projeto ETL/ETL_BD.CSV')

# Itera sobre as 3 primeiras linhas
for index, row in tabela.head(3).iterrows():
    sugestao = generate_ai_news(row['user_id'])
    tabela.at[index, 'sugestao_aumento_limite'] = sugestao
 

# Salva a atualização no CSV
tabela.to_csv('C:/Users/danie/Desktop/DIO/Projeto ETL/ETL_BD.CSV', index=False)



