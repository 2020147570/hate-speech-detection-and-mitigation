from hate_speech_mitigation.mitigate_hate_speech import mitigate_hate_speech

original_text = '똥덕도 솔직히 들어오고 지 수능성적 까먹는거 마냥 난 여대 오고싶어서~여기왔어 ㅇㅈㄹ하는거지 저 성적대에 선택권이 어딨냐? 그냥 개박은 성적으로 인서울 기어들어간거지'

processed_text = mitigate_hate_speech(hate_speech=original_text)

print(processed_text)