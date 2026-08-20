[🇧🇷 Português](./README.pt-BR.md) | [🇬🇧 English](./README.md)

<p align="center">
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=49AA26&labelColor=000000">
  <img alt="Python" src="https://img.shields.io/badge/python-3.8%2B-blue.svg?labelColor=000000">
</p>

<p align="center">
  <a href="#-sobre-o-projeto">Sobre o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-funcionalidades">Funcionalidades</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-conceitos-demonstrados">Conceitos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-estrutura-do-projeto">Estrutura</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-tecnologias-utilizadas">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-executar-na-sua-máquina">Como executar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-licença">Licença</a>
</p>

# 🌳 Tree-verse: Lecionador Interativo de Árvores Binárias

## 📖 Sobre o projeto

O **Tree-verse** é uma aplicação educacional desenvolvida em Python para ensinar, de forma interativa e visual, os fundamentos da estrutura de dados **árvore**.

Por meio de lições interativas, animações nó a nó e visualizações dinâmicas no terminal, o projeto busca transformar conceitos teóricos de estruturas de dados em uma experiência prática de aprendizado.

> 🚧 **Projeto em desenvolvimento**
>
> O Tree-verse ainda está em construção. Novas funcionalidades, lições e recursos visuais serão adicionados ao longo do desenvolvimento.

---

## ⚙️ Funcionalidades

- Inserção de elementos em uma Árvore Binária de Busca
- Busca de elementos
- Remoção de nós
- Percursos em pré-ordem, em-ordem e pós-ordem
- Percurso em nível
- Cálculo da altura da árvore
- Contagem de nós e folhas
- Visualização da estrutura da árvore no terminal
- Lições interativas sobre conceitos de árvores

---

## 💡 Conceitos Demonstrados

* **Árvore Binária de Busca (BST):** Uma estrutura de dados hierárquica onde cada nó possui no máximo dois filhos, organizada de forma que os valores à esquerda sejam menores e à direita sejam maiores que o nó pai.
* **Percursos em Árvores:** Animações e visualizações demonstrando as estratégias clássicas de exploração, como pré-ordem, em-ordem, pós-ordem e percurso em nível (largura).
* **Fundamentos Teóricos:** Abordagem dos conceitos fundamentais que estruturam as árvores, tais como:
  * **Nós e folhas**
  * **Florestas e subárvores**
  * **Árvore binária**
  * **Altura mínima e máxima**
  * **Comprimento e profundidade**
  * **Árvore Binária de Busca (BST)**

---

## 🏗️ Estrutura do projeto

Para manter a separação de responsabilidades, a aplicação foi organizada em diferentes módulos:

* **`main.py`**: Ponto de entrada da aplicação, responsável por iniciar o programa.
* **`app.py`**: Orquestrador central responsável por gerenciar o fluxo de execução das funcionalidades do sistema.
* **`src/classes.py`**: Contém a classe responsável pela criação dos nós e a estrutura base da árvore binária, juntamente com seus métodos de percurso.
* **`src/tree.py`**: Classe dedicada às árvores de busca do sistema, atualmente contendo a implementação da **Binary Search Tree (BST)**.
* **`src/visualizer.py`**: Responsável pela renderização das árvores e dos percursos no terminal, incluindo suas animações.
* **`src/lessons.py`**: Central de aprendizado responsável pelas lições e explicações dos conceitos relacionados às árvores.
* **`src/menu.py`**: Responsável pela exibição dos menus e pelo direcionamento das opções escolhidas pelo usuário.
* **`src/queue.py`**: Implementação personalizada da estrutura de dados **fila**, utilizada como suporte para o percurso em nível.
* **`src/utils.py`**: Reúne funções utilitárias, como leitura e validação de opções numéricas e limpeza do terminal.
* **`requirements.txt`**: Gerencia as dependências externas utilizadas pelo projeto, como `rich` e `pytest`.
* **`tests/*`**: Diretório destinado aos testes das funcionalidades do projeto.

---

## 🛠️ Tecnologias utilizadas

- **Python 3.8+**
- **Rich** — renderização e estilização do conteúdo no terminal
- **Pytest** — testes automatizados
- **Git** — controle de versão

---

## 🚧 Desenvolvimento

O projeto encontra-se em desenvolvimento e novas funcionalidades serão adicionadas conforme o avanço dos estudos e da implementação.

### Implementado

- [x] Estrutura de árvore binária
- [x] Árvore Binária de Busca (BST)
- [x] Inserção de elementos
- [x] Busca de elementos
- [x] Remoção de nós
- [x] Percursos em pré-ordem, em-ordem e pós-ordem
- [x] Percurso em nível
- [x] Cálculo da altura
- [x] Contagem de nós
- [x] Contagem de folhas
- [x] Estrutura de fila para suporte ao percurso em nível
- [x] Sistema inicial de menus
- [x] Estrutura inicial das lições

### Próximos passos

- [ ] Finalizar as lições interativas
- [ ] Finalizar e aprimorar as visualizações animadas
- [ ] Expandir a cobertura de testes
- [ ] Melhorar a experiência de interação no terminal
- [ ] Estudar e avaliar uma futura implementação de **Árvore AVL**

> A implementação de uma **Árvore AVL** não faz parte do escopo atual. Ela será estudada posteriormente antes de qualquer decisão sobre sua implementação no projeto.

---

## 🚀 Como executar na sua máquina

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/tree-verse.git
cd tree-verse