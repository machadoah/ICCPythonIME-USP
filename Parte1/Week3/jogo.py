tempoDeJogo = int(input("Quanto tempo temos já jogado? "))

placarMeuTime = bool(input("Meu time esta ganhando? "))

if ((tempoDeJogo <= 90 ) and (placarMeuTime == True)):
    print("É recuar a bola e trancar a zaga, temos a vantagem!")
    print("É CAMPEÃOOO! 🎶")

elif((tempoDeJogo > 90 ) and (placarMeuTime == True)):
    print("Apita logo juiz!")
    print("Agora é só bicuda para frente!")

elif((tempoDeJogo > 90 ) and (placarMeuTime != True)):
    print("Vamo para cima!")
    print("Apita não juiz!")
    
#elif((tempoDeJogo <= 90 ) and (placarMeuTime != True)):
else:
    print("É ir para cima tentar a virada! Temos tempo aida!")
    