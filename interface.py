from typing import List, Dict, Set, Optional
from datetime import datetime
import os


class ClassificacaoTaxonomica:
    """Representa a classificação taxonômica científica de uma planta"""

    def __init__(self, reino: str, divisao: str, classe: str, ordem: str,
                 familia: str, genero: str, especie: str):
        self.reino = reino
        self.divisao = divisao
        self.classe = classe
        self.ordem = ordem
        self.familia = familia
        self.genero = genero
        self.especie = especie

    def obter_nome_cientifico(self) -> str:
        """Retorna o nome científico (gênero + espécie)"""
        return f"{self.genero} {self.especie}"

    def obter_classificacao_completa(self) -> Dict[str, str]:
        """Retorna dicionário com toda a classificação"""
        return {
            'Reino': self.reino,
            'Divisão': self.divisao,
            'Classe': self.classe,
            'Ordem': self.ordem,
            'Família': self.familia,
            'Gênero': self.genero,
            'Espécie': self.especie,
            'Nome Científico': self.obter_nome_cientifico()
        }

    def __str__(self) -> str:
        return f"{self.obter_nome_cientifico()} (Família: {self.familia})"


class Planta:
    """Representa uma planta com suas características e classificação"""

    def __init__(self, nome_popular: str, classificacao: ClassificacaoTaxonomica,
                 descricao: str, caracteristicas: List[str], habitat: str,
                 status_conservacao: str = "Não avaliado"):
        self.nome_popular = nome_popular
        self.classificacao = classificacao
        self.descricao = descricao
        self.caracteristicas = caracteristicas if caracteristicas else []
        self.habitat = habitat
        self.status_conservacao = status_conservacao

    def exibir_informacoes(self) -> str:
        """Exibe informações completas da planta"""
        info = f"\n{'=' * 60}\n"
        info += f" PLANTA: {self.nome_popular}\n"
        info += f"{'=' * 60}\n"
        info += f"Nome Científico: {self.classificacao.obter_nome_cientifico()}\n"
        info += f"Família: {self.classificacao.familia}\n"
        info += f"Status de Conservação: {self.status_conservacao}\n\n"
        info += f"Descrição:\n{self.descricao}\n\n"
        info += f"Habitat: {self.habitat}\n\n"
        info += f"Características:\n"
        for i, carac in enumerate(self.caracteristicas, 1):
            info += f"  {i}. {carac}\n"
        info += f"{'=' * 60}\n"
        return info

    def adicionar_caracteristica(self, caracteristica: str) -> None:
        """Adiciona uma nova característica à planta"""
        if caracteristica not in self.caracteristicas:
            self.caracteristicas.append(caracteristica)

    def verificar_familia(self, familia: str) -> bool:
        """Verifica se a planta pertence a uma família específica"""
        return self.classificacao.familia.lower() == familia.lower()

    def __str__(self) -> str:
        return f"{self.nome_popular} ({self.classificacao.obter_nome_cientifico()})"


class BiomaCatinga:
    """Representa o bioma Caatinga com suas plantas características"""

    def __init__(self, nome: str = "Caatinga", descricao: str = ""):
        self.nome = nome
        self.descricao = descricao or "Único bioma exclusivamente brasileiro"
        self.plantas: List[Planta] = []

    def adicionar_planta(self, planta: Planta) -> None:
        """Adiciona uma planta ao bioma"""
        self.plantas.append(planta)
        print(f"✓ Planta '{planta.nome_popular}' adicionada ao bioma {self.nome}")

    def listar_plantas(self) -> List[Planta]:
        """Retorna lista de todas as plantas"""
        return self.plantas

    def buscar_por_nome_popular(self, nome: str) -> Optional[Planta]:
        """Busca planta por nome popular"""
        for planta in self.plantas:
            if planta.nome_popular.lower() == nome.lower():
                return planta
        return None

    def buscar_por_familia(self, familia: str) -> List[Planta]:
        """Busca todas as plantas de uma família"""
        return [p for p in self.plantas if p.verificar_familia(familia)]

    def contar_plantas(self) -> int:
        """Retorna o número total de plantas cadastradas"""
        return len(self.plantas)

    def gerar_relatorio(self) -> str:
        """Gera relatório sobre o bioma"""
        relatorio = f"\n{'#' * 60}\n"
        relatorio += f" RELATÓRIO DO BIOMA: {self.nome}\n"
        relatorio += f"{'#' * 60}\n\n"
        relatorio += f"Descrição: {self.descricao}\n"
        relatorio += f"Total de plantas cadastradas: {self.contar_plantas()}\n\n"
        relatorio += f"Lista de Plantas:\n"
        relatorio += f"{'-' * 60}\n"
        for i, planta in enumerate(self.plantas, 1):
            relatorio += f"{i}. {planta}\n"
        relatorio += f"{'#' * 60}\n"
        return relatorio


class SistemaIdentificacao:
    """Sistema principal para identificação e gestão de plantas"""

    def __init__(self, bioma: BiomaCatinga):
        self.bioma = bioma
        self.catalogo: Dict[str, Planta] = {}

    def cadastrar_planta(self, planta: Planta) -> None:
        """Cadastra uma planta no sistema"""
        nome_cientifico = planta.classificacao.obter_nome_cientifico()
        self.catalogo[nome_cientifico] = planta
        self.bioma.adicionar_planta(planta)

    def identificar_por_caracteristicas(self, caracteristicas: List[str]) -> List[Planta]:
        """Identifica plantas com base em características fornecidas"""
        plantas_encontradas = []
        for planta in self.bioma.listar_plantas():
            coincidencias = sum(1 for c in caracteristicas
                                if any(c.lower() in pc.lower()
                                       for pc in planta.caracteristicas))
            if coincidencias > 0:
                plantas_encontradas.append((planta, coincidencias))

        plantas_encontradas.sort(key=lambda x: x[1], reverse=True)
        return [planta for planta, _ in plantas_encontradas]

    def listar_familias(self) -> Set[str]:
        """Lista todas as famílias cadastradas"""
        return {p.classificacao.familia for p in self.bioma.listar_plantas()}

    def obter_estatisticas(self) -> Dict[str, any]:
        """Retorna estatísticas do sistema"""
        plantas = self.bioma.listar_plantas()
        familias = self.listar_familias()

        return {
            'total_plantas': len(plantas),
            'total_familias': len(familias),
            'familias': list(familias),
            'plantas_por_familia': {
                familia: len(self.bioma.buscar_por_familia(familia))
                for familia in familias
            }
        }


# ============================================================
# FUNÇÕES INTERATIVAS DO MENU
# ============================================================

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """Pausa a execução até o usuário pressionar Enter"""
    input("\n||  Pressione ENTER para continuar...")


def exibir_menu_principal():
    """Exibe o menu principal"""
    print("\n" + "=" * 60)
    print("🌿 SISTEMA DE CLASSIFICAÇÃO DE PLANTAS DO CEARÁ 🌿")
    print("=" * 60)
    print("\n MENU PRINCIPAL:\n")
    print("  1. > Cadastrar nova planta")
    print("  2. > Listar todas as plantas")
    print("  3. > Buscar planta por nome")
    print("  4. >️ Buscar plantas por família")
    print("  5. > Identificar por características")
    print("  6. > Ver estatísticas do sistema")
    print("  7. > Gerar relatório completo")
    print("  8. > Carregar plantas de exemplo")
    print("  0. > Sair do sistema")
    print("\n" + "=" * 60)


def cadastrar_planta_interativa(sistema: SistemaIdentificacao):
    """Função interativa para cadastrar uma nova planta"""
    limpar_tela()
    print("\n" + "=" * 60)
    print(" CADASTRAR NOVA PLANTA")
    print("=" * 60 + "\n")

    # Coletar informações básicas
    nome_popular = input("Nome popular da planta: ").strip()
    if not nome_popular:
        print(" Nome não pode ser vazio!")
        pausar()
        return

    descricao = input("Descrição da planta: ").strip()
    habitat = input("Habitat: ").strip()
    status = input("Status de conservação (ou ENTER para 'Não avaliado'): ").strip()
    status = status if status else "Não avaliado"

    # Coletar características
    print("\n Características da planta (digite uma por vez, ENTER vazio para terminar):")
    caracteristicas = []
    contador = 1
    while True:
        carac = input(f"  Característica {contador}: ").strip()
        if not carac:
            break
        caracteristicas.append(carac)
        contador += 1

    # Coletar classificação taxonômica
    print("\n Classificação Taxonômica:")
    reino = input("  Reino (ou ENTER para 'Plantae'): ").strip() or "Plantae"
    divisao = input("  Divisão: ").strip() or "Magnoliophyta"
    classe = input("  Classe: ").strip() or "Magnoliopsida"
    ordem = input("  Ordem: ").strip()
    familia = input("  Família: ").strip()
    genero = input("  Gênero: ").strip()
    especie = input("  Espécie: ").strip()

    # Criar classificação
    classificacao = ClassificacaoTaxonomica(
        reino=reino,
        divisao=divisao,
        classe=classe,
        ordem=ordem,
        familia=familia,
        genero=genero,
        especie=especie
    )

    # Criar e cadastrar planta
    planta = Planta(
        nome_popular=nome_popular,
        classificacao=classificacao,
        descricao=descricao,
        caracteristicas=caracteristicas,
        habitat=habitat,
        status_conservacao=status
    )

    sistema.cadastrar_planta(planta)
    print(f"\n Planta '{nome_popular}' cadastrada com sucesso!")
    pausar()


def listar_todas_plantas(sistema: SistemaIdentificacao):
    """Lista todas as plantas cadastradas"""
    limpar_tela()
    print("\n" + "=" * 60)
    print(" TODAS AS PLANTAS CADASTRADAS")
    print("=" * 60 + "\n")

    plantas = sistema.bioma.listar_plantas()

    if not plantas:
        print(" Nenhuma planta cadastrada ainda.")
    else:
        for i, planta in enumerate(plantas, 1):
            print(f"{i}. {planta}")

    pausar()


def buscar_por_nome(sistema: SistemaIdentificacao):
    """Busca uma planta pelo nome popular"""
    limpar_tela()
    print("\n" + "=" * 60)
    print(" BUSCAR PLANTA POR NOME")
    print("=" * 60 + "\n")

    nome = input("Digite o nome popular da planta: ").strip()
    planta = sistema.bioma.buscar_por_nome_popular(nome)

    if planta:
        print(planta.exibir_informacoes())
    else:
        print(f" Planta '{nome}' não encontrada.")

    pausar()


def buscar_por_familia(sistema: SistemaIdentificacao):
    """Busca plantas por família"""
    limpar_tela()
    print("\n" + "=" * 60)
    print("  BUSCAR PLANTAS POR FAMÍLIA")
    print("=" * 60 + "\n")

    # Mostrar famílias disponíveis
    familias = sistema.listar_familias()
    if familias:
        print("Famílias cadastradas:")
        for i, fam in enumerate(sorted(familias), 1):
            print(f"  {i}. {fam}")
        print()

    familia = input("Digite o nome da família: ").strip()
    plantas = sistema.bioma.buscar_por_familia(familia)

    if plantas:
        print(f"\n Encontradas {len(plantas)} planta(s) da família {familia}:\n")
        for i, planta in enumerate(plantas, 1):
            print(f"{i}. {planta}")
    else:
        print(f" Nenhuma planta da família '{familia}' encontrada.")

    pausar()


def identificar_por_caracteristicas(sistema: SistemaIdentificacao):
    """Identifica plantas por características"""
    limpar_tela()
    print("\n" + "=" * 60)
    print(" IDENTIFICAR PLANTAS POR CARACTERÍSTICAS")
    print("=" * 60 + "\n")

    print("Digite as características (uma por vez, ENTER vazio para terminar):\n")
    caracteristicas = []
    contador = 1
    while True:
        carac = input(f"  Característica {contador}: ").strip()
        if not carac:
            break
        caracteristicas.append(carac)
        contador += 1

    if not caracteristicas:
        print(" Nenhuma característica informada.")
        pausar()
        return

    plantas = sistema.identificar_por_caracteristicas(caracteristicas)

    if plantas:
        print(f"\n Encontradas {len(plantas)} planta(s) com essas características:\n")
        for i, planta in enumerate(plantas, 1):
            print(f"{i}. {planta}")
    else:
        print(" Nenhuma planta encontrada com essas características.")

    pausar()


def exibir_estatisticas(sistema: SistemaIdentificacao):
    """Exibe estatísticas do sistema"""
    limpar_tela()
    print("\n" + "=" * 60)
    print(" ESTATÍSTICAS DO SISTEMA")
    print("=" * 60 + "\n")

    stats = sistema.obter_estatisticas()

    print(f"Total de plantas: {stats['total_plantas']}")
    print(f"Total de famílias: {stats['total_familias']}")

    if stats['familias']:
        print(f"\nFamílias cadastradas: {', '.join(sorted(stats['familias']))}")
        print("\nDistribuição por família:")
        for familia, count in sorted(stats['plantas_por_familia'].items()):
            print(f"  • {familia}: {count} planta(s)")

    pausar()


def gerar_relatorio(sistema: SistemaIdentificacao):
    """Gera relatório completo"""
    limpar_tela()
    print(sistema.bioma.gerar_relatorio())
    pausar()


def carregar_plantas_exemplo(sistema: SistemaIdentificacao):
    """Carrega algumas plantas de exemplo do Ceará"""
    limpar_tela()
    print("\n Carregando plantas de exemplo...\n")

    # Juazeiro
    juazeiro = Planta(
        nome_popular="Juazeiro",
        classificacao=ClassificacaoTaxonomica(
            reino="Plantae", divisao="Magnoliophyta", classe="Magnoliopsida",
            ordem="Brassicales", familia="Rhamnaceae", genero="Ziziphus", especie="joazeiro"
        ),
        descricao="Árvore de médio porte, símbolo da resistência da Caatinga",
        caracteristicas=["Folhas pequenas e perenes", "Espinhos nos ramos", "Frutos amarelos", "Resistente à seca"],
        habitat="Caatinga, margens de rios",
        status_conservacao="Pouco preocupante"
    )

    # Mandacaru
    mandacaru = Planta(
        nome_popular="Mandacaru",
        classificacao=ClassificacaoTaxonomica(
            reino="Plantae", divisao="Magnoliophyta", classe="Magnoliopsida",
            ordem="Caryophyllales", familia="Cactaceae", genero="Cereus", especie="jamacaru"
        ),
        descricao="Cacto colunar icônico da Caatinga",
        caracteristicas=["Caule suculento verde", "Espinhos longos", "Flores brancas noturnas", "Fruto vermelho"],
        habitat="Caatinga, áreas rochosas",
        status_conservacao="Pouco preocupante"
    )

    # Umbuzeiro
    umbuzeiro = Planta(
        nome_popular="Umbuzeiro",
        classificacao=ClassificacaoTaxonomica(
            reino="Plantae", divisao="Magnoliophyta", classe="Magnoliopsida",
            ordem="Sapindales", familia="Anacardiaceae", genero="Spondias", especie="tuberosa"
        ),
        descricao="Árvore sagrada do sertão",
        caracteristicas=["Raízes tuberosas", "Folhas compostas", "Frutos ácidos", "Reserva de água"],
        habitat="Caatinga, solos profundos",
        status_conservacao="Vulnerável"
    )

    sistema.cadastrar_planta(juazeiro)
    sistema.cadastrar_planta(mandacaru)
    sistema.cadastrar_planta(umbuzeiro)

    print("\n 3 plantas de exemplo carregadas com sucesso!")
    pausar()


def main():
    """Função principal com menu interativo"""
    # Criar o sistema
    caatinga = BiomaCatinga("Caatinga", "Bioma exclusivamente brasileiro")
    sistema = SistemaIdentificacao(caatinga)

    # Loop principal
    while True:
        limpar_tela()
        exibir_menu_principal()

        opcao = input("\n> Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_planta_interativa(sistema)
        elif opcao == "2":
            listar_todas_plantas(sistema)
        elif opcao == "3":
            buscar_por_nome(sistema)
        elif opcao == "4":
            buscar_por_familia(sistema)
        elif opcao == "5":
            identificar_por_caracteristicas(sistema)
        elif opcao == "6":
            exibir_estatisticas(sistema)
        elif opcao == "7":
            gerar_relatorio(sistema)
        elif opcao == "8":
            carregar_plantas_exemplo(sistema)
        elif opcao == "0":
            limpar_tela()
            print("\n" + "=" * 60)
            print(" Obrigado por usar o Sistema de Plantas do Ceará!")
            print("=" * 60 + "\n")
            break
        else:
            print("\n Opção inválida! Tente novamente.")
            pausar()


if __name__ == "__main__":
    main()