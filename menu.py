import os
from database.insert_database import *
from database.list_database import *
from database.edit_database import *
from database.delete_database import *

from models.funcionario import Funcionario
op =0


def menu():
        print('1 - Cadastrar Cargo\n')
        print('2 - Cadastrar Empresa\n')
        print('3 - Cadastrar Funcionario\n')
        print('4 - Editar Cargo\n')
        print('5 - Editar Empresa\n')
        print('6 - Editar Funcionario\n')
        print('7 - Excluir Cargo\n')
        print('8 - Excluir Empresa\n')
        print('9 - Excluir Funcionario\n')
        print('10 - Listar Cargo\n')
        print('11 - Listar Empresa\n')
        print('12 - Listar Funcionario\n')
        print('0 - Sair\n')



while op == 0:
    menu()
    entrada = input('Digite aqui: ')
    if entrada.isdigit():
        op = int(entrada)
    elif op == 0:
        break
    else:
        print('Entrada inválida! Por favor, digite um número entre 1 e 13.')
        continue  # Pula para a próxima iteração do loop sem limpar a tela
        
    os.system('cls')
    match op:
        case 1:
            cargo = input('Digite o cargo ')
            insert_cargo(cargo)
            os.system('cls')
            op = 0
            
        case 2:
            empresa = input('Digite o Empresa ')
            insert_empresa(empresa)
            os.system('cls')
            op = 0
        case 3:
            nome = input('Digite o nome ')
            sobrenome = input('Digite o sobrenome ')
            email = input('Digite o email ')
            funcionario = Funcionario(id,nome,sobrenome,email)
            insert_funcionario(funcionario)
            op = 0
        case 4:
            os.system('cls')
            list_cargo()
            id_alter_cargo = input('Digite o id do cargo que deseja alterar !')
            edit_cargo(id_alter_cargo)
            op = 0
        case 5:
            os.system('cls')
            list_empresa()
            id_alter_empresa = input('Digite o id da empresa que deseja alterar !')
            edit_empresa(id_alter_empresa)
            op = 0
        case 6:
            os.system('cls')
            list_funcionario()
            id_alter_funcionario = input('Digite o id do funcionario que deseja alterar !')
            edit_funcionario(id_alter_funcionario)
            op = 0
        case 7:
            os.system('cls')
            list_cargo()
            id_delete_cargo = input('Digite o id do cargo que deseja deletar !')
            delete_cargo(id_delete_cargo)
            op = 0
        case 8:
            os.system('cls')
            list_empresa()
            id_delete_empresa = input('Digite o id do empresa que deseja deletar !')
            delete_empresa(id_delete_empresa)
            op = 0
        case 9:
            os.system('cls')
            list_funcionario()
            id_delete_funcionario = input('Digite o id do funcionario que deseja deletar !')
            delete_funcionario(id_delete_funcionario)
            op = 0
        case 10:
            os.system('cls')
            list_cargo()
            op = 0
            input("Pressione Enter para continuar...")
        case 11:
            os.system('cls')
            list_empresa()
            op = 0
            input("Pressione Enter para continuar...")
        case 12:
            os.system('cls')
            list_funcionario()
            op = 0
            input("Pressione Enter para continuar...")
        case 0:
            break

        
        case _:
            print(op)


