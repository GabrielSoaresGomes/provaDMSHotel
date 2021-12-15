# Prova de Reserva de Hospedagens
 Processo Seletivo DMS - Gabriel Soares Gomes - 202110116
 
## Requisitos Implementados:
● O sistema deve possibilitar ao visitante se autenticar no sistema através de seu email e
senha.

● O sistema deve possibilitar ao visitante buscar por hotéis, pousadas e casas de temporada,
filtrando por cidade, parte do nome do local, preço, nota de avaliação, qualidade do Wi-Fi e
se há TV a cabo.

● O sistema deve possibilitar ao usuário agendar um local informando a data de entrada e de
saída do local e a quantidade de pessoas.

● Caso a quantidade de pessoas informada no momento do agendamento de uma
hospedagem extrapole o limite definido, o sistema deve informar ao usuário que a
quantidade de pessoas informada não é aceita pela hospedagem, deixando claro qual o
limite máximo de pessoas que é aceito.

● O sistema deve possibilitar ao usuário visualizar os seus agendamentos realizados.

## Informações Úteis: 
### Login:
usuário: selecaoengsoftware@universidadedevassouras.edu.br

senha: default123

### Gerar o banco de daods:

Para poder gerar o banco de dados, é só rodar o seguinte comando no terminal: <code>python3 manage.py loaddata banco.json</code>

Ele irá rodar o arquivo json que contêm o comando sql que irá gerar a table.

### Observações:

Não consegui utilizar ddl para gerar o banco, e por isso usei esse arquivo json, mas deve ter o postgres configurado em sua máquina.

Esse comando do json cria a table, porém deve ter uma conexão com o postgres.
