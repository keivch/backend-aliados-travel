class SortService:

    @staticmethod
    def merge_sort(numbers):

        #caso base: lista con 0 o 1 elementos
        if len(numbers) <= 1:
            return numbers

        #dividir la lista en dos
        middle = len(numbers) // 2

        left = numbers[:middle]
        right = numbers[middle:]

        # ordenar recursivamente cada mitad
        left = SortService.merge_sort(left)
        right = SortService.merge_sort(right)

        # combinar las dos mitades ordenadas
        return SortService.merge(left, right)

    @staticmethod
    def merge(left, right):

        result = []

        i = 0
        j = 0

        # se comparan los elementos de ambas listas
        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # se agregan los elementos restantes

        result.extend(left[i:])
        result.extend(right[j:])

        return result