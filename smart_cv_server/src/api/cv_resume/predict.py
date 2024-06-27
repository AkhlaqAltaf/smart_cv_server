
import warnings
warnings.filterwarnings("ignore")

# LlamaCpp is used to load GGUF models
from langchain.llms import LlamaCpp
# langchain imports used
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])


callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])


def gen():

    # gemma-1.1-2b-it (GGUF format) from Kaggle Models
    llm = LlamaCpp(
        model_path=r"/model/input/gemma/gguf/1.1-2b-it/1/gemma-1.1-2b-it.gguf",
        temperature=0.3,
        max_tokens=2000,
        top_p=1,
        callback_manager=callback_manager,
        verbose=False,
    )




    # Using PromptTemplate of LangChain
    question = PromptTemplate.from_template(template= "You are a highly talented data scientist who has shown exceptional performance in data-science Kaggle competitions, explain and teach me concepts from Kaggle competition solution write-ups that solved this competition:{competition_title}")

    # The chain (using LangChain Expression Language (LCEL)), but you can try the traditional method of LangChain
    chain = question | llm

    # I used the competition :"Google - American Sign Language Fingerspelling Recognition". Obviously, you can try any other competition.

    chain.invoke({"competition_title": "Google - American Sign Language Fingerspelling Recognition"})