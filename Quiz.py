import random
import json

with open('capitals.json','r') as f:
    capitals=json.load(f)



for quiz in range(35):
    question=open('question_paper_%s' %(quiz+1),'w')
    answer=open('answer_sheet_%s' %(quiz+1),'w')

    question.write('Name:\n\nDate:\n\nPeriod:\n\n')
    question.write((' '*20)+'Capital Quiz %s\n' %(quiz+1))
    states = list(capitals.keys())
    random.shuffle(states)
    for i in range(50):


        correct=capitals[states[i]]

        wrong=list(capitals.values())
        del wrong[wrong.index(correct)]
        wrong=random.sample(wrong,3)
        options=wrong+[correct]
        random.shuffle(options)
        question.write( '\n%s.What is the capital of %s\n\n' % (i + 1, states[i]))
        for j in range(4):
            question.write('%s.%s\n' %('ABCD'[j],options[j]))

        answer.write('%s.%s\n' %(i+1,'ABCD'[options.index(correct)]))
    question.close()
    answer.close()