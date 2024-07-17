# https://how.wtf/how-to-use-csv-files-in-vector-stores-with-langchain.html

#from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import CSVLoader


#from langchain.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import OllamaEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

from langchain.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

#embedding_function = OpenAIEmbeddings()
#embedding_function = OllamaEmbeddings(model="llama3")
#embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
embedding_function = HuggingFaceEmbeddings(model_name="multi-qa-mpnet-base-cos-v1")


print("load CSV...")
loader = CSVLoader("./codes-postaux.csv",
    csv_args={
    'delimiter': ';',
    'quotechar': '"',
    'fieldnames': ["insee_code","commune_name","postal_code","delivery_label","line_5"]
})
documents = loader.load()

print(documents[0].page_content[:1000])
print(documents[0].metadata)

print("create db...")
db = Chroma.from_documents(documents, embedding_function)
retriever = db.as_retriever()

print("search")
query = "Do you know Loray?"
docs = db.similarity_search(query)
print(docs)


template = """Answer the question using the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

#model = ChatOpenAI()
model = ChatOllama(model="llama3", temperature=1.0)

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

#print("retriever.invoke :")
#print(retriever.invoke("Do you know Loray (25390)?"))

print("")
print("#### PARIS #####")
print("")
print(chain.invoke("Do you informations about PARIS (75020)?"))

print("")
print("#### BESANCON #####")
print("")
print(chain.invoke("BESANCON"))

print("")
print("#### LORAY #####")
print("")
print(chain.invoke("Can you find the INSEE code of LORAY (25390)?"))

print("")
print("#### PONTARLIER #####")
print("")
print(chain.invoke("Can you find the INSEE code of PONTARLIER?"))
