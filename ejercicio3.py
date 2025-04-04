salario= int(input("Introduce el salario: "))
impuesto_renta= salario*0.10
seguro_social= salario*0.05 
fond_pension= salario*0.03
r= impuesto_renta+seguro_social+fond_pension
r-salario
print("el salario bruto es: ", salario)
print("las deducciones son: ", r)
print("el salario neto es: ", salario-r)