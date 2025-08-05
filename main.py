# Vamos a importar NLTK. nos va a ayudar a trabajar con lenguaje natural
import nltk
nltk.download('punkt_tab')

# Definiir la ruta donde se almacenarán los datos descargados
nltk.data.path.append(r'C:\\Users\\osdar\\AppData\\Roaming\\nltk_data')

# descargar el paquete stopwords
nltk.download('stopwords')

# importar funcion para dividir texto en palabras
from nltk.tokenize import word_tokenize

# importar lista vacia de stopwords en español
from nltk.corpus import stopwords

# importar herramienta que calcula frencuencia de palabras en texto
from nltk.probability import FreqDist

# Definimos texto en español a analizar 

texto =""" Soy Daniel Rueda, de la ciudad de Bucaramanga,Colombia. Soy ingeniero Químico, Me gusta trabajar en a salud mental, física y emocional 
para lograr el equilibrio.
Mis compañeros de grupo son Esmeralda, Gustavo, Diego y Juan Carlos, los cuales son personas muy comprometidas y respetuosas y hemos hecho buen equipo.
"""
# tokenización: convertir texto en palabras
palabras = word_tokenize(texto, language='spanish')

# mostramos lista palabras obtenidas
print(palabras)

# Obtener lista de palabras vacias 
stops = set(stopwords.words('spanish'))

# Filtrar palabras ( eliminar stopwords y signos de puntuación)
palabras_filtradas = [palabras for palabras in palabras if palabras.lower() not in stops and palabras.isalpha()] 
print(palabras_filtradas)

# calcular frencuencia de cada palabra filtrada
frecuency = FreqDist(palabras_filtradas)
print(frecuency.most_common(10))