import re

texto = ("The Python Software Foundation and the global Python community welcome and encourage "
         "participation by everyone. Our community is based on mutual respect, tolerance, and "
         "encouragement, and we are working to help each other live up to these principles. We want "
         "our community to be more diverse: whoever you are, and whatever your background, we welcome you.")

texto_limpo = re.sub(r'[^\w\s]', '', texto).lower()

palavras = texto_limpo.split()

letras_python = set("python")

palavras_filtradas = [palavra for palavra in palavras 
                      if palavra[0] in letras_python or palavra[-1] in letras_python]

print(palavras_filtradas)
