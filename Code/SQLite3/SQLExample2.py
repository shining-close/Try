# 导入sqlite3库，使Python可以使用SQLite3相关功能
import sqlite3

# 连接到company.db数据库（若不存在则创建），并使用上下文管理器管理连接
with sqlite3.connect("company.db") as db:
    # 创建游标对象，用于执行SQL语句和获取结果
    cursor = db.cursor()

# 执行SQL语句，创建students表（若不存在），包含id、name、class、grade字段，
# id为主键且为整数类型，name、class为非空文本类型，grade为整数类型
cursor.execute("""CREATE TABLE IF NOT EXISTS students(
    id integer PRIMARY KEY,
    name text NOT NULL,
    class text NOT NULL,
    grade integer);""")



# 执行查询并遍历打印students表中所有数据，每条记录单独一行
cursor.execute("SELECT * FROM students") 
for x in cursor.fetchall():
  print(x)

# 执行查询并遍历打印students表中所有数据（按name排序），每条记录单独一行
cursor.execute("SELECT * FROM students ORDER By name") 
for x in cursor.fetchall():
  print(x)

# 查询students表中grade大于50的所有数据
cursor.execute("SELECT * FROM students WHERE grade>50")

# 查询students表中class为'Python'的所有数据
cursor.execute("SELECT * FROM students WHERE class = 'Python'")

# 多表关联查询：从students和class表中查询grade大于70的学生id、name以及对应的lecturer
cursor.execute("""SELECT students.id, students.name, students.lecturer
FROM students, class WHERE students.class=class.class
AND students.grade > 70""")

# 查询students表中的id、name和grade字段
cursor.execute("SELECT id, name, grade FROM students")

# 执行查询并打印students表中所有数据，每条记录单独一行
cursor.execute("SELECT * FROM students") 
for x in cursor.fetchall():
  print(x)

# 执行查询并打印students表中所有数据（按name排序），每条记录单独一行
cursor.execute("SELECT * FROM students ORDER By name") 
for x in cursor.fetchall():
  print(x)

# 查询students表中grade大于50的所有数据
cursor.execute("SELECT * FROM students WHERE grade>50")

# 查询students表中class为'Python'的所有数据
cursor.execute("SELECT * FROM students WHERE class = 'Python'")

# 多表关联查询：从students和class表中查询grade大于70的学生id、name以及对应的lecturer
cursor.execute("""SELECT students.id, students.name, students.lecturer
FROM students, class WHERE students.class=class.class
AND students.grade > 70""")

# 查询students表中的id、name和grade字段
cursor.execute("SELECT id, name, grade FROM students")


# 从用户输入获取班级名称
whichClass = input("Enter a class: ")
# 查询employees表中指定班级的所有记录（使用参数化查询防止SQL注入）
cursor.execute("SELECT * FROM employees WHERE class=?", [whichClass])
# 遍历并打印查询结果
for x in cursor.fetchall():
  print(x)

# 多表查询：关联students表和class表，查询学生的id、姓名以及对应的讲师信息（通过班级字段关联）
cursor.execute("""SELECT students.id, students.name, class.lecturer
  FROM students,class WHERE students.class= class.class""")

# 更新操作：将students表中id为1的学生姓名改为'Richard'
cursor.execute("UPDATE students SET name = 'Richard' WHERE id =1")
# 提交事务，使更新操作生效（对数据库的写操作需要commit才能保存）
db.commit()

# 删除操作：删除students表中id为1的学生记录（注意原语句缺少FROM关键字，正确应为DELETE FROM students WHERE id=1）
cursor.execute("DELETE students WHERE id=1")