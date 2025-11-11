# Chat Eco-nomico
A revolução que os Grandes Modelos de Linguagem (LLM), estão produzindo, em muito se dá pela capacidade deles "lembrarem" o contexto do que estão falando (i.e., a instrução do usuário e o texto que ela já produziu). Isso acontece, pois as redes neurais que produzem os textos, funcionam recebendo um input e respondendo com o próximo token (cada token pode ser uma palavra ou uma parte de uma palavra) mais provável. Ele consegue "lembrar" o que ja foi dito e manter uma produção de texto coerente, graças à técnica de kv-caching, que retroalimenta a LLM após cada token ser gerado, com o input original e os tokens que já foram gerados.

Está é uma técnica poderosa para produzir textos com alto nível de coerência, mas é pouco eficiente, com uma eficiencia de O(n(n+m), onde n é a resposta da LLM e m é o input do usuário.

Visando reduzir o consumo elétrico e de água dos grandes datacenters que processam os inputs de inteligências Artificiais, este projeto tem como objetivo desenvolver um software para reduzir o total de tokens processados pelas LLMs e consequentemente reduzir o consumo elétrico e de água. O software utiliza um LLM menor e local, para recriar o input, reduzindo o total de tokens de entrada. Após isso, ambos os inputs são submetidos para uma LLM disponível em grandes datacentes, para que o usuário possa comparar as respostas produzidas e é realizado o cálculo de tokens submetidos e recebidos, bem como o provável consumo gerado pelos servidores, através de dados médios.

O projeto utiliza o tkinter para construir uma interface de usuário que irá receber um input de texto, processar esse input com uma IA local e enviar esse input para a API do Google GEMINI. Após receber a resposta, a interface gráfica será atualizada com o input processado e a resposta do GEMINI para que o usuário possa ver o resultado. Junto da resposta, será feito o cálculo de total de tokens do input do usuário, do input gerado pela IA local e da resposta do GEMINI e a partir disso gerar um gráfico exibindo a diferença de consumo devido à mudança de input, utilizando o matplotlib.


## Planejamento do trabalho

- Construir interface Gráfica:
    **Danielle**
- Construir modelo de IA menor e local:
    **Fábio**
- Construir prompts para redução de tokens:
    **Matheus**
- Construir cálculos de consumo:
    **Ingrid**

## Instruções para inicializar o projeto

1. Instalação e configuração do git

    1. Baixe e instale o git através do link: https://git-scm.com/downloads
    2. Configuração do git:
        ```bash
        git config user.name "Seu Nome"
        git config user.email "seu_email@email.com"
        ```
    3. Clone o projeto para o seu computador
        1. abra o terminal
        2. abra a pasta onde o projeto ficará
        ```bash
        cd caminho/para/pasta
        ```
        3. faça o clone do projeto
        ```bash
        git clone https://github.com/psifabiohenrique/eco_nomia.git
        ```
    4. Escolha a ramificação que irá trabalhar
        + master:
            A versão mais estável do projeto, versão que será a final
            ```bash
            git checkout master
            ```
        + develop:
            A versão de desenvolvimento, ela irá agrupar todas as atualizações, até que possam ser enviadas para a versão master
            ```bash
            git checkout develop
            ```
        + feat/meu_recurso
            A versão com o novo recurso que você está trabalhando, você deverá criar esse ramo para contribuir com o projeto.
            ```bash
            git checkout feat/meu_recurso
            ```
            ou
            ```bash
            git checkout -b feat/meu_recurso
            ```

2. Configurando o projeto

    1. Crie um ambiente virtual
    ```bash
    python -m venv .venv
    ```
    2. Entre no ambiente virtual
    ``` bash
    .venv/scripts/activate # no windows
    source .venv/bin/activate # no linux/mac
    ```
    3. Instale as dependências do projeto
    ``` bash
    pip install -r requirements.txt
    ```

3. Instalando e iniciando o Ollama
    1. Baixe e instale o [Ollama](https://ollama.com/download)
    2. Baixe um modelo de IA pequeno (entre 1 e 8 bilhões de parâmetros)
        *Pesquise por modelos em: [https://ollama.com/search](https://ollama.com/search)*
        No terminal:
        ```bash
        ollama pull nome_do_modelo
        ```
        Inicialize o processo do ollama (caso não esteja inicializado)

        ```bash
        ollama serve
        ```

4. Executando o projeto
    ```bash
    python main.py
    ```
