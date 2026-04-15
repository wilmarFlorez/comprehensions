# ============================================================
#  DATACLASSES — Clases de datos sin boilerplate
#  Python genera __init__, __repr__, __eq__ automáticamente.
# ============================================================
from dataclasses import dataclass, field


@dataclass
class User:
    name: str
    email: str
    role: str = "viewer"  # valor por defecto

    @property
    def is_admin(self):
        return self.role == "admin"


alice = User("Alice", "alice@dev.com", "admin")
bob = User("Bob", "bob@dev.com")

print(alice)           # User(name='Alice', email='alice@dev.com', role='admin')
print(alice.is_admin)  # True
print(bob.is_admin)    # False
print(alice == User("Alice", "alice@dev.com", "admin"))  # True


# Dataclass con campo computado y lista mutable
@dataclass
class Team:
    name: str
    members: list[User] = field(default_factory=list)

    def add(self, user: User):
        self.members.append(user)

    @property
    def size(self):
        return len(self.members)

    def admins(self):
        return [u for u in self.members if u.is_admin]


team = Team("Backend")
team.add(alice)
team.add(bob)
print(f"\n{team.name}: {team.size} miembros, {len(team.admins())} admin(s)")
