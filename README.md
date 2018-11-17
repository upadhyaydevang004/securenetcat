# securenetcat
Secure Netcat


The goal is to provide confidentiality and integrity to this simple version of
netcat. The standard way to add confdentiality and integrity to messages is through the use of
cryptography. Encryption functions (e.g., AES) provide confidentiality. MAC functions (HMAC)
provide integrity. As discussed in course lectures, there are different ways to combined encryp-
tion and MAC functions to provide both confidentiality and integrity: encrypt-and-MAC (E&M),
encrypt-then-MAC (EtM), and MAC-then-encrypt (MtE). Out of these methods, E&M is insecure
(sending the MAC of plaintext in the clear leaks information). Both EtM and MtE are used in
a variety of cryptographic protocols, but only EtM reaches the highest definition of security. In
addition to these ways of combining encryption and integrity, there are cipher modes that pro-
vide Authenticated Encryption (AE). These modes security combine encryption and MAC into the
construction itself. The most notable of these modes is Galios Couter Mode (GCM).AES-GCM is used for this process.
