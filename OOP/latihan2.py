class Human:
    def __init__(self, nama, role, damage):
        self.nama = nama
        self.role = role
        self.damage = damage

    def greetings(self):
        return f"Halo tuan namaku {self.nama} aku memiliki role {self.role} dan memiliki damage {self.damage}"
    
    def atack(self, target):
        # Memastikan target memiliki metode take_damage
        if hasattr(target, "take_damage"):
            target.take_damage(self.damage)


class Monster:
    def __init__(self, nama, health):
        self.nama = nama
        self.health = health
        self.max_health = 10
    
    def take_damage(self, damage_amount):
        self.health -= damage_amount
        if self.health <= 0:
            print(f"{self.nama} mati")


# Contoh penggunaan
rookie = Human(nama="Rookie", role="Beban", damage=10)
mimic = Monster("Mimic", 10)

print(rookie.greetings())
rookie.atack(mimic)  # Tidak perlu mengirim argumen kedua
