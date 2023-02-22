import openai
from env.get_env import set_env

# GET API KEY IN FUNCTION
env = set_env(['openai.api_key'])
openai.api_key = env['openai.api_key']

# ENGINE INSTRUCT TEXT AI, new model text-davinci-003
# https://help.openai.com/en/articles/6779149-how-do-text-davinci-002-and-text-davinci-003-differ
model_engine = 'text-davinci-003'

while True:
        print()
        prompt = input('Faça seu questionamento ao Chat GPyThon: ')
        print()
        print('[Chat] Sua mensagem está sendo processada, aguarde ...')
        print()

        # CONFIGURE A RESPONSE QUESTION
        completion = openai.Completion.create(
                engine = model_engine,
                prompt = prompt,
                max_tokens = 1024,
                temperature = 0.5,
        )

        
        response = completion.choices[0].text
        print(response)
        print()
       

        out = input('[Chat] Você deseja fazer outro questinamento? (s)im ou (n)ão: ')
        if out != 's':
            print('Saindo...')
            break