#Sistema Bancario
# Desafio: Criar um sistema bancário simples que permita depósitos, saques e extratos.
texto = """
========================= SISTEMA BANCARIO L.K ========================
Escolha uma opção:
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
====================================================================
"""


saldo = 0
limite = 500
extrato = ""
saques_diarios = 0
NUMERO_SAQUES = 3

while True:
    escolha = int(input(texto))
    
    if(escolha == 1):
        valor = float(input("Digite o valor do deposito:\nR$"))
        if(valor > 0):
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"
            print("Deposito realizado com sucesso!\n")
        else:
            print("Operação falhou! O valor informado é inválido.\n")
    elif(escolha == 2):
        valor = float(input("Digite o valor do saque:\nR$"))
        if(valor <= saldo):
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            saques_diarios += 1
            print("Saque realizado com sucesso!\n")
        elif(saques_diarios == NUMERO_SAQUES):
            print("Operação falhou! Número máximo de saques diários excedido.\n")
        else:
            print("Operação falhou! Saldo insuficiente.\n")
    elif(escolha == 3):
        print("\n==================== EXTRATO ====================\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("==================================================\n")
    elif(escolha == 4):
        print("\nObrigado por usar nosso sistema bancário. Até logo!")
        break
        
        
        

