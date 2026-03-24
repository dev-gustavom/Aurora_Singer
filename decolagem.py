temperatura_interna = int(input("Temperatura interna: "))
temperatura_externa = int(input("Temperatura externa: "))
integridade_estrutural = bool(int(input("Integridade estrutural (1=OK,0=Falha): ")))
nivel_energia = int(input("Nível de energia (%): "))
pressao_tanques = int(input("Pressão dos tanques: "))
status_modulos_criticos = bool(int(input("Status módulos críticos (1=OK,0=Falha): ")))

if temperatura_interna < 18 or temperatura_interna > 27:
    print("DECOLAGEM ABORTADA")

elif temperatura_externa < 40 or temperatura_externa > 50:
    print("DECOLAGEM ABORTADA")

elif not integridade_estrutural:
    print("DECOLAGEM ABORTADA")

elif nivel_energia < 85:
    print("DECOLAGEM ABORTADA")

elif pressao_tanques < 90 or pressao_tanques > 110:
    print("DECOLAGEM ABORTADA")

elif not status_modulos_criticos:
    print("DECOLAGEM ABORTADA")

else:
    print("PRONTO PARA DECOLAR")