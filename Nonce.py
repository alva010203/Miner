import hashlib, time


try:
    def findnonce(datatoHash: bytes, bitsTOzero: int):
        nonce = 0  # Inicializa o valor do nonce
        valor = (1 << (256 - bitsTOzero)) - 1  # Calcula o valor limite para a comparação
        tempi_i = time.time()  # Registra o tempo inicial

        while True:
            n_by = nonce.to_bytes(4, byteorder='big')  # Converte o nonce para bytes (big endian)
            resul_hash = hashlib.sha256(n_by + datatoHash).hexdigest()  # Criação do hash utilizando sha256
            if int(resul_hash, 16) <= valor:  # Converte o hash hexadecimal para inteiro
                break
            nonce += 1

        tempo_f = time.time() - tempi_i  # Calcula o tempo total de execução
        return nonce, tempo_f  # Retorna o nonce e o tempo de execução

    def preencher_tabela(): #conversão
        texto_bytes = [
            ("Esse é fácil", 8),
            ("Esse é fácil", 10),
            ("Esse é fácil", 15),
            ("Texto maior muda o tempo?", 8),
            ("Texto maior muda o tempo?", 10),
            ("Texto maior muda o tempo?", 15),
            ("É possível calcular esse?", 18),
            ("É possível calcular esse?", 19),
            ("É possível calcular esse?", 20)
        ]
        resultado = []

        for texto, bits in texto_bytes:
            data_To_hash = texto.encode("utf-8")  # Converte o texto para bytes
            nonce, tempo = findnonce(data_To_hash, bits)  # Chama a função para encontrar o nonce e o tempo
            resultado.append((texto, bits, nonce, tempo))  # Adiciona uma tupla com os resultados
            print(f"Texto: '{texto}', Bits: {bits}, Nonce: {nonce}, Tempo: {tempo:.6f} S")

                #Abre e escreve a tabela
        try:
            with open("tabela.txt", "w") as file:
                file.write("Texto a validar\tBits em zero\tNonce\tTempo (s)\n") #\t (caractere de tabulação)
                for texto, bits, nonce, tempo in resultado:
                    file.write(f"{texto}\t{bits}\t{nonce}\t{tempo:.6f}\n")
            print("Tabela salva em 'tabela.txt'.")
        except IOError as e:
            print(f"Erro de entrada/saída: {e}")
        except Exception as e:
            print(f"Erro {e}")

    def executar():
        preencher_tabela()

    executar()


except Exception as e :
    print({e})




