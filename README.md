# Projeto Restaurant Orders

[MEUS COMMITS](https://github.com/HugoRamosC/restaurant-orders-python/commits)

## O que foi desenvolvido?

Foi finalizada uma ferramenta de construção de cardápios de restaurante desenvolvida em Python com leitura de arquivo csv. A ferramenta gera cardápios considerando possíveis restrições alimentares e também a disponibilidade dos ingredientes em estoque.

O projeto iniciou já com uma estrutura inicial eu fui responsável por construir testes para classes já implementadas, implementar uma nova classe para mapear os pratos e suas respectivas receitas (ingredientes e quantidades), também implementar uma classe que gera os cardápios que devem ser mostrados para as pessoas que frequentam o estabelecimento e outra que faz a gestão de estoque dos ingredientes.

### Tecnologias utilizadas:

- Python
- Hashmaps através das estruturas de dados Dict e Set
- Testes de software
- Programação orientada a objetos


### Requisitos obrigatórios do Projeto

- [x] 1 - Escreva os testes para a classe Ingredient no arquivo tests/ingredient/test_ingredient.py. Seus testes devem garantir que:
      
        - a classe pode ser instanciada corretamente de acordo com a assinatura esperada;
        - o atributo conjunto restrictions é populado como esperado;
        - o método mágico __repr__ funcione como esperado;
        - o método mágico __eq__ funcione como esperado;
        - o método mágico __hash__ funcione como esperado.
- [x] 2 - Escreva os testes para a classe Dish no arquivo tests/dish/test_dish.py. Seus testes devem garantir que:
      
        - a classe pode ser instanciada corretamente de acordo com a assinatura esperada;
        - os métodos da classe, inclusive os métodos mágicos, funcionem como esperado;
        - o dicionário de receita do prato devolve a quantidade correta de um ingrediente;
        - são levantados erros ao criar pratos inválidos;
- [x] 3 - Implemente a classe MenuData no arquivo src/services/menu_data.py. Ao longo da sua implementação você deve garantir que:
      
        - a classe, ao ser instanciada, recebe o caminho para o arquivo csv no parâmetro source_path;
        - a classe fará a leitura do arquivo csv e baseado em seu conteúdo fará as devidas instanciações de pratos e ingredientes;
        - a classe contenha o atributo dishes que deverá ser um set com todos os pratos devidamente instanciados;
        - cada um dos pratos contenha sua respectiva receita, isto é, seus ingredientes e quantidades, bem como seu preço.
- [x] 4 - Você deve implementar o método get_main_menu dentro da classe MenuBuilder que se encontra no arquivo src/services/menu_builder.py. O método tem como parâmetro opcional uma restrição que deve ser levada em conta na hora de gerar o cardápio.<br>
Seguindo a assinatura do método que foi deixada pela equipe anterior, o retorno deste método deve ser do tipo List[Dict]. Assim, é necessário que o método retorne uma lista de dicionários que         contenham as chaves dish_name, ingredients, price e restrictions que se referem, respectivamente, ao nome do prato, ingredientes que o compõem, seu preço no cardápio e restrições daquele mesmo prato.<br>
Ao longo de sua implementação você deve garantir que:

        - a classe possa ser instanciada corretamente;
        - o método get_main_menu retorna uma lista de dicionários com o cardápio completo quando não é passado nenhum parâmetro;
        - o método get_main_menu retorna uma lista de dicionários com o cardápio correto respeitando a restrição alimentar passada como parâmetro;
            
## Requisitos Bônus

- [x] 5 - A classe InventoryMapping se encontra no arquivo src/services/inventory_control.py, nela você deverá implementar os métodos check_recipe_availability e consume_recipe. Ao longo da sua implementação você deve garantir que:
      
        - a classe possa ser devidamente instanciada;
        - o método check_recipe_availability retorna True caso a receita esteja disponível para consumo e False caso contrário;
        - o método consume_recipe subtrai os ingredientes da receita do total disponível em estoque caso a receita esteja disponível para consumo e levanta uma exceção ValueError caso contrário.
- [x] 6 - Você deve complementar a implementação do método get_main_menu, feito no requisito 4. O método agora precisa considerar também a disponibilidade em estoque dos ingredientes dos pratos. Use a classe implementada no requisito anterior, InventoryMapping, para ter acesso a informações do estoque.<br>
Ao longo de sua implementação você deve garantir que:

        - o método get_main_menu retorna uma lista de dicionários com o cardápio completo caso não exista restrição e todos os ingredientes estiverem disponíveis;
        - o método get_main_menu retorna uma lista de dicionários com os cardápios corretos respeitando a restrição alimentar passada como parâmetro e também a disponibilidade de ingredientes no estoque;
