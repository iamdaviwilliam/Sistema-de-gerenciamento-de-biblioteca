import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import uuid

# Função para inicializar o estado da sessão
def init_session_state():
    if 'biblioteca' not in st.session_state:
        st.session_state['biblioteca'] = Biblioteca()

# Estrutura para armazenar os livros
class Biblioteca:
    def __init__(self):
        self.livros = []

    def cadastrar_livro(self, titulo, autor, categoria, ano):
        # Gera um ID único para cada livro
        livro = {
            'id': str(uuid.uuid4()),  # Geração do ID único
            'titulo': titulo,
            'autor': autor,
            'categoria': categoria,
            'ano': ano,
            'emprestado': False
        }
        self.livros.append(livro)

    def listar_livros(self):
        return pd.DataFrame(self.livros)

    def emprestar_livro(self, livro_id):
        for livro in self.livros:
            if livro['id'] == livro_id and not livro['emprestado']:
                livro['emprestado'] = True
                return f"Livro '{livro['titulo']}' emprestado com sucesso."
        return "Livro não disponível para empréstimo."

    def devolver_livro(self, livro_id):
        for livro in self.livros:
            if livro['id'] == livro_id and livro['emprestado']:
                livro['emprestado'] = False
                return f"Livro '{livro['titulo']}' devolvido com sucesso."
        return "Livro não encontrado ou não estava emprestado."

# Funções para criar e visualizar o grafo
def criar_grafo(livros):
    G = nx.Graph()
    categorias = list(set([livro['categoria'] for livro in livros]))
    
    for i, categoria1 in enumerate(categorias):
        for j, categoria2 in enumerate(categorias):
            if i < j:
                distancia = abs(i - j) + 1  # Exemplo de distância simples
                G.add_edge(categoria1, categoria2, weight=distancia)
    
    return G

def plotar_grafo(G):
    fig, ax = plt.subplots()  # Cria a figura e os eixos
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
    return fig

def calcular_menor_caminho(G, origem, destino):
    try:
        caminho = nx.dijkstra_path(G, origem, destino)
        distancia_total = nx.dijkstra_path_length(G, origem, destino)
        return caminho, distancia_total
    except nx.NetworkXNoPath:
        return "Caminho não encontrado.", None

# Inicializando o estado da sessão
init_session_state()

# Interface com Streamlit
st.title("Sistema de Gerenciamento de Biblioteca")

# Usando a sessão cacheada
biblioteca = st.session_state['biblioteca']

# Implementação do menu
menu = st.sidebar.selectbox("Menu", ["Cadastrar Livro", "Listar Livros", "Empréstimo/Devolução", "Gerar Grafo", "Calcular Menor Caminho"])

# Função para cada menu
if menu == "Cadastrar Livro":
    st.header("Cadastro de Livro")
    titulo = st.text_input("Título")
    autor = st.text_input("Autor")
    categoria = st.text_input("Categoria")
    ano = st.text_input("Ano de Lançamento")

    if st.button("Cadastrar Livro"):
        biblioteca.cadastrar_livro(titulo, autor, categoria, ano)
        st.success("Livro cadastrado com sucesso!")
        # Atualizando o estado da sessão
        st.session_state['biblioteca'] = biblioteca

elif menu == "Listar Livros":
    st.header("Livros Cadastrados")
    livros_df = biblioteca.listar_livros()
    st.dataframe(livros_df)

elif menu == "Empréstimo/Devolução":
    st.header("Empréstimo e Devolução")
    livro_id = st.text_input("ID do Livro")
    acao = st.selectbox("Ação", ["Empréstimo", "Devolução"])

    if st.button("Executar"):
        if acao == "Empréstimo":
            resultado = biblioteca.emprestar_livro(livro_id)
        else:
            resultado = biblioteca.devolver_livro(livro_id)
        st.write(resultado)
        # Atualizando o estado da sessão
        st.session_state['biblioteca'] = biblioteca

elif menu == "Gerar Grafo":
    st.header("Grafo de Categorias")
    if st.button("Gerar Grafo"):
        G = criar_grafo(biblioteca.livros)
        fig = plotar_grafo(G)  # Chama a função que retorna a figura
        st.pyplot(fig)  # Passa a figura explicitamente

elif menu == "Calcular Menor Caminho":
    st.header("Calcular Menor Caminho Entre Categorias")
    categoria_origem = st.text_input("Categoria de Origem")
    categoria_destino = st.text_input("Categoria de Destino")

    if st.button("Calcular Menor Caminho"):
        G = criar_grafo(biblioteca.livros)
        caminho, distancia_total = calcular_menor_caminho(G, categoria_origem, categoria_destino)
        
        if distancia_total is not None:
            st.write(f"Menor caminho: {' -> '.join(caminho)}")
            st.write(f"Distância total: {distancia_total}")
        else:
            st.write(caminho)
