from typing import Final

class SistemaBancario:
   __LIMITE_SAQUE: Final[int] = 3
   __AGENCIA = Final[str] = '0001'
   def __init__(self):
      self._saldo = 0
      self._extrato = {'saques': [], 'depositos': []}
      self._numero_saques = 0
      self._usuarios = []
      self._contas = []
      self._numero_contas = 1

   @property
   def limite_saque(self):
      return self.__LIMITE_SAQUE
   
   @property
   def agencia(self):
      return self.__AGENCIA
   
   def filtrar_usuarios(self, cpf):
      usuarios_filtrados = [usuario for usuario in self._usuarios if usuario['cpf'] == cpf]
      return usuarios_filtrados[0] if usuarios_filtrados else None
   
   def criar_usuario(self):
      cpf = input('Informe o CPF (somente números)\n')
      usuario = self.filtrar_usuarios(cpf)
      
      if usuario:
         print('CPF já cadastrado!')
         return
      print('DADOS PESSOAIS')
      nome = input('Nome: ').strip()
      sobrenome = input('Sobrenome: ')
      nome_completo = f'{nome} {sobrenome}'
      dia = input('Dia: ').strip()
      mes = input('Mês: ').strip()
      ano = input('Ano: ').strip()
      data_nascimento = f'{dia}/{mes}/{ano}'
      logradouro = input('Logradouro: ')
      numero = input('Número: ')
      bairro = input('Bairro: ')
      cidade = input('Cidade: ')
      estado = input('Estado (Sigla): ')
      pais = input('País: ')
      endereco = f'{logradouro}, {numero}, {bairro}, {cidade}/{estado}, {pais}'
      senha = input('Crie uma senha: ')
      novo_usuario = {'nome_completo': nome_completo, 'data_nascimento': data_nascimento, 'endereco': endereco,'cpf': cpf, 'senha': senha}
      self._usuarios.append(novo_usuario)
      print('Usuário cadastrado com sucesso!!')

   def criar_conta(self):
      cpf = input('Informe o CPF (somente números)\n')
      usuario = self.filtrar_usuarios(cpf)

      if usuario:
         return self.estrair_usuario(usuario)
      print('Usuário não encontrado!')

   def estrair_usuario(self, usuario):
      print('Conta criada com sucesso!')
      conta = {'agencia': self.__AGENCIA, 'numero': {self._numero_contas}, 'usuario': {usuario}}
      self._contas.append(conta)
      self._numero_contas += 1
      print('Conta criada com sucesso!')
      return
   
   def listar_contas(self):
      for conta in self._contas:
         print(f'Agência: {conta['agencia']} - Número: {conta['numero']} - Titular: {conta['usuario']['nome_completo']}')

   def saque(self, valor=0):
      excedeu_limite = valor > 500
      excedeu_saldo = valor > self._saldo
      excedeu_saque = self._numero_saques >= self.__LIMITE_SAQUE
      if not isinstance(valor, float):
         raise ValueError
      if excedeu_limite:
         print('Operação inválida! Não possível sacar um valor maior que R$ 500.00')
      elif excedeu_saldo:
         print('Operação inválida! Saldo insuficiente!')
      elif excedeu_saque:
         print('Operação inválida! Não é possível fazer mais de 3 saques por dia!')
      else:
         self._saldo -= valor
         self._numero_saques += 1
         print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
         self._extrato['saques'].append(f'Saque de R$ {valor:.2f}')
         self.exibir_extrato()

   def deposito(self, valor=0):
      if not isinstance(valor, float):
         raise ValueError
      self._saldo += valor
      print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
      self._extrato['depositos'].append(f'Depósito de R$ {valor:.2f}\n')
      self.exibir_extrato()

   def exibir_extrato(self):
      print('======Extrato======')
      print('SAQUES:')
      for i, saque in enumerate(self._extrato['saques']):
         print(f'{i + 1} - {saque}')
      print('DEPÓSITOS:')
      for i, deposito in enumerate(self._extrato['depositos']):
         print(f'{i + 1} - {deposito}')
      print(f'Saldo atual R$ {self._saldo:.2f}')

   def menu(self):
      texto = 'MENU'
      while True:
         print(texto.center(21))
         print('\n[1] - Criar usuário\n[2] - Criar conta\n[3] - Listar contas\n[4] - Depositar\n[5] - Sacar\n[6] - Extrato\n[7] - Sair do sistema')
         opcao = input('Escolha o tipo de transação:\n')
         if opcao == '1':
            self.criar_usuario()
         elif opcao == '2':
            self.criar_conta()
         elif opcao == '4':
            valor = float(input('Informe o valor do depósito: '))
            self.deposito(valor)
         elif opcao == '5':
            valor = float(input('Informe o valor do saque: '))
            self.saque(valor)
         elif opcao == '6':
            self.exibir_extrato()
         elif opcao == '7':
            print('Saindo do sistema...')
            break
         else:
            print('Digite uma opção válida!')


if __name__ == '__main__':
   banco = SistemaBancario()
   banco.menu()