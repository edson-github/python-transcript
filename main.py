from youtube_transcript_api import YouTubeTranscriptApi
from googletrans import Translator

def get_translated_transcript(video_id):
    """Extrai a transcrição de um vídeo do YouTube, traduz para português e retorna como texto.

    Args:
        video_id: O ID do vídeo do YouTube.

    Returns:
        Uma string com a transcrição traduzida, ou None em caso de erro.
    """

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        translator = Translator()
        translated_text = ""
        for entry in transcript:
            translated_text += translator.translate(entry['text'], dest='pt').text + " "
        return translated_text
    except Exception as e:
        print(f"Erro ao extrair ou traduzir a transcrição: {e}")
        return None

def save_transcript_to_file(transcript, filename="transcricao.txt"):
    """Salva a transcrição em um arquivo de texto.

    Args:
        transcript: A transcrição como uma string.
        filename: O nome do arquivo de saída (opcional).
    """

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(transcript)
        print(f"Transcrição salva em: {filename}")
    except Exception as e:
        print(f"Erro ao salvar a transcrição: {e}")

# Exemplo de uso
video_id = "iUD5pPpcyZk"  # Substitua pelo ID do vídeo desejado
transcript = get_translated_transcript(video_id)

if transcript:
    save_transcript_to_file(transcript)
