class Unit:
  def __init__(self,name,hp):
    self.name = name
    self.hp =hp

class AttactUnit(Unit):
  def __init__(self,name,hp,damage):
    Unit.__init__(self,name,hp)
    self.damage = damage

  def attck(self, location):
    print("{} : {} 방향으로 적군을 공격 합니다.. [공격력 {}"\
      .format(self.name, location, self.damage))

  def damaged(self, damage):
    print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
    self.hp -= damage
    print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
    if self.hp <= 0:
      print("{} : 파괴되었습니다.".format(self.name))

class Flyable:
  def __init__(self, flying_speed):
    self.flying_speed = flying_speed

  def fly(self, name, location):
    print("{} : {} 방향으로 날아갑니다.[속도 {}]"\
      .format(self.name, location, self.flying_speed))

class FlyableAttackUnit(AttactUnit, Flyable):
  def __init__(self, name, hp, damage, flying_speed):
      AttactUnit.__init__(self,name,hp,damage)
      Flyable.__init__(self, flying_speed)
      print("유닛이 생성되었습니다. {}".format(self.name))
  
  def move(self, location):
    print("[공중 유닛 이동]")
    self.fly(self.name, location)

class BuildingUnit(Unit):
  def __init__(self, name, hp):
      super().__init__(name, hp)