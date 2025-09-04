from utils.positive_words import positive_words
from utils.negative_words import negative_words
from utils.neutral_words import neutral_words

"""sample_sentences = [
    'there was a cockroach in my soup',
    'she gave a brilliant presentation',
    'Have you tried any new restaurants or cafes recently',
    'The player ran with the ball and scored a goal.',
    'I went to the fridge for water and came back with cake.',
    'The service was terrible and the food tasted awful.',
    'It’s not that he lacked the ability to succeed; rather, he refused to put in the effort required to even begin',
    'I ate a good sweet today in saturday market.',
    'The food tasted amazing, but the service was slow, and the atmosphere was just okay.',
    'i felt joyful after the exam',
    'The movie was not bad, but it wasn’t exactly good either',
    'The Actors did a great job with their acting ,but the movie was boring',
    'Have you tried any new restaurants or cafes recently',
    'An apple a day keeps the doctor away- if you throw it hard enough',
    'He was chalant and helped his friend',
    'the service was rude and the wait was too long',
    'The computer generated a list of random numbers',
    'The weather was horrible yesterday',
    'While the weather was pleasant, the traffic made our journey stressful.',
    'She received an award for her outstanding performance',
    'The trip was exciting, but the weather was terrible, and the hotel was decent.',
    'I hope it doesn’t rain tomorrow',
    'His presentation was impressive, though he spoke too fast, and the slides were fine.',
]"""

sample_sentences=[
'The food was tasty and fresh',
'But the service was very slow',
'We have computer class in the afternoon',
'The movie was boring and too long',
'I felt disappointed after watching it',
'the library opens at 9 o’clock It closes in the evening at 5',
'He argued with his friend yesterday Both of them were very angry',
'I am very happy with my project result',
'My teacher praised my effort',
'The food was cold and tasteless The waiter behaved rudely too',
'The trip was wonderful and full of joy',
'We enjoyed every moment together',
'I placed the pen on the table Then I opened my notebook',

]


def positive_check(word):
    return word in positive_words


def negative_check(word):
    return word in negative_words


def neutral_check(word):
    return word in neutral_words


for sentence in sample_sentences:
    sentence_score = 0
    words = sentence.split()
    for test_word in words:
        score = 0
        is_positive = positive_check(test_word)
        is_negative = negative_check(test_word)
        is_neutral = neutral_check(test_word)
        if is_positive:
            score = score + 1
        if is_negative:
            score = score - 1
        sentence_score += score
    print(f"{sentence} ===> {sentence_score}")




"""for sentence in sample_sentences:
    words = sentence.split()
    for test_word in words:
        is_positive = positive_check(test_word)
        is_negative = negative_check(test_word)
        is_neutral = neutral_check(test_word)
        print(test_word)
        print(f'\t is positive = {is_positive}')
        print(f'\t is negative = {is_negative}')
        print(f'\t is neutral = {is_neutral}')"""
