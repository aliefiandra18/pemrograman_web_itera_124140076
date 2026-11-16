"""Latihan 3 - Inheritance: super(), overriding, multiple inheritance, dan MRO."""


class Hewan:
    """Superclass untuk semua hewan."""

    def __init__(self, nama: str, umur: int):
        self.nama = nama
        self.umur = umur

    def suara(self) -> str:
        """Suara umum hewan (akan di-override oleh subclass)."""
        return "..."

    def info(self) -> str:
        """Informasi dasar hewan."""
        return f"{self.nama} ({self.umur} tahun)"


class Kucing(Hewan):
    """Kucing adalah sebuah Hewan."""

    def __init__(self, nama: str, umur: int, warna_bulu: str):
        super().__init__(nama, umur)
        self.warna_bulu = warna_bulu

    def suara(self) -> str:
        return "Meong"

    def info(self) -> str:
        return f"{super().info()} - kucing berbulu {self.warna_bulu}"


class Anjing(Hewan):
    """Anjing adalah sebuah Hewan."""

    def __init__(self, nama: str, umur: int, ras: str):
        super().__init__(nama, umur)
        self.ras = ras

    def suara(self) -> str:
        return "Guk guk"

    def info(self) -> str:
        return f"{super().info()} - anjing ras {self.ras}"

    def ambil_bola(self) -> str:
        """Perilaku khusus Anjing."""
        return f"{self.nama} mengambil bola!"


class KemampuanBerenang:
    """Mixin: menambahkan kemampuan berenang ke class lain."""

    def berenang(self) -> str:
        return f"{self.nama} berenang di kolam"


class Bebek(Hewan, KemampuanBerenang):
    """Multiple inheritance: Bebek adalah Hewan dan bisa berenang."""

    def suara(self) -> str:
        return "Kwek kwek"


if __name__ == "__main__":
    kucing = Kucing("Mimi", 3, "oranye")
    anjing = Anjing("Bobi", 5, "Golden Retriever")
    bebek = Bebek("Donal", 2)

    print("=== Info (method overriding + super) ===")
    for hewan in (kucing, anjing, bebek):
        print(hewan.info(), "| suara:", hewan.suara())

    print("\n=== Perilaku khusus subclass ===")
    print(anjing.ambil_bola())
    print(bebek.berenang())

    print("\n=== isinstance & issubclass ===")
    print("isinstance(kucing, Hewan)  :", isinstance(kucing, Hewan))
    print("isinstance(kucing, Anjing) :", isinstance(kucing, Anjing))
    print("issubclass(Bebek, Hewan)   :", issubclass(Bebek, Hewan))
    print("issubclass(Anjing, Kucing) :", issubclass(Anjing, Kucing))

    print("\n=== MRO Bebek ===")
    print([kelas.__name__ for kelas in Bebek.__mro__])
