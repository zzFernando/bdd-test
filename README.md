# BDD Test

Este repositório contém testes de comportamento (Behavior Driven Development - BDD) utilizando a biblioteca **Behave** para validar interações com a API **Leaf**.

## Visão Geral

O projeto foi desenvolvido para realizar testes automatizados em APIs utilizando o framework **Behave**. Ele cobre cenários como a autenticação de um usuário e a solicitação de campos via chamadas HTTP.

### Cenários de Teste

1. **Solicitação de Token**
   - Autentica um usuário com credenciais válidas.
   - Faz uma chamada HTTP `POST` para obter um token de autenticação.
   - Verifica se o status code da resposta é 200 e se o token está presente.

2. **Solicitação de Todos os Campos**
   - Usa um token válido para fazer uma chamada HTTP `GET` para a API de campos.
   - Verifica se a resposta contém um código de status 200 e os dados dos campos solicitados.

## Estrutura do Projeto

```
|-- features/
|   |-- request_all_fields.feature  # Arquivo de feature para solicitar todos os campos.
|   |-- request_token.feature       # Arquivo de feature para solicitar o token de autenticação.
|   |-- steps/
|       |-- request_all_fields.py   # Implementação dos passos para solicitar campos.
|       |-- request_token.py        # Implementação dos passos para solicitar o token.
|-- pytest_tests.py                 # Testes simples usando pytest.
```

## Requisitos

- **Python 3.12+**
- **Behave**
- **Requests**

### Instalando as Dependências

Use o seguinte comando para instalar as dependências necessárias:

```bash
pip install -r requirements.txt
```

### Executando os Testes

Para rodar os testes BDD, execute:

```bash
behave
```

### Testes Unitários

Você também pode rodar os testes unitários com o Pytest:

```bash
pytest pytest_tests.py
```

## API Utilizada

- **Autenticação**: `https://api.withleaf.io/api/authenticate`
- **Campos**: `https://api.withleaf.io/services/fields/api/fields`

## Licença

Este projeto está licenciado sob a **MIT License** - consulte o arquivo [LICENSE](./LICENSE) para mais detalhes.
