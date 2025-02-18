import pandas as pd
from datetime import datetime

list = []
valorInicial = 360000.0  

def calc(valor, taxa_diaria, dias_passados):
    global valorInicial
    valor_corrigido = valor * taxa_diaria * dias_passados
    print(f'Correção de {dias_passados} dias: {valor_corrigido:.4f}')
    list.append(valor_corrigido + valorInicial)
    valorInicial += valor_corrigido
    print(f'Novo valor Inicial após correção: {valorInicial:.3f}')

df = pd.read_excel('taxas_corrigidas.xlsx')

while True:
    data_atual = datetime.now()
    data_formatada = datetime.strptime(data_atual.strftime('%d/%m/%Y'), '%d/%m/%Y')
    data_Parcela = datetime(2025, 2, 1)
    dias_passados = data_formatada - data_Parcela
    dias_passados = dias_passados.days  
    mes_atual = data_atual.strftime('%Y-%m')
    taxa_atual = df.loc[df['Mês'] == mes_atual, 'Taxa de Correção'].values
    
    if len(taxa_atual) > 0:
        valorIncc = float(taxa_atual[0]) 
        print(f'Taxa de correção para o mês {mes_atual}: {valorIncc}%')
    else:
        print(f"Taxa de correção para o mês {mes_atual} não encontrada!")
        valorIncc = 0
    taxa_diaria = (valorIncc / 100) / 30


    calc(valorInicial, taxa_diaria, dias_passados)

    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        print("Saindo do programa...")
        break
