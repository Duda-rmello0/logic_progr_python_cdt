'''
javascript object notation (JSON)
'''



import json



with open('arquivo_leitura_em_json_maariaeduardamello.json', 'r') as arquivo:
    dados_arquivo = json.load(arquivo)



dados_formatados = []



for item in dados_arquivo:

    aluno_formatado = {
        "Nome completo": item.get ("nome") or item.get ("Nome completo"),
        "idade": item.get ("idade"),
        "CEP": item.get ("cep") or item.get ("CEP"),
        "ResgMatr": item.get ("RestMatr") or item.get ("ResgMatr"),
        "E-Mail": item.get ("email") or item.get ("E-Mail")
    }
    dados_formatados.append(aluno_formatado)



    with open('alunos_indicadores.json', 'w', 
    encording= 'utf-8') as novo_arquivo:
        json.dump(dados_formatados, novo_arquivo,
        ensure_ascii=False, indent=2)

    print("Novo arquivo 'alunos_indicadores.json' criado com sucesso!")