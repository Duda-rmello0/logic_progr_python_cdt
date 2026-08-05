arquivo_read = open('arquivo_leitura.txt', 'r') 

conteudo_arquivo = arquivo_read.readlines()

print(conteudo_arquivo[5].strip())
print(conteudo_arquivo[7].strip())

arquivo_read.close()