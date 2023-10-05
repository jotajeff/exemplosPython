from flashtext import KeywordProcessor

keyword_processor = KeywordProcessor()

keyword_processor.add_keyword('New Delhi', 'NCR region')
new_sentence = keyword_processor.replace_keywords('I love Big Apple and new delhi.')
print(new_sentence)

