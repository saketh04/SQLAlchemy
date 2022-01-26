#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlalchemy as db


# In[8]:


from sqlalchemy import create_engine, MetaData,Column, Table, Integer, String
engine = db.create_engine('sqlite:///employ.db',echo=True)
meta = MetaData()


# In[11]:


employ=Table('employ',meta,
              Column('Id',Integer,primary_key=True),
              Column('Name',String),
              Column('Department',String),
              Column('Basicsalary',Integer),
              Column('DA',Integer),
              Column('HRA',Integer),
)
meta.create_all(engine)


# In[12]:


conn=engine.connect()
conn.execute(employ.insert(),[
    {'Name':'Saketh','Department':'ECE','Basicsalary':'27000','DA':'1500','HRA':'50000'},
    {'Name':'Jahnavi','Department':'ECE','Basicsalary':'70000','DA':'5500','HRA':'70000'},
    {'Name':'Koundinya','Department':'Civil','Basicsalary':'20000','DA':'1500','HRA':'20000'},
    {'Name':'Subash','Department':'Civil','Basicsalary':'25000','DA':'1500','HRA':'30000'},
    {'Name':'Vinay','Department':'Civil','Basicsalary':'15000','DA':'1500','HRA':'60000'}
    
])


# In[28]:


res=employ.select().where(employ.c.Name=='Saketh')
op=conn.execute(res)
for i in op:
    print(i)


# In[26]:


res=employ.select().where(employ.c.HRA.in_([50000,70000,30000]))
op=conn.execute(res)
for i in op:
    print(i)


# In[23]:


from sqlalchemy import asc, desc
res=employ.select().order_by(desc(employ.c.Basicsalary))
op=conn.execute(res)
for i in op:
    print(i)


# In[55]:


from sqlalchemy.sql import func

res=db.select([employ.c.Department,func.sum(employ.c.Basicsalary),func.count(employ.c.Name)]).order_by(desc(employ.c.Basicsalary)).group_by(employ.c.Department)
op=conn.execute(res)
for i in op:
    print(i)


# In[63]:


res = db.update(employ).values(Basicsalary = '100000').where(employ.c.Name=="Saketh")
op = conn.execute(res)


# In[64]:


res=employ.select().where(employ.c.Name=='Saketh')
op=conn.execute(res)
for i in op:
    print(i)


# In[ ]:




