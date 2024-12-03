import re
import validators
import tldextract

# Lista de palavras-chave suspeitas
suspect_keywords = ["promoção", "grátis", "oferta", "desconto", "urgente"]

# Lista de domínios menos confiáveis
suspect_domains = [".xyz", ".info", ".top", ".click", ".online"]

def is_suspicious_url(url):
    if not validators.url(url):  # Valida a URL
        return "A URL fornecida não é válida."

    # Extrai partes da URL
    extracted = tldextract.extract(url)
    domain = extracted.domain
    suffix = f".{extracted.suffix}"

    # Verifica se o domínio contém caracteres suspeitos
    if re.search(r"[0-9]{2,}|[!@#$%^&*()_+=]", domain):
        return "A URL pode ser suspeita: domínio estranho detectado."

    # Verifica o uso de domínios menos confiáveis
    if suffix in suspect_domains:
        return "A URL pode ser suspeita: domínio incomum."

    # Verifica palavras-chave suspeitas
    for keyword in suspect_keywords:
        if keyword in url.lower():
            return f"A URL pode ser suspeita: palavra-chave '{keyword}' encontrada."

    return "A URL parece segura."



import streamlit as st

st.title("Este site é seguro?")
st.write ("")
st.text("Analise um URL que você deseja visitar para detectar malwares, sites falsos e ataques de phishing.")

#espaçamento

st.write ("")

url = st.text_input("Digite a URL que deseja verificar: ")

if url:
    resultado = is_suspicious_url(url)
    st.write(resultado)

#Espaçamento
st.write ("")
st.write ("")
st.write ("")
st.write ("")
st.write ("")
st.write ("")
st.write ("")
st.write ("")
st.write ("")
st.write ("")


st.title("O que é um verificador de link?")
st.text("O Verificador de Links é uma ferramenta de verificação de URL projetada para ajudar você a evitar malwares e sites falsos. ")

#espaçamento
st.write ("")
st.write ("")

#layout em 2 colunas
col_image, col_text = st.columns([1,2])

#adicionando image,
with col_image:
    st.image("https://www.ufsm.br/app/uploads/sites/601/2021/07/capa-1024x668.jpg", caption=(""), use_container_width=True)

with col_text:
    col_text1, col_text2 = st.columns(2)

    with col_text1:
        st.header("Evite sites maliciosos")
        st.text("Recebeu um email ou uma promoção duvidosa? verifique o link antes de acessar; isso reduzirá muito as chances de você cair num golpe ou qualquer outro ataque!")

    with col_text2:
        st.header("bloquie imediato")
        st.text("Alguns sites estão repletos de malwares que aguardam para serem baixados e executados no seu dispositivo. Bloqueie eles e denuncie imediatamente para a polícia federal para ajudar nesse causa contra sites mal intecionados")

