import transformers
from hate_speech_mitigation.utils import get_model_response, load_prompt
from typing import List


MATCHES = {
    'gender': '성별',
    'age': '나이',
    'race': '인종',
    'religion': '지역',
    'politics': '정치',
    'job': '직업',
    'disability': '무능',
    'individual': '개인',
    'others': '기타'
}


def mitigate_hate_speech(
        hate_speech: str,
        labels: List[str],
        rationales: List[List[int]]
    ) -> str:
    """ mitigate hate speech

    [Params]
    hate_speech : str
    labels      : List[str]
    rationales  : List[List[int]]

    [Return]
    mitigated_hate_speech : str
    """
    task = 'mitigate_hate_speech'

    mitigated_hate_speech = get_model_response(
        model_name='Bllossom-ELO',
        system_prompt=load_prompt(role='system', task=task),
        user_prompt=load_prompt(role='user', task=task).format(
            hate_speech=hate_speech,
            labels=', '.join([MATCHES[l] for l in labels]),
            rationales=', '.join(hate_speech[span[0]:span[1]+1] for span in rationales)
        )
    )

    return mitigated_hate_speech
