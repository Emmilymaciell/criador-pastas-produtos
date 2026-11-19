import os

# Pasta-alvo: variável de ambiente PROG_PRODUTOS_DIR ou ./produtos ao lado do script.
BASE_DIR_PADRAO = os.environ.get(
    "PROG_PRODUTOS_DIR",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "produtos"),
)

def main():
    print("==================================================")
    print("      CRIADOR DE ÁRVORE DE PASTAS - Programa")
    print("==================================================")
    
    base_dir = BASE_DIR_PADRAO
    
    print(f"Diretório alvo:\n{base_dir}\n")
    print("OBS: defina PROG_PRODUTOS_DIR para usar outra pasta.")
    print("--------------------------------------------------")
    
    try:
        ano = int(input("Digite o ANO (ex: 2027): "))
        mes_inicio = int(input("Digite o número do mês de INÍCIO (1 a 12): "))
        mes_fim = int(input("Digite o número do mês de FIM (1 a 12): "))
        seq_inicio = int(input("Qual o número da primeira pasta? (Ex.: 7 para começar em '07.'; para começar no 01, digite 1): "))
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos!")
        input("Pressione ENTER para sair...")
        return

    meses_nomes = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }

    # Grupos e produtos com títulos genéricos fictícios (os títulos do contrato real foram removidos)
    estrutura_anexos = {
        "G1": [
            "P1.1 - Relatorio de Coordenacao",
            "P1.2 - Relatorio de Comunicacao",
            "P1.3 - Relatorio de Tecnologia da Informacao",
        ],
        "G2": [
            "P2.1 - Relatorio de Engenharia",
            "P2.2 - Relatorio de Analise de Projetos",
            "P2.3 - Relatorio de Acompanhamento de Obras",
        ],
        "G3": [
            "P3.1 - Relatorio de Qualidade",
            "P3.2 - Planos de Inspecao",
            "P3.3 - Relatorio de Inspecao",
        ],
        "G4": [
            "P4.1 - Relatorio Financeiro",
            "P4.2 - Relatorio de Riscos",
        ],
        "G5": [
            "P5.1 - Relatorio Juridico",
            "P5.2 - Relatorio de Gestao Contratual",
        ],
    }

    seq_atual = seq_inicio
    pastas_mes_criadas = 0

    print("\nIniciando a criação das pastas...")
    print("--------------------------------------------------")

    for mes in range(mes_inicio, mes_fim + 1):
        nome_mes = meses_nomes.get(mes, "Desconhecido")
        
        # Formata o número com 2 dígitos (ex: 07, 08, 09)
        nome_pasta_mes = f"{seq_atual:02d}. {nome_mes} {ano}"
        caminho_mes = os.path.join(base_dir, nome_pasta_mes)
        
        try:
            # Cria a pasta do mês
            os.makedirs(caminho_mes, exist_ok=True)
            
            # Cria G1 a G5, a pasta 'Anexos' e as subpastas P
            for grupo, anexos in estrutura_anexos.items():
                caminho_anexos = os.path.join(caminho_mes, grupo, "Anexos")
                
                # A função makedirs já cria as pastas intermediárias (G1/Anexos, etc)
                os.makedirs(caminho_anexos, exist_ok=True)
                
                for anexo in anexos:
                    caminho_final = os.path.join(caminho_anexos, anexo)
                    os.makedirs(caminho_final, exist_ok=True)
            
            print(f"[OK] {nome_pasta_mes}")
            pastas_mes_criadas += 1
            seq_atual += 1
            
        except Exception as e:
            print(f"[ERRO] Falha ao criar {nome_pasta_mes}. Detalhes: {e}")

    print("--------------------------------------------------")
    print(f"Sucesso! {pastas_mes_criadas} pastas mensais e todas as suas respectivas subpastas foram criadas.")
    input("\nPressione ENTER para fechar o programa...")

if __name__ == '__main__':
    main()
