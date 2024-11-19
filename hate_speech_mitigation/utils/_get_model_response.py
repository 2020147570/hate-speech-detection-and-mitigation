from ._load_pipeline import _load_pipeline
from ._load_terminators import _load_terminators


def get_model_response(
    model_name: str,
    system_prompt: str,
    user_prompt: str,
    do_sample: bool=False,
    temperature: float=1.0,
    top_p: float=0.0
    ) -> str:
    """ load llm

    [Params]
    model_name    : str
    system_prompt : str
    user_prompt   : str
    do_sample     : bool (default: False),
    temperature   : float (default: 1.0),
    top_p         : float (default: 0.0)

    [Return]
    response : str
    """
    pipeline = _load_pipeline(model_name=model_name)

    prompt = pipeline.tokenizer.apply_chat_template(
        conversation=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt}
        ],
        tokenize=False,
        add_generation_prompt=True
    )

    outputs = pipeline(
        prompt,
        max_new_tokens=TOKEN_LENGTH_LIMIT,
        eos_token_id=_load_terminators(model_name=model_name, pipeline=pipeline),
        do_sample=do_sample,
        temperature=temperature,
        top_p=top_p
    )

    return outputs[0]['generated_text'][len(prompt):]


if __name__ == 'hate_speech_mitigation.utils._get_model_response':
    TOKEN_LENGTH_LIMIT = 2048
