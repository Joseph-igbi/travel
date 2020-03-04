
from application import db
from application.models import City
import pandas as pd



db.drop_all()
db.create_all()

if len(City.query.all())<1:
    data = pd.read_excel('./data2.xlsx')
    data.columns=['city','country']
    for index, row in data.iterrows():
        city= City(city_name=row[0], country=row[1])
        db.session.add(city)
    db.session.commit()
