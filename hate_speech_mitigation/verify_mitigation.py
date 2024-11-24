import transformers
from hate_speech_mitigation.utils import get_model_response, load_prompt


def verify_mitigation(
        original_speech: str,
        mitigated_speech: str
    ) -> bool:
    """ verfiy mitigation

    [Params]
    original_speech  : str
    mitigated_speech : str

    [Return]
    verification_flag : bool
    """
    task = 'verify_mitigation'

    verification_flag = get_model_response(
        model_name='Bllossom-ELO',
        system_prompt=load_prompt(role='system', task=task),
        user_prompt=load_prompt(role='user', task=task).format(
            original_speech=original_speech,
            mitigated_speech=mitigated_speech
        )
    )

    return True if verification_flag == '참' else False if verification_flag == '거짓' else None
