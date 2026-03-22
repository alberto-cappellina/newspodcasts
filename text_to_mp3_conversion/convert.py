import boto3


def newsletter_to_audio():

    key =


    client = boto3.client(
        'polly',
        region_name='eu-west-1',  # o la tua region
        aws_access_key_id='',
        aws_secret_access_key=''
    )

    response = client.synthesize_speech(
        Text='Il testo da convertire',
        OutputFormat='mp3',
        VoiceId='Carla'  # voce italiana
    )

    with open('output.mp3', 'wb') as f:
        f.write(response['AudioStream'].read())
