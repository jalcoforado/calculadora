import pandas as pd

# Carregar os dados da planilha
file_path = '/mnt/data/Datacenter.xlsx'
datacenter_data = pd.read_excel(file_path, sheet_name='Datacenter')

# Calcular o custo total anual do datacenter
datacenter_data['Total Anual'] = datacenter_data.iloc[:, 1:13].sum(axis=1)
custo_total_anual = datacenter_data['Total Anual'].sum()

# Definir os percentuais de uso dos recursos
percentuais_uso = {
    'VMs': 0.40,
    'Armazenamento': 0.30,
    'Backup e Recuperação': 0.15,
    'Rede': 0.10,
    'Segurança': 0.05
}

# Calcular a alocação dos custos com base nos percentuais de uso
alocacao_custos = {recurso: custo_total_anual * percentual for recurso, percentual in percentuais_uso.items()}

# Definir uma margem de lucro
margem_lucro = 0.0

# Calcular o custo unitário e o preço de venda
def calcular_custo_unitario_e_preco_venda(custo, carga_trabalho_total):
    custo_unitario = custo / carga_trabalho_total
    preco_venda = custo_unitario * (1 + margem_lucro)
    return custo_unitario, preco_venda

# Exemplo de carga de trabalho total (em horas de CPU, armazenamento em GB, etc.)
carga_trabalho_total = {
    'VMs': 20000,  # horas de CPU
    'Armazenamento': 100000,  # GB
    'Backup e Recuperação': 50000,  # GB
    'Rede': 10000,  # GB transferidos
    'Segurança': 5000  # eventos monitorados
}

# Calcular e exibir os custos unitários e preços de venda para cada recurso
resultados = {}
for recurso, custo in alocacao_custos.items():
    carga = carga_trabalho_total[recurso]
    custo_unitario, preco_venda = calcular_custo_unitario_e_preco_venda(custo, carga)
    resultados[recurso] = {
        'Custo Unitário': custo_unitario,
        'Preço de Venda': preco_venda
    }

# Exibir os resultados
for recurso, valores in resultados.items():
    print(f"{recurso}:")
    print(f"  Custo Unitário: R$ {valores['Custo Unitário']:.2f}")
    print(f"  Preço de Venda: R$ {valores['Preço de Venda']:.2f}")

# Salvar os resultados em um arquivo Excel
resultados_df = pd.DataFrame(resultados).T
resultados_df.to_excel('/mnt/data/Alocacao_Custos_Resultados.xlsx')
