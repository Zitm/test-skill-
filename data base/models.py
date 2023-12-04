from sqlalchemy import Table, Column,Integer,Boolean,String,MetaData

metadata_obj=MetaData()

workers_table = Table(
    "test",
    metadata_obj,
    Column("id",Integer, primary_key=True),
    Column("Число",Integer, ),
    Column("Простое",Boolean),
    Column("Вхождений",Integer),
    Column("Делители",String),
)
