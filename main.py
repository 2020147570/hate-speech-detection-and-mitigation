from hate_speech_mitigation.mitigate_hate_speech import mitigate_hate_speech
from hate_speech_mitigation.verify_mitigation import verify_mitigation
from typing import List


def main(
        original_speech: str,
        labels: List[str],
        rationales: List[List[int]]
    ):
    """Main"""
    verification_flag = True
    while verification_flag:
        mitigated_speech = mitigate_hate_speech(
            hate_speech=original_speech,
            labels=labels,
            rationales=rationales
        )

        verification_flag = verify_mitigation(
            original_speech=original_speech,
            mitigated_speech=mitigated_speech
        )
    
    print(f"Original speech: {original_speech}")
    print(f"Mitigated_speech: {mitigated_speech}")


if __name__ == '__main__':
    main(
        original_speech='똥덕도 솔직히 들어오고 지 수능성적 까먹는거 마냥 난 여대 오고싶어서~여기왔어 ㅇㅈㄹ하는거지 저 성적대에 선택권이 어딨냐? 그냥 개박은 성적으로 인서울 기어들어간거지',
        labels=['gender', 'disability'],
        rationales=[[0, 1], [44, 46], [72, 74], [85, 91]]
    )
