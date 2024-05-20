! pip install langchain
! pip install langchain-openai



import os
os.environ["OPENAI_API_KEY"] = "YOUR KEY"

from langchain_openai import OpenAI

llm = OpenAI()

llm.invoke(
    "La capital de la comunidad autonoma de Andalucia es ?"
)

! pip install  langchain_experimental

#! pip install  dotenv



from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
#from dotenv import load_dotenv

from google.colab import drive
drive.mount('/content/drive')

csv_file = "/content/drive/MyDrive/rag/Mapa_del_Comer__Catal_.csv"

agent = create_csv_agent(
    OpenAI(temperature=0),
    csv_file,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

agent.run("Cuantas filas tiene el fichero?")

agent.run("Que ciudad tiene los activos mas grandes?")

agent.run("Dime las 3 ciudades que tiene los activos mas grandes?")

agent.run("Dime el porcentaje de los activos totales que tiene la ciudad de Barcelona?")

agent.run("Dime el porcentaje de los activos totales que tiene la ciudad de Terrassa?")

agent.run("Dime las ciudades que son del Maresme?")

agent.run("Dime el porcentaje de los activos totales que tiene la ciudad de Badalona?")
