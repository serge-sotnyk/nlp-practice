import sys
import numpy as np
from keras_bert import load_trained_model_from_checkpoint
from scripts.tokenization import FullTokenizer

#_folder = "d:\\nlp\\multi_cased_L-12_H-768_A-12\\"
_folder = "d:\\nlp\\cased_L-12_H-768_A-12\\"
_config_path = _folder + 'bert_config.json'
_checkpoint_path = _folder + 'bert_model.ckpt'
_vocab_path = _folder + 'vocab.txt'

_tokenizer = FullTokenizer(vocab_file=_vocab_path, do_lower_case=False)
_model = None

max_seq_len = 64  # 512


def load_bert_model():
    global _model
    if _model is None:
        _model = load_trained_model_from_checkpoint(_config_path, _checkpoint_path, training=True, seq_len=max_seq_len)
    return _model


def calc_entailment_prob(sentence_1: str, sentence_2: str, model=load_bert_model()) -> (float, float):
    tokens_sen_1 = _tokenizer.tokenize(sentence_1)[:30]
    tokens_sen_2 = _tokenizer.tokenize(sentence_2)[:30]

    tokens = ['[CLS]'] + tokens_sen_1 + ['[SEP]'] + tokens_sen_2 + ['[SEP]']
    # print(tokens)

    # преобразуем строковые токены в числовые индексы:
    token_input = _tokenizer.convert_tokens_to_ids(tokens)
    # удлиняем до 512
    token_input = token_input + [0] * (max_seq_len - len(token_input))

    # маска в этом режиме все 0
    mask_input = [0] * max_seq_len

    # в маске предложений под второй фразой, включая конечный SEP, надо поставить 1, а все остальное заполнить 0
    seg_input = [0] * max_seq_len
    len_1 = len(tokens_sen_1) + 2  # длина первой фразы, +2 - включая начальный CLS и разделитель SEP
    for i in range(len(tokens_sen_2) + 1):  # +1, т.к. включая последний SEP
        seg_input[len_1 + i] = 1  # маскируем вторую фразу, включая последний SEP, единицами
    # print(seg_input)

    # конвертируем в numpy в форму (1,) -> (1,512)
    token_input = np.asarray([token_input])
    mask_input = np.asarray([mask_input])
    seg_input = np.asarray([seg_input])

    # пропускаем через нейросеть...
    predicts = model.predict([token_input, seg_input, mask_input])[
        1]  # в [1] ответ на вопрос, является ли второе предложение логичным по смыслу
    # print('Sentence is okey: ', not bool(np.argmax(predicts, axis=-1)[0]), predicts)
    # print('Sentence is okey:', int(round(predicts[0][0] * 100)),
    #      '%')  # [[0.9657724  0.03422766]] - левое число вероятность что второе предложение подходит по смыслу, а правое - что второе предложение случайное
    return predicts[0]


def main():
    model = load_bert_model()
    print(model.summary())
    sentence_1 = 'Roy Big Country Nelson KOs Kongo'
    sentence_2 = 'Roy Nelson Knocks Out Cheick Kongo In The First Round'
    p = calc_entailment_prob(sentence_1, sentence_2)
    print(sentence_1)
    print(sentence_2)
    print("Entailment probs:", p)
    bp = calc_entailment_prob(sentence_2, sentence_1)
    print("Backward entailment probs:", bp)


if __name__ == "__main__":
    main()
