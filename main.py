# Vamos a importar NLTK. nos va a ayudar a trabajar con lenguaje natural
import nltk
nltk.download('punkt_tab')

# Definiir la ruta donde se almacenarán los datos descargados
nltk.data.path.append('C:\\Users\\osdar\\AppData\\Roaming\\nltk_data')

# descargar el paquete stopwords
nltk.download('stopwords')

# importar funcion para dividir texto en palabras
from nltk.tokenize import word_tokenize

# importar lista vacia de stopwords en español
from nltk.corpus import stopwords

# importar herramienta que calcula frencuencia de palabras en texto
from nltk.probability import FreqDist

# Definimos texto en español a analizar 

texto ="""¿Cómo funciona la IA?
Las Inteligencias artificiales utilizan algoritmos y modelos matemáticos para procesar grandes cantidades de datos y tomar decisiones basadas en patrones y reglas establecidas a través del aprendizaje automático, que es la capacidad de una máquina para aprender de forma autónoma a partir de datos sin ser programada específicamente para hacerlo. De esta manera la IA puede mejorar su precisión y eficiencia con el tiempo.
Espero que esta información sobre la IA sea de gran apoyo para su formación y aprendizaje.
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