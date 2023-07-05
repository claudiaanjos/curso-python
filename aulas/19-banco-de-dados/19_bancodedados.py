# -*- coding: utf-8 -*-
"""19_BancodeDados.ipynb

Prof. Fernando Amaral

www.eia.ai

# Banco de dados
"""

import psycopg2
con = psycopg2.connect(host='database-1.cuf8rlopzxtf.us-east-1.rds.amazonaws.com', database='postgres',
                       user='postgres', password='12345678')
cur = con.cursor()
con.close()

import psycopg2
con = psycopg2.connect(host='database-1.cuf8rlopzxtf.us-east-1.rds.amazonaws.com', database='postgres',
                       user='postgres', password='12345678')
con.autocommit = True
cur = con.cursor()
cur.execute('create database inventario;')
con.commit()
con.close()

import psycopg2
con = psycopg2.connect(host='database-1.cuf8rlopzxtf.us-east-1.rds.amazonaws.com', database='inventario',
                       user='postgres', password='12345678')
con.autocommit = True
cur = con.cursor()
cur.execute('create table arquivos (idarquivo INT, nomearquivo VARCHAR(256));')
con.commit()
con.close()

import psycopg2
con = psycopg2.connect(host='database-1.cuf8rlopzxtf.us-east-1.rds.amazonaws.com', database='inventario',
                       user='postgres', password='12345678')
con.autocommit = True
cur = con.cursor()
cur.execute("insert into arquivos (idarquivo, nomearquivo) values (123, 'teste.jpg')" )

import psycopg2
con = psycopg2.connect(host='database-1.cuf8rlopzxtf.us-east-1.rds.amazonaws.com', database='inventario',
                       user='postgres', password='12345678')
con.autocommit = True
cur = con.cursor()
cur.execute("select * from arquivos" )
recset = cur.fetchall()
for rec in recset:
  print(rec)
con.close()

import psycopg2
con = psycopg2.connect(host='database-1.cuf8rlopzxtf.us-east-1.rds.amazonaws.com', database='inventario',
                       user='postgres', password='12345678')
con.autocommit = True
cur = con.cursor()
cur.execute("delete from arquivos" )
con.commit()
con.close()

