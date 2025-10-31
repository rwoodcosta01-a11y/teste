import requests
import sys

def buscar_cotacao_dolar():
    """ção usa a biblioteca 'requests' (que instalamos)
    para buscar a cotação em uma API pública.
    """
    print("Buscando cotação do Dólar...")
    
    # Este é o URL da API de cotação
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    
    try:
        # A linha principal: 'requests.get' faz a mágica!
        response = requests.get(url)
        
        # 'raise_for_status' verifica se houve um erro HTTP (como 404 ou 500)
        response.raise_for_status()
        
        # O 'response.json()' transforma o texto da web em um dicionário Python
        dados = response.json()
        
        # 'USDBRL' é a chave que a API usa para os dados do Dólar-Real
        cotacao = dados['USDBRL']['bid']
        
        print(f"\n--- SUCESSO ---")
        print(f"1 Dólar (USD) vale R$ {cotacao} (BRL)")
        
    except requests.exceptions.RequestException as e:
        print(f"\n--- ERRO ---")
        print(f"Falha ao conectar na API de cotação: {e}")
    except KeyError:
        print(f"\n--- ERRO ---")
        print("Não foi possível encontrar a cotação 'USDBRL' na resposta da API.")

def verificar_versao_python():
    """Função bônus para provar que estamos usando o Python 3.8"""
    print("---------------------------------")
    print(f"Este script está rodando no: {sys.version.split()[0]}")
    print("---------------------------------")


# --- Ponto de Entrada Principal ---
if __name__ == "__main__":
    verificar_versao_python()
    buscar_cotacao_dolar()