import ffmpeg
import os

def comprimir_video(arquivo_entrada, arquivo_saida, crf=23):
    """
    Comprime um vídeo usando FFmpeg.
    
    Parâmetros:
    arquivo_entrada (str): Caminho do vídeo original.
    arquivo_saida (str): Caminho onde o vídeo comprimido será salvo.
    crf (int): Nível de qualidade (0-51). 23 é o padrão, 18 é excelente, 28 é menor e com menos qualidade.
    """
    
    if not os.path.exists(arquivo_entrada):
        print(f"Erro: O arquivo '{arquivo_entrada}' não foi encontrado.")
        return

    print(f"Iniciando a compressão de: {arquivo_entrada}")
    print("Isso pode demorar um pouco dependendo do tamanho do vídeo...")

    try:
        # Configurando os parâmetros do FFmpeg
        stream = ffmpeg.input(arquivo_entrada)
        
        # libx264 é o codec de vídeo padrão (MP4)
        # aac é o codec de áudio
        # preset='medium' (você pode mudar para 'slow' para comprimir mais, porém demora mais tempo)
        stream = ffmpeg.output(stream, arquivo_saida, vcodec='libx264', crf=crf, acodec='aac', preset='medium')
        
        # Executa o comando e sobrescreve o arquivo de saída se ele já existir (-y)
        ffmpeg.run(stream, overwrite_output=True, quiet=True)
        
        print(f"Sucesso! Vídeo salvo como: {arquivo_saida}")
        
        # Mostra a diferença de tamanho
        tamanho_original = os.path.getsize(arquivo_entrada) / (1024 * 1024)
        tamanho_final = os.path.getsize(arquivo_saida) / (1024 * 1024)
        print(f"Tamanho original: {tamanho_original:.2f} MB")
        print(f"Tamanho final: {tamanho_final:.2f} MB")

    except ffmpeg.Error as e:
        print("Ocorreu um erro durante a compressão. Verifique se o FFmpeg está instalado corretamente.")
        print(e.stderr)

# --- Como usar o script ---
if __name__ == "__main__":
    # Substitua pelos nomes dos seus vídeos
    video_original = "duasmetades.mp4"
    video_comprimido = "duasmetades_comprimido.mp4"
    
    # CRF 23 é o padrão recomendado para manter a qualidade e diminuir o tamanho
    comprimir_video(video_original, video_comprimido, crf=23)