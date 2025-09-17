# `auth`

O pacote `auth` é responsável pelo **Controle de Acesso e Autorização** dentro do banco de dados. Ele gerencia usuários, papéis (roles) e permissões para garantir que apenas entidades autorizadas possam executar ações em recursos específicos.

Esta camada responde a perguntas como:

- > O usuário `Alice` pode ler a tabela `salarios`?
- > Quem pode criar novas tabelas?
- > O usuário `Bob` pode deletar o banco de dados?
