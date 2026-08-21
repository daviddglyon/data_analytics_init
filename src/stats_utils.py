import pandas as pd
df = pd.read_csv("data/sales.csv")


def analyser_ventes(transactions):

    nombre_total_transactions_valides  = len(transactions)

    somme_total_ventes = transactions["montant"].sum()

    mediane = transactions["montant"].median() # ▪ Médiane (valeur centrale une fois la liste triée).

    # ▪ Écart-type (mesure de la dispersion des ventes autour de la moyenne).
    ecart = transactions["montant"].std() 

    # ▪ Valeur maximale et minimale (max(), min()).
    val_max = transactions["montant"].max() 
    val_min = transactions["montant"].min() 


    print(f"Nombre total de transactions valides: { nombre_total_transactions_valides }", sep="\n")
    print(f"Somme totale des ventes (sum()):      { somme_total_ventes }", sep="\n")
    print(f"Moyenne (Somme / Nombre): { int(somme_total_ventes) / int(nombre_total_transactions_valides) }", sep="\n")
    print(f"Médiane (valeur centrale une fois la liste triée): { mediane }", sep="\n")
    print(f"Écart-type (mesure de la dispersion des ventes autour de la moyenne): { round(ecart,2) }", sep="\n")
    print(f"Valeur maximale et minimale (max(), min())s: { val_max } et { val_min }", sep="\n")
    print("\n\n")


    

# analyser_ventes(df)
analyser_ventes(df)





