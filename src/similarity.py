from sentence_transformers import util
from sacrebleu.metrics import CHRF
import pyter
from config import MODEL

def compute_similarity(orig_text: str, potential_text: str) -> float:
    embedding_orig_text = MODEL.encode(str(orig_text), convert_to_tensor=True)
    embedding_potential_text = MODEL.encode(str(potential_text), convert_to_tensor=True)
    return round(util.pytorch_cos_sim(embedding_orig_text, embedding_potential_text).item(), 4)

def compute_chrf_score(orig_text: str, potential_text: str) -> float:
    potential_text = potential_text or 'text'
    orig_text = orig_text or 'aa'
    chrf = CHRF()
    return float(str(chrf.corpus_score([str(orig_text)], [[str(potential_text)]]).split('=')[1].split(' ')[1]))

def evaluate_sacrebleu(reference, hypothesis):
    bleu = sacrebleu.corpus_bleu([hypothesis], [[reference]])
    return round(bleu.score, 2)

def evaluate_ter(reference, hypothesis):
    if not reference.strip() or not hypothesis.strip():
        return None
    ter_score = pyter.ter(reference.split(), hypothesis.split())
    return round(ter_score, 2)
