import transformers
from typing import List, Literal


def _load_terminators(
        model_name: Literal['Bllossom-ELO'],
        pipeline: transformers.Pipeline
    ) -> List[int]:
    """ load llm

    [Params]
    model_name : Literal['Bllossom-ELO']
    pipeline   : transformers.Pipeline

    [Return]
    terminators : List[int]
    """
    if model_name == 'Bllossom-ELO':
        return [
            pipeline.tokenizer.eos_token_id,
            pipeline.tokenizer.convert_tokens_to_ids('<|eot_id|>')
        ]
    
    else:
        return None
