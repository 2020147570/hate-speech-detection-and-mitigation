from typing import Literal
from ._dir import current_dir


def load_prompt(
        role: Literal['assistant', 'system', 'user'],
        task: str
    ) -> str:
    """ load prompt

    [Params]
    role : Literal['assistant', 'system', 'user']
    task : str

    [Return]
    prompt_template : str
    """
    with open(f'{current_dir}/../prompts/{role}/{task}.txt', 'r') as file:
        prompt_template = file.read()
    
    return prompt_template
