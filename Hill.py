import numpy

def create_matrix_from(key):
    m=[[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            m[i][j] = ord(key[3*i+j]) % 65
    return m

def create_matrix():
    m=[[17, 17, 5], [21, 18, 21], [2, 2, 19]]
    return m

def encrypt(P, K):
    C=[0,0,0]
    C[0] = (K[0][0]*P[0] + K[0][1]*P[1] + K[0][2]*P[2]) % 26
    C[1] = (K[1][0]*P[0] + K[1][1]*P[1] + K[1][2]*P[2]) % 26
    C[2] = (K[2][0]*P[0] + K[2][1]*P[1] + K[2][2]*P[2]) % 26
    return C

def Hill(message, K):
    cipher_text = []
    for i in range(int(len(message) / 3)):
        P=[0, 0, 0]
        for j in range(3):
            P[j] = ord(message[j]) % 65
        message = message[3:]
        #Encript three letters
        C = encrypt(P,K)
        for j in range(3):
            cipher_text.append(chr(C[j] + 65))
    return "".join(cipher_text)

def MatrixInverse(K):
    det_ = int(numpy.linalg.det(K))
    det_multiplicative_inverse = pow(det_, -1, 26)
    K_inv = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            Dji = K
            Dji = numpy.delete(Dji, (j), axis=0)
            Dji = numpy.delete(Dji, (i), axis=1)
            det = Dji[0][0]*Dji[1][1] - Dji[0][1]*Dji[1][0]
            K_inv[i][j] = (det_multiplicative_inverse * pow(-1,i+j) * det) % 26
    return K_inv

if __name__ == "__main__":
    
    message = "MYSECRETMESSAGE"
    key = "RRFVSVACT"

    K = create_matrix_from(key)
    print(K)
    # C = P * K mod 26
    cipher_text = Hill(message, K)
    print ('Cipher text: ', cipher_text)
    
    # P = C * K^-1 mod 26
    K_inv = MatrixInverse(K)            
    plain_text = Hill(cipher_text, K_inv)
    print ('Plain text: ', plain_text)

    