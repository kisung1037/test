class House:
  def __init__(self, location, house_type, deal_type, price, completion_year):
    self.location = location
    self.house_type = house_type
    self.deal_type = deal_type
    self.price = price
    self.completon_year = completion_year

  def show_detail(self):
    print("위치: {} , 타입: {}, 매전: {}, 가격: {}, 완공일: {}".format(self.location,\
      self.house_type, self.deal_type, self.price, self.completon_year))


apart1 = House("강남", "아파트", "매매", "10억", "2010년")
op1 = House("마포", "오피스텔","전세","5억","2007년")
vila1 = House("송파","빌라","월세","500/50","2000년")

houses = []

houses.append(apart1)
houses.append(op1)
houses.append(vila1)

print(" 총 {} 대의 매물이 있습니다.".format(len(houses)))
for house in houses:
  house.show_detail()