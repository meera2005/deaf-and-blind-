# import os
# import openai

# openai.api_key = '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'
# # openai.api_key = os.environ.get("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")
# # openai.organization=os.getenv("OPENAI_ORGANIZATION")

# response=openai.ChatCompletion.create(
#             model='gpt-3.5-turbo',
#             messages=[{"role":"user","content:":"Who are you"}]    
#             )
# print(response)




import openai


openai.api_key = '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'

# list models
# models = openai.Model.list()

# print the first model's id
# print(models.data[0].id)
def opppen(contents):
   contents="I want you to act as an AI assisted doctor. I will provide you with details of a patient, and your task is to use the details provided in a medical report and tell what precautions should I take as bullet points"+ contents + ""
   completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": contents}])
   return completion.choices[0].message.content
   



    