import re
from .utils import get_model_response, load_prompt
from typing import Tuple


def self_verify_and_feedback(
        original_speech: str,
        mitigated_speech: str
    ) -> Tuple[bool, str, str]:
    """ self verify and feedback

    [Params]
    original_speech  : str
    mitigated_speech : str

    [Return]
    verification_flag : bool
    feedback          : str
    response          : str
    """
    task = 'self_verify_and_feedback'

    response = get_model_response(
        model_name='Bllossom-ELO',
        system_prompt=load_prompt(role='system', task=task),
        user_prompt=load_prompt(role='user', task=task).format(
            original_speech=original_speech,
            mitigated_speech=mitigated_speech
        )
    )

    pattern = r"\*\*검증:\*\*\s*(참|거짓)\s*\*\*설명:\*\*\s*(.+)"
    match = re.search(pattern, response, re.DOTALL)
    
    if match:
        verification_flag = True if match.group(1) == '참' else False if match.group(2) == '거짓' else None
        feedback = match.group(2)
        return verification_flag, feedback, response
    
    return None, None, response
