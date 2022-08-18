import boto3
import Polly
def translate(txt, id):

    translate = boto3.client(service_name='translate', region_name = 'us-east-1')
    result = translate.translate_text(Text=txt,
                                      SourceLanguageCode="en", TargetLanguageCode="es")
    print(txt)
    Polly.generate_audio(result.get('TranslatedText'), id, txt)

