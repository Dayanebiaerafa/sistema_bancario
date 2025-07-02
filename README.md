# 🏦 Sistema Bancário em Python

Este é um projeto desenvolvido em Python com o objetivo de simular um sistema bancário básico, operando diretamente pelo terminal. Ele foi criado com fins didáticos e pode ser usado como base para quem está iniciando no mundo da programação e deseja entender conceitos como estruturas condicionais, laços, funções, tratamento de erros e manipulação de datas.

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
- ❌ **Encerrar o programa com segurança**

---

## 🧠 Lógica por trás do código

O programa utiliza um **laço de repetição `while True`** para manter o menu sempre disponível até que o usuário deseje sair (`opção q`).  
Cada operação é selecionada com uma letra específica e processada com estrutura `if/elif/else`.

### 🔷 1. Menu Principal
Exibe as opções disponíveis ao usuário:
```python
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[r] Redefinir Saques Diários
[a] Alterar Limite de Saque
[q] Sair
"""
```

---

### 🔷 2. Depósito
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

### 🔷 3. Saque
Validações importantes:
- Saldo suficiente?
- Valor dentro do limite de saque?
- Número de saques diários não ultrapassado?
- Se aprovado:
- Subtrai do saldo
- Registra a data e hora
- Atualiza o extrato

---

### 🔷 4. Extrato
Exibe todas as transações do dia, com timestamp e descrição.
Caso não haja movimentações, mostra uma mensagem informativa.

---

### 🔷 5. Redefinir Saques
Restaura o contador de saques diários para zero.
Ideal para simular um novo dia de uso.

---

### 🔷 6. Alterar Limite de Saque
Permite ao usuário definir um novo valor máximo para os saques.
Valida se o novo valor é positivo antes de aplicar a mudança.

---

### 🛠️ Tecnologias e Bibliotecas
- Python 3.11+
- ```datetime ```→ Usada para registrar a hora exata de cada transação.

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

### 💡 Possíveis Melhorias Futuras
- Armazenar dados em arquivos .csv ou .json
- Implementar login por CPF/senha
- Criar uma interface gráfica (Tkinter ou Web)
- Criar uma API simulando um serviço bancário

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


