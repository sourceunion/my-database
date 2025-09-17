# `schema`

O pacote `schema` é responsável por gerenciar a **estrutura e a definição dos dados**, também conhecido como o **catálogo do sistema**. Ele permite aos usuários criar, modificar e consultar os metadados que descrevem as "tabelas" (ou coleções) do banco de dados.

Esta camada responde a perguntas como:

- > Quais campos a tabela `usuários` possui?
- > O campo `idade` é um número inteiro?
- > O campo `email` é obrigatório?

Ele atua como o "arquiteto" do banco de dados, garantindo que os dados inseridos através da camada de armazenamento (`storage`) estejam em conformidade com as regras definidas.
