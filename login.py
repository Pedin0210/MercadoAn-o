from classPerson import User
import re
#importa o modulo RE
users = []
employees = []


def cpf_validation(cpf):
    # Remove caracteres não numéricos
    cpf = re.sub(r"[^0-9]", "", cpf)
    
    # Checa se o CPF tem exatamente 11 dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    # Elimina CPFs inválidos conhecidos (ex.: 111.111.111-11)
    if cpf == cpf[0] * 11:
        return False

    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    # Verifica se os dígitos verificadores estão corretos
    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])
   
def email_validation(email):
    email_standard = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_standard, email) is not None
#checa se o email entra em um padrão de formataçao

def password_validation(password):
    if len(password) < 8:
        return False
    password_standard = r"^[0-9]{8,8}"
    return re.match(password_standard, password) is not None
#checa se o id entra em um padrão de formataçao

def registration_id_validation(registration_id):
    registration_id_standard = r"^\d{6,8}$"
    return re.match(registration_id_standard, registration_id) is not None
#checa se a matricula entra em um padrão de formataçao