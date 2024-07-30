import socket

def descobrir_meu_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        endereco_ip = s.getsockname()[0]
    except Exception:
        endereco_ip = '127.0.0.1'
    finally:
        s.close()
    return endereco_ip

if __name__ == "__main__":
    meu_ip = descobrir_meu_ip()
    print("O endereço IP do seu dispositivo é:", meu_ip)
