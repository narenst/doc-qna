from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

def get_prompt():
    prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. 

{context}

Question: {question}
Answer:"""
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    return prompt
    

class AI:

    context = ""
    llm = None
    chain = None

    def __init__(self, context=None):
        if context is not None:
            self.context = context
        self.llm = OpenAI(temperature=0.1)
        self.chain = LLMChain(llm=self.llm, prompt=get_prompt())
        
    
    def process_messages(self, messages):
        response = self.chain.run(context=self.context, question=messages)
        return response