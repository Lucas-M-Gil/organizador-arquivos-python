import os
import shutil

def organizar_arquivos(pasta):
    if not os.path.isdir(pasta):
        print("❌ Caminho inválido.")
        return

    arquivos = os.listdir(pasta)

    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta, arquivo)

        if os.path.isfile(caminho_arquivo):
            extensao = arquivo.split('.')[-1]

            pasta_destino = os.path.join(pasta, extensao.upper() + "_files")

            if not os.path.exists(pasta_destino):
                os.mkdir(pasta_destino)

            novo_caminho = os.path.join(pasta_destino, arquivo)

            shutil.move(caminho_arquivo, novo_caminho)
            print(f"✅ {arquivo} movido para {pasta_destino}")

    print("✅ Organização concluída!")

if __name__ == "__main__":
    caminho = input("Digite o caminho da pasta que deseja organizar: ")
    organizar_arquivos(caminho.strip())
