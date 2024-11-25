from .utils import get_model_response, load_prompt
from typing import List, Tuple


def mitigate_hate_speech(
        original_speech: str,
        rationales: List[List[int]],
        feedback: str=''
    ) -> Tuple[str, str]:
    """ mitigate hate speech

    [Params]
    original_speech : str
    rationales      : List[List[int]]
    feedback        : str (default '')

    [Return]
    mitigated_speech : str
    response         : str
    """
    if feedback == '':
        task = 'mitigate_hate_speech'

        instruction, response = get_model_response(
            model_name='Bllossom-ELO',
            system_prompt=load_prompt(role='system', task=task),
            user_prompt=load_prompt(role='user', task=task).format(
                original_speech=original_speech,
                rationales=', '.join(original_speech[span[0]:span[1]+1] for span in rationales)
            )
        )
    
    else:
        task = 'mitigate_hate_speech_with_feedback'

        instruction, response = get_model_response(
            model_name='Bllossom-ELO',
            system_prompt=load_prompt(role='system', task=task),
            user_prompt=load_prompt(role='user', task=task).format(
                original_speech=original_speech,
                rationales=', '.join(original_speech[span[0]:span[1]+1] for span in rationales),
                feedback=feedback
            )
        )

    mitigated_speech = response.replace('**완화된 문장:**\n', '')

    return mitigated_speech, instruction, response
