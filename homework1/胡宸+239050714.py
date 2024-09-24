def c_f(celsius):
    return (celsius * 9/5) + 32

def f_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def m_f(meter):
      return meter * 3.28084

def f_m(foot):
      return foot / 3.28084
  
data = input("请输入需要转换的数据:")
if data[-1] == 'C':
    celsius = float(data[0:len(data-1)])
    fahrenheit = c_f(celsius)
    print(str(fahrenheit)+'F')
elif data[-1] == 'F'
  choice = int(input("温度 or 长度？(输入1或2)"))
  if choice == 1:
      fahrenheit = float(data[0:len(data-1)])
      celsius = f_c(fahrenheit)
      print(str(celsius)+'C')
  elif choice == 2:
      foot = float(data[0:len(data-1)])
      meter = f_m(foot)
      print(str(meter)+'M')
elif data[-1] == 'M'
    meter = float(data[0:len(data-1)])
    foot = m_f(meter)
    print(str(foot)+'F')
    
