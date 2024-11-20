from hate_speech_mitigation.utils import get_model_response, load_prompt


def mitigate_hate_speech(
        hate_speech: str
    ):
    """ mitigate hate speech

    [Param]
    hate_speech : str

    [Return]
    mitigated_hate_speech : str
    """
    task = 'mitigate_hate_speech'

    mitigated_hate_speech = get_model_response(
        model_name='Bllossom-ELO',
        system_prompt=load_prompt(role='system', task=task),
        user_prompt=load_prompt(role='user', task=task).format(
            hate_speech=hate_speech
        )
    )

    return mitigated_hate_speech
