# Importar librería NLTK 
import nltk

# desde nltk descargar el paquete stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')

# Crear variable que contenga las stopwords
lista_stopwords = stopwords.words('spanish')
print(lista_stopwords)

