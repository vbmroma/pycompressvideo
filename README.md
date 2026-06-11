Compressor de Vídeo com Python 🎬

Este é um script simples e eficiente em Python para comprimir vídeos utilizando a biblioteca `ffmpeg-python` (um wrapper para o poderoso **FFmpeg**). 
Ele permite reduzir significativamente o tamanho de arquivos de vídeo mantendo uma ótima qualidade de imagem.

Funcionalidades

- Compressão de vídeo utilizando o codec padrão `libx264` (MP4) e áudio `aac`.
- Controle dinâmico de qualidade e tamanho através do parâmetro CRF (Constant Rate Factor).
- Comparativo automático no terminal exibindo o tamanho original e o tamanho final do vídeo (em MB).
- Tratamento de erros para arquivos não encontrados ou problemas na execução do FFmpeg.

Pré-requisitos

Antes de rodar o script, certifique-se de ter os seguintes requisitos na sua máquina:

1. **Python 3.x**: Download Python
2. **FFmpeg**: O software FFmpeg precisa estar instalado no seu sistema e adicionado às variáveis de ambiente (`PATH`).
   - **Windows**: Guia de Instalação
   - **Linux**: `sudo apt install ffmpeg`
   - **macOS**: `brew install ffmpeg`
3. **Biblioteca ffmpeg-python**: Dependência do projeto. Instale executando o comando abaixo:
   ```bash
   pip install ffmpeg-python
   ```

Como Usar

1. Faça o clone deste repositório ou baixe o arquivo `compress.py`.
2. Coloque o vídeo que deseja comprimir na mesma pasta do script (ou utilize caminhos absolutos).
3. Abra o arquivo `compress.py` e edite as variáveis no final do arquivo com o nome dos seus vídeos:
   ```python
   video_original = "seu_video.mp4"
   video_comprimido = "seu_video_comprimido.mp4"
   ```
4. Execute o script no terminal:
   ```bash
   python compress.py
   ```

Entendendo o parâmetro CRF

O script permite o ajuste da taxa de compressão através do parâmetro **CRF** (*Constant Rate Factor*). 

- **Intervalo**: 0 a 51.
- **23 (Padrão)**: Recomendado para ótimo equilíbrio entre tamanho e qualidade.
- **18 (Excelente)**: Prioriza a qualidade, gerando arquivos um pouco maiores.
- **28 (Baixa qualidade)**: Prioriza um tamanho de arquivo menor em troca de alguma perda de qualidade visual.

Para alterar, basta modificar o valor passado na função principal dentro do código:
```python
comprimir_video(video_original, video_comprimido, crf=28)
```
