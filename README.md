# Trabalho-Final-de-POO
# 🌿 Sistema de Classificação de Plantas do Ceará

Sistema interativo para identificação e classificação de plantas representativas da região do Ceará, desenvolvido com Programação Orientada a Objetos (POO) seguindo padrões científicos da taxonomia de Lineu.

---

## 🎯 Sobre o Projeto

Este sistema foi desenvolvido para uma ONG com o objetivo de facilitar a identificação e catalogação de plantas da **Caatinga**, bioma exclusivamente brasileiro presente no Ceará. 

O projeto utiliza **Programação Orientada a Objetos (POO)** para modelar a classificação taxonômica científica, permitindo:

- Cadastro detalhado de plantas com classificação científica completa
- Busca e identificação por múltiplos critérios
- Geração de relatórios e estatísticas
- Interface interativa e amigável via terminal

### 🎓 Contexto Educacional

O sistema segue a **taxonomia de Lineu**, padrão internacional para classificação biológica:

```
Reino → Divisão → Classe → Ordem → Família → Gênero → Espécie
```

---

## ✨ Funcionalidades

### Menu Interativo

O sistema oferece um menu completo com as seguintes opções:

| Opção | Funcionalidade | Descrição |
|-------|---------------|-----------|
| 1 | ➕ Cadastrar nova planta | Adiciona uma planta com classificação completa |
| 2 | 📖 Listar todas as plantas | Exibe lista de todas as plantas cadastradas |
| 3 | 🔍 Buscar por nome | Busca planta pelo nome popular |
| 4 | 🏷️ Buscar por família | Lista plantas de uma família taxonômica |
| 5 | 🔎 Identificar por características | Encontra plantas baseado em características |
| 6 | 📊 Ver estatísticas | Mostra estatísticas do sistema |
| 7 | 📄 Gerar relatório | Cria relatório completo do bioma |
| 8 | 💾 Carregar exemplos | Carrega 3 plantas de exemplo |
| 0 | 🚪 Sair | Encerra o sistema |

### Recursos Principais

- ✅ **Classificação Taxonômica Completa**: Reino, Divisão, Classe, Ordem, Família, Gênero, Espécie
- ✅ **Busca Inteligente**: Por nome, família ou características
- ✅ **Identificação por Características**: Sistema de matching baseado em atributos
- ✅ **Estatísticas**: Análise de distribuição por família
- ✅ **Status de Conservação**: Acompanhamento do risco de extinção
- ✅ **Interface Intuitiva**: Menu interativo e limpo

---

## 🛠 Tecnologias Utilizadas

- **Python 3.7+**: Linguagem de programação
- **POO (Programação Orientada a Objetos)**: Paradigma de desenvolvimento
- **Typing**: Anotações de tipo para melhor legibilidade
- **OS**: Manipulação do sistema (limpeza de tela)

### Bibliotecas Padrão Utilizadas

```python
from typing import List, Dict, Set, Optional
from datetime import datetime
import os
```

**Não há dependências externas!** O sistema roda apenas com Python instalado.

---

## 🚀 Como Usar

### Início Rápido

1. Execute o programa
2. Escolha a opção **8** para carregar plantas de exemplo
3. Explore as outras funcionalidades do menu

### Cadastrando uma Nova Planta

1. Escolha a opção **1** no menu
2. Preencha as informações solicitadas:
   - Nome popular (ex: "Mandacaru")
   - Descrição
   - Habitat
   - Status de conservação
   - Características (uma por vez)
   - Classificação taxonômica completa

### Buscando Plantas

**Por Nome:**
- Opção **3** → Digite o nome popular

**Por Família:**
- Opção **4** → Digite o nome da família (ex: "Cactaceae")

**Por Características:**
- Opção **5** → Digite características como "espinhos", "flores brancas"

---

## 📁 Estrutura do Projeto

```
plantas-ceara/
│
├── sistema_plantas.py          # Código principal
├── README.md                   # Este arquivo
├── diagrama_uml.png           # Diagrama UML das classes
```

### Estrutura de Classes

O sistema é composto por 4 classes principais:

```
ClassificacaoTaxonomica
    ├── Armazena hierarquia taxonômica
    └── Gera nome científico

Planta
    ├── Contém ClassificacaoTaxonomica
    ├── Armazena características
    └── Gerencia informações da planta

BiomaCaatinga
    ├── Contém lista de Plantas
    ├── Gerencia busca e listagem
    └── Gera relatórios

SistemaIdentificacao
    ├── Gerencia BiomaCaatinga
    ├── Cadastra e identifica plantas
    └── Gera estatísticas
```

---

## 📊 Diagrama UML

O sistema segue o seguinte diagrama de classes:

```

┌─────────────────────────────────┐
│   ClassificacaoTaxonomica       │
├─────────────────────────────────┤
│ - reino: str                    │
│ - divisao: str                  │
│ - classe: str                   │
│ - ordem: str                    │
│ - familia: str                  │
│ - genero: str                   │
│ - especie: str                  │
├─────────────────────────────────┤
│ + obter_nome_cientifico()       │
│ + obter_classificacao_completa()│
└─────────────────────────────────┘
           ▲
           │ possui
           │
┌─────────────────────────────────┐
│         Planta                  │
├─────────────────────────────────┤
│ - nome_popular: str             │
│ - classificacao: Classificacao  │
│ - descricao: str                │
│ - caracteristicas: List[str]    │
│ - habitat: str                  │
│ - status_conservacao: str       │
├─────────────────────────────────┤
│ + exibir_informacoes()          │
│ + adicionar_caracteristica()    │
│ + verificar_familia()           │
└─────────────────────────────────┘
           ▲
           │ contém
           │
┌─────────────────────────────────┐
│      BiomaCaatinga              │
├─────────────────────────────────┤
│ - nome: str                     │
│ - plantas: List[Planta]         │
│ - descricao: str                │
├─────────────────────────────────┤
│ + adicionar_planta()            │
│ + listar_plantas()              │
│ + buscar_por_nome_popular()     │
│ + buscar_por_familia()          │
│ + gerar_relatorio()             │
└─────────────────────────────────┘
           ▲
           │ gerencia
           │
┌─────────────────────────────────┐
│   SistemaIdentificacao          │
├─────────────────────────────────┤
│ - bioma: BiomaCaatinga          │
│ - catalogo: Dict[str, Planta]   │
├─────────────────────────────────┤
│ + cadastrar_planta()            │
│ + identificar_por_carac()       │
│ + listar_familias()             │
│ + obter_estatisticas()          │
└─────────────────────────────────┘
```

---

## 💡 Exemplos de Uso

### Exemplo 1: Cadastrando uma Planta

```python
# Criar classificação
classificacao = ClassificacaoTaxonomica(
    reino="Plantae",
    divisao="Magnoliophyta",
    classe="Magnoliopsida",
    ordem="Caryophyllales",
    familia="Cactaceae",
    genero="Cereus",
    especie="jamacaru"
)

# Criar planta
mandacaru = Planta(
    nome_popular="Mandacaru",
    classificacao=classificacao,
    descricao="Cacto icônico da Caatinga",
    caracteristicas=["Espinhos longos", "Flores brancas"],
    habitat="Caatinga",
    status_conservacao="Pouco preocupante"
)

# Cadastrar no sistema
sistema.cadastrar_planta(mandacaru)
```

### Exemplo 2: Buscando Plantas

```python
# Buscar por nome
planta = sistema.bioma.buscar_por_nome_popular("Mandacaru")

# Buscar por família
cactos = sistema.bioma.buscar_por_familia("Cactaceae")

# Identificar por características
plantas = sistema.identificar_por_caracteristicas(["espinhos", "verde"])
```

### Exemplo 3: Gerando Estatísticas

```python
stats = sistema.obter_estatisticas()
print(f"Total de plantas: {stats['total_plantas']}")
print(f"Famílias: {stats['familias']}")
```

---

## 🌱 Plantas Incluídas

O sistema vem com 3 plantas de exemplo da Caatinga:

### 1. Juazeiro (*Ziziphus joazeiro*)
- **Família**: Rhamnaceae
- **Características**: Resistente à seca, espinhos, frutos amarelos
- **Status**: Pouco preocupante

### 2. Mandacaru (*Cereus jamacaru*)
- **Família**: Cactaceae
- **Características**: Cacto colunar, espinhos longos, flores brancas
- **Status**: Pouco preocupante

### 3. Umbuzeiro (*Spondias tuberosa*)
- **Família**: Anacardiaceae
- **Características**: Raízes tuberosas, armazena água, frutos ácidos
- **Status**: Vulnerável

---

### Ideias para Contribuição

- 🌿 Adicionar mais plantas da Caatinga
- 📸 Incluir fotos das plantas
- 🗺️ Adicionar mapas de distribuição
- 💾 Implementar salvamento em arquivo/banco de dados
- 🌐 Criar interface web
- 📱 Desenvolver app mobile

---

## 📚 Referências

- [Taxonomia de Lineu](https://pt.wikipedia.org/wiki/Taxonomia_de_Lineu)
- [Bioma Caatinga](https://www.mma.gov.br/biomas/caatinga)
- [Flora do Brasil](http://floradobrasil.jbrj.gov.br/)

---
