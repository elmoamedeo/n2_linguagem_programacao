import conexoes.conexao_mongo_pessoa as conn_mongo
import re


class Pessoa:

    def __init__(self, name, cpf, email):
        self.name = name
        self.cpf = cpf
        self.email = email

    def save(self):
        if Pessoa.validations(self):
            conn_mongo.save(self.__dict__)
            print('Registro de pessoa salvo com sucesso')

    def search(self):
        return conn_mongo.search(self.cpf)

    def update(self, pessoa):
        if Pessoa.validations_update(pessoa):
            conn_mongo.update(self.cpf, pessoa.__dict__)
            print('Atualização feita com sucesso')

    def delete(self):
        conn_mongo.delete(self.cpf)

    def validations(self):
        if Pessoa.val_name(self) and Pessoa.val_cpf(self) and Pessoa.val_cpf_exist(self) and Pessoa.val_email(self):
            return True
        return False

    def validations_update(self):
        if Pessoa.val_name(self) and Pessoa.val_cpf(self) and Pessoa.val_email(self):
            return True
        return False

    def val_name(self):
        if self.name is None:
            print('Name cannot be null')
            return False

        if len(self.name) > 150:
            print('Name cant have more than 150 chars')
            return False

        return True

    def val_cpf(self):
        cpf = [int(digit) for digit in self.cpf if digit.isdigit()]

        if self.cpf is None:
            print('CPF cannot be null')
            return False

        if len(cpf) != 11:
            print('CPF should have 11 digits')
            return False

        sum_of_products = sum(a * b for a, b in zip(cpf[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10

        if cpf[9] != expected_digit:
            print('Invalid/Incorrect CPF number')
            return False

        sum_of_products = sum(a * b for a, b in zip(cpf[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10

        if cpf[10] != expected_digit:
            print('Invalid/Incorrect CPF number')
            return False

        return True

    def val_cpf_exist(self):
        if conn_mongo.check_if_cpf_exists(self.cpf):
            print('CPF already exists in base')
            return False

        return True

    def val_email(self):
        if self.email is None:
            print('Email cannot be null')
            return False

        if not re.match(r'^[A-Za-z0-9.+_-]+@[A-Za-z0-9._-]+\.[a-zA-Z]*$', self.email):
            print('Email is not valid')
            return False

        return True
