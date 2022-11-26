class IOManager:
    """
    Менеджер работы с образом
    """

    def __init__(self, file_path):
        self._position = 0
        self.file = open(file_path, 'r+b')

    @property
    def position(self) -> int:
        return self._position

    @position.setter
    def position(self, value: int) -> None:
        if value < 0:
            raise ValueError("Incorrect file position set")
        self._position = value

    def __del__(self):
        self.file.close()

    def close(self) -> None:
        """
        Корректное закрытие файла
        """
        self.file.close()

    def read(self, count: int) -> bytes:
        if count <= 0:
            raise ValueError('Count must be a natural number')

        result = self.file.read(count)
        self.position += count
        return result

    def read_int(self, count: int, endian='little') -> int:
        """
        Считывает следующие count байт в файле
        :param endian:
        :param count: Число байт, которые необходимо считать
        :return: bytes, считанные из файла
        """
        result = self.read(count)
        return int.from_bytes(result, endian)

    def rollback(self, count: int) -> None:
        """
        Возвращает указатель в файле на count_of_bytes байт назад
        :param count: число байт, на которые требуется вернуть указатель в файле
        """
        if count <= 0:
            raise ValueError('Count must be a natural number')

        self.position -= count
        self.file.seek(self.position)

    def seek(self, position: int) -> None:
        """
        Смещение в файле на позицию, относительно начала файла
        :param position: позция, относительно начала файла
        :return: None
        """
        self.position = position
        self.file.seek(position)

    def write_int(self, value: int, length: int) -> None:
        """
        Запись интового значения на образ в current_position
        :param value: записываемое значение
        :param length: длинна записываемого значения
        :return: None
        """
        self.position += length
        self.file.write(int.to_bytes(value, length, 'little'))

    def write_bytes(self, value: bytes) -> None:
        """
        Записывает некоторое количество байт на образ в current_position
        :param value: записываемые байты
        :return: None
        """
        self.position += len(value)
        self.file.write(value)
