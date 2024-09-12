import re

texto = ("The Python Software Foundation and the global Python community welcome and encourage "
         "participation by everyone. Our community is based on mutual respect, tolerance, and "
         "encouragement, and we are working to help each other live up to these principles. We want "
         "our community to be more diverse: whoever you are, and whatever your background, we welcome you.")

texto_limpo = re.sub(r'[^\w\s]', '', texto).lower()

palavras = texto_limpo.split()

letras_python = set("python")

palavras_filtradas = [palavra for palavra in palavras 
                      if (len(palavra) > 4 and 
                          any(letra in letras_python for letra in palavra))]

quantidade_palavras_filtradas = len(palavras_filtradas)

print(quantidade_palavras_filtradas)
