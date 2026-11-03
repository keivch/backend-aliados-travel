import codecs

class UppercaseService:

    @staticmethod
    def     count_uppercase(file):

        count = 0

        # Decodificar en utf-8
        # que se pueda dividir en bloques

        decoder = codecs.getincrementaldecoder('utf-8')()

        while True:
            chunk = file.read(64 * 1024) # 64kb
            if not chunk:
                break

            text = decoder.decode(chunk)

            count += sum(1 for char in text if char.isupper())

        # procesar el resto
        remaining = decoder.decode(b'', final=True)

        count += sum(1 for char in remaining if char.isupper())

        return count