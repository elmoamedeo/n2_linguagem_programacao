from modelos.musica import Musica
from modelos.pessoa import Pessoa

# Questão 1: Persistência de 2 registros tipo música (PostgreSQL)
Musica.save_psql(Musica('Suns of Gold', 'Leifur James', 'A Louder Silence'))
Musica.save_psql(Musica('Mumma Dont tell', 'Leifur James', 'A Louder Silence'))

# Questão 2: Persistência de 2 registros tipo música (MongoDB)
Musica.save_mongo(Musica('Suns of Gold', 'Leifur James', 'A Louder Silence'))
Musica.save_mongo(Musica('Mumma Dont tell', 'Leifur James', 'A Louder Silence'))


# Questão 4: Fazer um CRUD de uma entidade chamada pessoa.
def crud_pessoa():
    print('---------------------')
    print('1. Salvar Pessoa')
    print('2. Buscar Pessoa')
    print('3. Alterar Pessoa')
    print('4. Deletar Pessoa')
    print('9. Sair')
    opc = int(input('Digite a opção: '))

    if opc == 1:
        nome = input('Digite o nome da pessoa: ')
        cpf = input('Digite o CPF da pessoa: ')
        email = input('Digite o email da pessoa: ')
        Pessoa.save(Pessoa(nome, cpf, email))
        crud_pessoa()
    elif opc == 2:
        cpf = input('Digite o CPF da pessoa que gostaria de buscar: ')
        if Pessoa.search(Pessoa(None, cpf, None)):
            pessoa_buscada = Pessoa.search(Pessoa(None, cpf, None))
            print(
                'Resultados da busca\nNome: {name}\nCpf: {cpf}\nEmail: {email}'.format(name=pessoa_buscada.get('name'),
                                                                                       cpf=pessoa_buscada.get('cpf'),
                                                                                       email=pessoa_buscada.get(
                                                                                           'email')))
        else:
            print('Pessoa não encontrada com o CPF especificado')
        crud_pessoa()
    elif opc == 3:
        cpf = input('Digite o CPF da pessoa que gostaria de alterar: ')
        if Pessoa.search(Pessoa(None, cpf, None)):
            pessoa_old = Pessoa.search(Pessoa(None, cpf, None))
            novo_nome = input('Digite o nome da pessoa (em branco caso não deseje alterar): ')
            if novo_nome.__len__() == 0:
                novo_nome = pessoa_old.get('name')
            novo_cpf = input('Digite o CPF da pessoa (em branco caso não deseje alterar): ')
            if novo_cpf.__len__() == 0:
                novo_cpf = pessoa_old.get('cpf')
            novo_email = input('Digite o email da pessoa (em branco caso não deseje alterar): ')
            if novo_email.__len__() == 0:
                novo_email = pessoa_old.get('email')
            Pessoa.update(Pessoa(None, cpf, None), Pessoa(novo_nome, novo_cpf, novo_email))
        else:
            print('Pessoa não encontrada com o CPF especificado, alteração não efetuada.')
            crud_pessoa()
    elif opc == 4:
        cpf = input('Digite o CPF da pessoa que gostaria de excluir: ')
        if Pessoa.search(Pessoa(None, cpf, None)) is None:
            print('Pessoa não encontrada com esse cpf')
            return crud_pessoa()
        Pessoa.delete(Pessoa(None, cpf, None))
        print('Pessoa deletada com sucesso')
        crud_pessoa()
    elif opc == 9:
        exit()
    else:
        print('Opção inválida')
        crud_pessoa()


crud_pessoa()

# Questão 5: Explique as bibliotecas que você precisou utilizar nas questoes desta prova.
# pymongo/pymongo.errors: Lib que contém arquivos necessários para a conexão e afins do MongoDB / Pacote utilizado para o tratamento mais eficaz das exceções
# psycopg2: Lib que contém arquivos necessários para a conexão e afins do PostgreSQL
# re: Responsável pelo regex, usado neste caso para validar o email

# Questão 6: Explique o que é pip.
# pip é o gerenciador de pacotes do Python, com ele é possível instalar e gerenciar pacotes que não são da biblioteca padrão do Python

# p.s.: Validações e separações adaptadas para fins da entrega da prova