# 🏦 Sistema Bancário em Python

Este é um projeto desenvolvido em Python com o objetivo de simular um sistema bancário básico, operando diretamente pelo terminal.

Criado com fins didáticos, este sistema é ideal para quem está iniciando no mundo da programação e deseja colocar em prática diversos conceitos importantes, como:

- Estruturas condicionais (`if`, `elif`, `else`)
- Laços de repetição (`while True`)
- Declaração e organização de funções
- Manipulação de datas com `datetime`
- Tratamento de erros com `try/except`
- Uso de listas e dicionários para representar dados de clientes e contas
- Argumentos posicionais (`/`) e nomeados (`*`) para tornar as funções mais seguras e legíveis
- Formatação visual no terminal com tabulação (`\t`)
- Aplicação da biblioteca `textwrap` para exibir menus alinhados de forma limpa

Este projeto também representa boas práticas de organização e modularização de código, incentivando o uso de funções bem definidas e separação clara de responsabilidades.

---

## 📌 Funcionalidades Implementadas

- 💰 **Depósito** com verificação de valores positivos e registro de data/hora.
- 🏧 **Saque** com controle de:
  - Valor limite por saque
  - Número máximo de saques diários
  - Verificação de saldo disponível
- 📄 **Extrato** de todas as operações com data e hora.
- 🔁 **Redefinir contador de saques diários**
- ⚙️ **Alterar limite de valor de saque**
- 🧾 **Cadastro de Cliente (Usuário)** com CPF, nome, data de nascimento e endereço.
- 🧾 **Criação de Conta Corrente** associada a um cliente existente.
- 👥 **Listagem de Clientes**
- 💳 **Listagem de Contas Bancárias**
- ❌ **Encerrar o programa com segurança**

---

## 🧠 Lógica por trás do código

O programa utiliza um **laço de repetição `while True`** para manter o menu sempre disponível até que o usuário deseje sair (`opção q`).  
Cada operação é processada com estrutura `if/elif/else`.

O sistema foi **organizado em funções** específicas para cada operação, melhorando a legibilidade e manutenção do código.

Além disso, o projeto faz uso de:

- `argumento por posição` (`/`) → para garantir que certos parâmetros sejam passados apenas por ordem.
- `argumento nomeado` (`*`) → para forçar que certos parâmetros sejam passados explicitamente pelo nome, aumentando a clareza.

### 1. Exemplo do Menu Principal com `textwrap`

O menu é apresentado de forma organizada, com uso de tabulação (`\t`) para alinhamento e clareza, e utiliza a biblioteca `textwrap` para remover indentação indesejada do menu multi-linha.

```python
import textwrap

def exibir_menu():
    menu_opcoes = """
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [r]\t Redefinir Saques do Dia
    [a]\t Alterar Limite de Saque
    [nu]\t Novo Cliente
    [nc]\t Nova Conta
    [lu]\t Ver Clientes
    [lc]\t Ver Contas
    [q]\t Sair do Banco
    """
    print(textwrap.dedent(menu_opcoes).strip())
```

---

### 2. Depósito
- O valor digitado deve ser positivo.
- A data e hora do depósito são registradas com `datetime.now()`.
- O valor é adicionado ao saldo e registrado no extrato.
```python
depósito = """
saldo += valor
data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
extrato += f"{data_hora} - Depósito: R$ {valor:.2f}\n"
"""
```

---

### 3. Saque
Validações importantes:
- Saldo suficiente?
- Valor dentro do limite de saque?
- Número de saques diários não ultrapassado?
- Se aprovado:
- Subtrai do saldo
- Registra a data e hora
- Atualiza o extrato

---

### 4. Extrato
Exibe todas as transações do dia, com timestamp e descrição.
Caso não haja movimentações, mostra uma mensagem informativa.

---

### 5. Redefinir Saques
Restaura o contador de saques diários para zero.
Ideal para simular um novo dia de uso.

---

### 6. Alterar Limite de Saque
Permite ao usuário definir um novo valor máximo para os saques.
Valida se o novo valor é positivo antes de aplicar a mudança.

---

### 7. Cadastro de Cliente
Permite criar usuários com nome, CPF, data de nascimento e endereço. Evita CPFs duplicados.

---

### 8. Criação de Conta Corrente
Cria uma conta para um cliente já cadastrado, associando agência, número da conta e dados do titular.

---

### 9. Listar Clientes e Contas
- Mostra a lista de todos os clientes cadastrados com seus dados.

- Lista todas as contas bancárias com agência, número, titular e saldo.

---

### 🛠️ Tecnologias e Bibliotecas
- Python 3.11+
- ```datetime ```→ Usada para registrar a hora exata de cada transação.
- ```textwrap```→ Usada para organizar visualmente o menu no terminal com indentação adequada. 

---

### ℹ️ O que é ```textwrap.dedent()```?
A função ```dedent() ```da biblioteca ```textwrap``` remove espaços em branco à esquerda de blocos de texto multilinha. Isso permite que o texto fique bonito e alinhado na tela, mesmo que o código esteja indentado corretamente no Python.

---

### ▶️ Como Executar
1. Clone o repositório:
```
git clone https://github.com/Dayanebiaerafa/sistema_bancario.git
```
2. Acesse a pasta:
```
cd sistema_bancario
```
3. Execute o arquivo:
```
python sistema_bancario.py
```

---

### 🤝 Contribuições
Contribuições são bem-vindas!
1. Faça um fork
2. Crie sua branch: ```git checkout -b minha-feature```
3. Commit suas alterações: ```git commit -m 'Adiciona nova feature'```
4. Push: ```git push origin minha-feature```
5. Crie um Pull Request

---

### 👩‍💻 Desenvolvido por

**Dayane Regina Teodoro Busto**  
📫 [LinkedIn](https://www.linkedin.com/in/dayaneteodoro)  
💻 [GitHub](https://github.com/Dayanebiaerafa)


