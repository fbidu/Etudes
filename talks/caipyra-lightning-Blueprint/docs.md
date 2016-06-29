FORMAT: 1A
HOST: http://caipyra.felipevr.com/

# Caipyra

API bem da hora pro Lightning Talk do Caipyra \o/ 

## User Collection [/users]

Essa coleção de endpoints cuida das operações relacionadas com usuários cadastrados

### Listar Todos os Usuários [GET]

+ Response 200 (application/json)

        [
            {
                "id": "1",
                "name": "Fernando Masanori",
                "twitter": "@fmasanori",
                "github": "fmasanori"
            },
            {
                "id": "2",
                "name": "Felipe Rodrigues",
                "twitter": "@fevir0",
                "github": "fbidu"
            },
            {
                "id": "3",
                "name": "Barbara Moraes",
                "twitter": "@barbararocham",
                "github": "barmvicente"
            }
        ]

### Criar um novo usuário [POST]

Você pode criar um novo usuário fazendo uma chamada do tipo POST
neste endpoint. Os seguintes parâmetros são utilizados:

+ name (string) - O nome completo do participante
+ twitter (string) - O nome de usuário do participante no Twitter, precedido por @
+ github (string) - O nome de usuário do participante no GitHub


+ Request (application/json)

        {
            "name": "Guido van Rossum,
            "twitter": "gvanrossum",
            "github": "gvanrossum"
        }

+ Response 201 (application/json)

    + Headers

            Location: /users/4

    + Body

            {
                "id": 4,
                "name": "Guido van Rossum,
                "twitter": "gvanrossum",
                "github": "gvanrossum"
            }


