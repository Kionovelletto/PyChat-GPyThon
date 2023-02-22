import openai
from env.get_env import set_env

# GET API KEY IN FUNCTION
env = set_env(['openai.api_key'])
openai.api_key = env['openai.api_key']

# SET ENGINE INSTRUCT TEXT AI, new model text-davinci-003
# https://help.openai.com/en/articles/6779149-how-do-text-davinci-002-and-text-davinci-003-differ
model_engine = 'text-davinci-003'

while True:
        print()
        prompt = input('Faça seu questionamento ao Chat GPyThon 💬: ')
        print()
        print('[Chat 🤖] Sua mensagem está sendo processada, aguarde ⏳\n')
        #print()

        # CONFIGURING ANSWER
        completion = openai.Completion.create(
                engine = model_engine,
                prompt = prompt,
                max_tokens = 1024,
                temperature = 0.5,
        )

        # PRINT CHATGPT RESPONSE
        response = completion.choices[0].text
        print(response)
        print()
       
        # CONFIGURING A CHAT OUTPUT
        out = input('[Chat 🤖] Você deseja fazer outro questionamento? (s)im👍 ou (n)ão👎: ')
        if out != 's':
            print('Saindo... 👋	\n')
            break