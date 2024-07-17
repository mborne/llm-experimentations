import bs4
from langchain import hub

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import AsyncHtmlLoader

from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
#from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import OllamaEmbeddings

from langchain_text_splitters import RecursiveCharacterTextSplitter
#from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama



from dotenv import load_dotenv
load_dotenv()

#llm = ChatOpenAI(model="gpt-3.5-turbo")
llm = Ollama(
    model="llama3"
)  # assuming you have Ollama installed and have llama3 model pulled with `ollama pull llama3 `

#loader = WebBaseLoader(["https://mborne.github.io"])
loader = AsyncHtmlLoader([
    "https://mborne.github.io",
    "https://mborne.github.io/cours-devops/annexe/docker/",
    "https://mborne.github.io/cours-devops/annexe/docker/bonnes-pratiques.html"
])
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=OllamaEmbeddings(model="llama3"))

retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print("retriever.invoke :")
print(retriever.invoke("Can you list 10 docker best practices?"))

print("rag_chain.invoke :")
print(rag_chain.invoke("Can you list 10 docker best practices?"))

