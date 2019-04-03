from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from database_setup import *

engine = create_engine("sqlite:///shoeland.db")

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# session.query(Owner).delete()

# session.query(Category).delete()

# session.query(Item_Details).delete()

# Create Owner
owner1 = Owner(owner_name="saiteja",
               owner_email="saitej9705@gmail.com",
               owner_picture="https://lh3.googleusercontent.com/-HBG4P1kjzDY/"
               "XFqmGLcwyyI/AAAAAAAAAjo/23mx7zNnop8fb8ZYPEhESncXe3N2Nwl_wCEwY"
               "BhgL/w139-h140-p/PROFILE%2BPIC.jpg")
session.add(owner1)
session.commit()
print("Done..!")

# Create Categories

category1 = Category(name="NIKE", owner_id=1)
session.add(category1)
session.commit()

category2 = Category(name="PUMA", owner_id=1)
session.add(category2)
session.commit()

category3 = Category(name="REEBOK", owner_id=1)
session.add(category3)
session.commit()


# Item_Details
product1 = Item_Details(brandname="NIKE",
                        model="1 pegasus 33",
                        image="https://n3.sdlcdn.com/imgs/h/s/4/Nike-1-"
                        "pegasus-33-Blue-SDL676548167-1-98ebf.jpeg",
                        color="blue",
                        price="3000",
                        description="NIKE sports shoe"
                        "best shoe for your sports",
                        category_id="1",
                        ownerid=1)
session.add(product1)
session.commit()

product2 = Item_Details(brandname="PUMA",
                        model="RANGER",
                        image="https://encrypted-tbn0.gstatic.com/images?"
                        "q=tbn:ANd9GcQgYvw7sNPcJq-cSgGBX9f3WP6opMV35"
                        "-3_uFFmdcepuLfYePEJ",
                        color="green",
                        price="3000",
                        description="PUMA sports shoe"
                        "best shoe for your sports",
                        category_id="2",
                        ownerid=1)
session.add(product2)
session.commit()

product3 = Item_Details(brandname="REEBOK",
                        model="CLOUD MODA",
                        image="https://shop.r10s.jp/cloudmoda/cabinet/reebok/"
                              "v67424_01.jpg",
                        color="orange",
                        price="3000",
                        description="REEBOK sports shoe"
                        "best shoe for your sports",
                        category_id="3",
                        ownerid=1)
session.add(product3)
session.commit()

print("Brands are Added..!")
