import json
import logging
from hate_speech_mitigation.mitigate_hate_speech import mitigate_hate_speech
from hate_speech_mitigation.self_verify_and_feedback import self_verify_and_feedback
from typing import List


def step_2_hate_speech_mitigation(
        original_speech: str,
        rationales: List[List[int]]
    ):
    """main"""
    buffer = [{'step': [0, 'initialization'], 'original_speech': original_speech}]

    verification_flag, iteration, feedback = False, 0, ''
    while not verification_flag and iteration < 3:
        iteration += 1

        logger.info(f"Iteration #{iteration}:")

        # Step - mitigate hate speech with feedback
        logger.info("> mitigate hate speech")

        mitigated_speech, instruction, response = mitigate_hate_speech(
            original_speech=original_speech,
            rationales=rationales,
            feedback=feedback # empty string at first iteration
        )

        buffer.append({'step': [iteration, 'mitigate_hate_speech'], 'instruction': instruction, 'response': response})
        logger.info(f">> Original speech : {original_speech}")
        logger.info(f">> Mitigated speech: {mitigated_speech}")

        # Step - self verify and feedback
        logger.info("> self verify and feedback")

        verification_flag, feedback, instruction, response = self_verify_and_feedback(
            original_speech=original_speech,
            mitigated_speech=mitigated_speech
        )

        buffer.append({'step': [iteration, 'self_verify_and_feedback'], 'instruction': instruction, 'response': response})
        logger.info(f">> Verification    : {verification_flag}")
        logger.info(f">> Feedback        : {feedback}")
    
    logger.info("Iteration done.")
    with open('hate_speech_mitigation/buffer.json', 'w', encoding='utf-8') as file:
        json.dump(buffer, file, ensure_ascii=False, indent=4)
    
    return mitigated_speech


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    original_speech_list = ['똥덕도 솔직히 들어오고 지 수능성적 까먹는거 마냥 난 여대 오고싶어서~여기왔어 ㅇㅈㄹ하는거지 저 성적대에 선택권이 어딨냐? 그냥 개박은 성적으로 인서울 기어들어간거지']
    rationales_list = [
        [[0, 1], [44, 46], [72, 74], [85, 91]]
    ]
    
    # Init
    from hate_speech_mitigation.utils._load_pipeline import _load_pipeline
    _load_pipeline('Bllossom-ELO')
    # Init

    mitigated_speech_list = [
        step_2_hate_speech_mitigation(
            original_speech=original_speech,
            rationales=rationales
        )
        for original_speech, rationales in zip(original_speech_list, rationales_list)
    ]

    print(mitigated_speech_list)
