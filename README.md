# Sistema de Gerenciamento de Biblioteca

## Descrição

Este projeto é um sistema de gerenciamento de biblioteca que permite o cadastro, consulta, empréstimo e devolução de livros. Além disso, utiliza o algoritmo de Dijkstra para calcular o menor caminho entre categorias de livros, representadas como um grafo. A interface é construída com Streamlit, proporcionando uma experiência interativa para o usuário.

## Funcionalidades

- **Cadastro de Livros**:  
  Permite registrar livros com título, autor, categoria, ano de lançamento e um ID único.

- **Listagem de Livros**:  
  Exibe todos os livros cadastrados em uma tabela interativa.

- **Empréstimo e Devolução**:  
  Controle de status de empréstimos e devoluções dos livros.

- **Visualização de Grafo**:  
  Representa categorias de livros como nós de um grafo, com as distâncias entre elas.

- **Cálculo de Menor Caminho**:  
  Utiliza o algoritmo de Dijkstra para encontrar o menor caminho entre categorias.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do sistema.
- **Streamlit**: Framework para criação de interfaces web interativas.
- **NetworkX**: Biblioteca para criação e manipulação de grafos.
- **Matplotlib**: Usada para plotagem do grafo gerado.
- **Pandas**: Para manipulação de dados dos livros em formato tabular.

## Instalação

Para executar o projeto, siga os passos abaixo:

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/iamdaviwilliam/Sistema-de-gerenciamento-de-biblioteca
   cd Sistema-de-gerenciamento-de-biblioteca

2. **Instale as dependências**

    pip install -r requirements.txt

## Como executar

Para iniciar a aplicação, execute o seguinte comando no terminal:
    streamlit run app.py
A aplicação será aberta em seu navegador padrão.

# Uso

1. **Cadastrar Livro:**
Preencha os campos de título, autor, categoria e ano de lançamento para adicionar um novo livro ao sistema.

2. **Listar Livros:**
Visualize todos os livros cadastrados em uma tabela.

3. **Empréstimo e Devolução:**
Insira o ID do livro para realizar um empréstimo ou devolução.

4. **Gerar Grafo:**
Clique para gerar e visualizar o grafo das categorias.

5. **Calcular Menor Caminho:**
Insira as categorias de origem e destino para calcular e exibir o menor caminho.

6. **Estrutura do Código**
Classe Biblioteca:
Gerencia o cadastro e controle de livros. Métodos para cadastrar, listar, emprestar e devolver livros.

7. **Funções de Grafo:**
criar_grafo, plotar_grafo e calcular_menor_caminho para manipulação e visualização das categorias.

**Contribuição**
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou pull request.
