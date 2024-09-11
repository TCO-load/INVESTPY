import random
import os
from colorama import init, Fore, Style
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from datetime import datetime

# Initialiser colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    terminal_width = os.get_terminal_size().columns
    title = "Conseiller d'investissement DCA avancé"
    
    print(Fore.CYAN + Style.BRIGHT + "╔" + "═" * (terminal_width - 2) + "╗")
    print(Fore.CYAN + Style.BRIGHT + "║" + " " * (terminal_width - 2) + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + title.center(terminal_width - 2) + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + " " * (terminal_width - 2) + "║")
    print(Fore.CYAN + Style.BRIGHT + "╚" + "═" * (terminal_width - 2) + "╝")

def print_centered(text):
    terminal_width = os.get_terminal_size().columns
    print(text.center(terminal_width))

def display_help():
    clear_screen()
    print_header()
    print_centered(Fore.GREEN + Style.BRIGHT + "\nGuide d'investissement DCA :")
    help_text = """
    1. Le DCA (Dollar Cost Averaging) est une stratégie d'investissement qui consiste à investir régulièrement 
       une somme fixe, indépendamment des fluctuations du marché.
    2. Cette approche permet de réduire l'impact de la volatilité du marché sur votre portefeuille.
    3. Vous pouvez personnaliser votre profil d'investissement en fonction de votre tolérance au risque.
    4. Le programme simule la performance de votre portefeuille sur plusieurs années, en tenant compte 
       des fluctuations du marché.
    5. Vous pouvez comparer différentes stratégies d'investissement pour prendre des décisions éclairées.
    6. N'oubliez pas de rééquilibrer régulièrement votre portefeuille pour maintenir votre allocation cible.
    """
    print(Fore.WHITE + help_text)
    input(Fore.CYAN + "\nAppuyez sur Entrée pour revenir au menu principal...")

def get_user_choice():
    while True:
        clear_screen()
        print_header()
        print_centered(Fore.YELLOW + "\nQue souhaitez-vous faire ?")
        options = [
            "1. Créer un nouveau profil d'investissement",
            "2. Modifier un profil existant",
            "3. Simuler la performance d'un portefeuille",
            "4. Rééquilibrer un portefeuille existant",
            "5. Comparer différentes stratégies d'investissement",
            "6. Analyser l'historique des performances",
            "7. Afficher le guide d'aide général",
            "8. Quitter le programme"
        ]
        for option in options:
            print_centered(Fore.WHITE + option)
        choice = input(Fore.CYAN + "Votre choix (1-8) : " + Fore.WHITE)
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
            return int(choice)
        else:
            print_centered(Fore.RED + "Choix invalide. Veuillez entrer un nombre entre 1 et 8.")
            input(Fore.CYAN + "Appuyez sur Entrée pour continuer...")

def get_risk_profile():
    while True:
        clear_screen()
        print_header()
        print_centered(Fore.YELLOW + "\nQuel est votre profil de risque ?")
        profiles = [
            "1. Conservateur (faible risque, rendements potentiels plus bas)",
            "2. Modéré (risque moyen, rendements potentiels moyens)",
            "3. Agressif (risque élevé, rendements potentiels plus élevés)"
        ]
        for profile in profiles:
            print_centered(Fore.WHITE + profile)
        choice = input(Fore.CYAN + "Votre choix (1-3) : " + Fore.WHITE)
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print_centered(Fore.RED + "Choix invalide. Veuillez entrer un nombre entre 1 et 3.")
            input(Fore.CYAN + "Appuyez sur Entrée pour continuer...")

def get_investment_amount():
    while True:
        try:
            amount = float(input(Fore.YELLOW + "Quel montant souhaitez-vous investir initialement ? " + Fore.WHITE))
            if amount > 0:
                return amount
            else:
                print_centered(Fore.RED + "Le montant doit être supérieur à 0.")
        except ValueError:
            print_centered(Fore.RED + "Veuillez entrer un nombre valide.")

def suggest_portfolio(risk, amount):
    portfolios = {
        1: {"Obligations": 70, "Actions": 25, "Or": 5},
        2: {"Obligations": 50, "Actions": 40, "Or": 5, "REITs": 5},
        3: {"Actions": 70, "REITs": 15, "Crypto": 10, "Or": 5}
    }
    
    portfolio = portfolios[risk]
    
    print_centered(Fore.GREEN + "\nVoici le portefeuille suggéré basé sur votre profil de risque :")
    for asset, allocation in portfolio.items():
        print_centered(f"{Fore.CYAN}{asset}: {Fore.GREEN}{allocation}% ({amount * allocation / 100:.2f}€)")
    
    return portfolio

def get_initial_investment():
    while True:
        try:
            amount = float(input(Fore.YELLOW + "Quel est votre investissement initial ? " + Fore.WHITE))
            if amount >= 0:
                return amount
            else:
                print_centered(Fore.RED + "Le montant doit être positif ou nul.")
        except ValueError:
            print_centered(Fore.RED + "Veuillez entrer un nombre valide.")

def get_monthly_contribution():
    while True:
        try:
            amount = float(input(Fore.YELLOW + "Quelle sera votre contribution mensuelle ? " + Fore.WHITE))
            if amount >= 0:
                return amount
            else:
                print_centered(Fore.RED + "Le montant doit être positif ou nul.")
        except ValueError:
            print_centered(Fore.RED + "Veuillez entrer un nombre valide.")

def simulate_performance(portfolio, years, initial_investment, monthly_contribution):
    clear_screen()
    print_header()
    print_centered(Fore.YELLOW + f"\nSimulation de performance sur {years} ans :")
    print_centered(Fore.WHITE + f"Investissement initial : {initial_investment}€")
    print_centered(Fore.WHITE + f"Contribution mensuelle : {monthly_contribution}€")

    total_value = initial_investment
    yearly_values = [total_value]
    total_invested = initial_investment
    performance_history = []
    
    for year in range(1, years + 1):
        year_growth = 0
        for asset, allocation in portfolio.items():
            if "obligataires" in asset.lower() or "obligations" in asset.lower():
                growth = random.uniform(0.01, 0.05)
            elif "actions" in asset.lower() or "reits" in asset.lower():
                growth = random.uniform(0.05, 0.12)
            elif "crypto" in asset.lower():
                growth = random.uniform(-0.2, 0.5)
            else:
                growth = random.uniform(0.02, 0.08)
            
            year_growth += (growth * allocation / 100)
        
        total_value *= (1 + year_growth)
        total_value += monthly_contribution * 12
        total_invested += monthly_contribution * 12
        yearly_values.append(total_value)
        
        performance_history.append({
            "Année": year,
            "Valeur du portefeuille": total_value,
            "Croissance": year_growth * 100,
            "Total investi": total_invested,
            "Gain/Perte": total_value - total_invested
        })
        
        print_centered(f"{Fore.WHITE}Année {year}:")
        print_centered(f"  {Fore.GREEN}Valeur du portefeuille: {total_value:.2f}€")
        print_centered(f"  {Fore.YELLOW}Croissance: {year_growth*100:.2f}%")
        print_centered(f"  {Fore.CYAN}Total investi: {total_invested:.2f}€")
        print_centered(f"  {Fore.MAGENTA}Gain/Perte: {total_value - total_invested:.2f}€")
    
    # Créer un graphique
    plt.figure(figsize=(12, 6))
    plt.plot(range(years + 1), yearly_values, label="Valeur du portefeuille")
    plt.plot(range(years + 1), [initial_investment + i * monthly_contribution * 12 for i in range(years + 1)], label="Total investi", linestyle="--")
    plt.title("Évolution de la valeur du portefeuille vs Total investi")
    plt.xlabel("Années")
    plt.ylabel("Valeur (€)")
    plt.legend()
    plt.grid(True)
    
    graph_path = os.path.join(os.getcwd(), "portfolio_performance.png")
    plt.savefig(graph_path)
    print_centered(f"\n{Fore.CYAN}Le graphique de performance a été sauvegardé ici : {graph_path}")

    # Sauvegarder l'historique des performances
    df = pd.DataFrame(performance_history)
    csv_path = os.path.join(os.getcwd(), "performance_history.csv")
    df.to_csv(csv_path, index=False)
    print_centered(f"{Fore.CYAN}L'historique des performances a été sauvegardé ici : {csv_path}")

    input(Fore.CYAN + "\nAppuyez sur Entrée pour revenir au menu principal...")

def rebalance_portfolio(portfolio):
    clear_screen()
    print_header()
    print_centered(Fore.YELLOW + "\nRééquilibrage du portefeuille :")
    
    print_centered(Fore.WHITE + "\nPortefeuille actuel :")
    for asset, allocation in portfolio.items():
        print_centered(f"{Fore.CYAN}{asset}: {Fore.GREEN}{allocation}%")
    
    total_value = float(input(Fore.YELLOW + "\nQuelle est la valeur totale actuelle de votre portefeuille ? " + Fore.WHITE))
    
    new_portfolio = {}
    for asset, target_allocation in portfolio.items():
        current_value = float(input(Fore.YELLOW + f"Quelle est la valeur actuelle de votre investissement en {asset} ? " + Fore.WHITE))
        current_allocation = (current_value / total_value) * 100
        new_portfolio[asset] = current_allocation
        
        adjustment = target_allocation - current_allocation
        if adjustment > 0:
            print_centered(f"{Fore.GREEN}Achetez {abs(adjustment * total_value / 100):.2f}€ de {asset}")
        elif adjustment < 0:
            print_centered(f"{Fore.RED}Vendez {abs(adjustment * total_value / 100):.2f}€ de {asset}")
        else:
            print_centered(f"{Fore.BLUE}Aucun ajustement nécessaire pour {asset}")
    
    input(Fore.CYAN + "\nAppuyez sur Entrée pour revenir au menu principal...")
    return new_portfolio

def display_disclaimer():
    clear_screen()
    print_header()
    print_centered(Fore.RED + Style.BRIGHT + "\nAVERTISSEMENT IMPORTANT")
    disclaimer_text = """
    Ce programme est fourni à titre informatif uniquement et ne constitue pas un conseil financier professionnel.
    Les performances passées ne garantissent pas les résultats futurs. Tous les investissements comportent des risques,
    y compris la perte potentielle du capital investi. Avant de prendre des décisions d'investissement,
    consultez un conseiller financier qualifié pour obtenir des conseils personnalisés adaptés à votre situation.
    """
    print_centered(Fore.WHITE + disclaimer_text)
    input(Fore.CYAN + "\nAppuyez sur Entrée pour continuer...")

def modify_existing_profile(portfolio):
    clear_screen()
    print_header()
    print_centered(Fore.YELLOW + "\nModification du profil d'investissement existant :")
    
    print_centered(Fore.WHITE + "\nPortefeuille actuel :")
    for asset, allocation in portfolio.items():
        print_centered(f"{Fore.CYAN}{asset}: {Fore.GREEN}{allocation}%")
    
    while True:
        asset = input(Fore.YELLOW + "\nQuel actif souhaitez-vous modifier ? (ou 'q' pour quitter) : " + Fore.WHITE)
        if asset.lower() == 'q':
            break
        if asset in portfolio:
            try:
                new_allocation = float(input(Fore.YELLOW + f"Nouvelle allocation pour {asset} (en %) : " + Fore.WHITE))
                if 0 <= new_allocation <= 100:
                    portfolio[asset] = new_allocation
                    print_centered(Fore.GREEN + "Allocation mise à jour.")
                else:
                    print_centered(Fore.RED + "L'allocation doit être entre 0 et 100%.")
            except ValueError:
                print_centered(Fore.RED + "Veuillez entrer un nombre valide.")
        else:
            print_centered(Fore.RED + "Cet actif n'existe pas dans votre portefeuille.")
    
    # Normaliser les allocations
    total = sum(portfolio.values())
    for asset in portfolio:
        portfolio[asset] = (portfolio[asset] / total) * 100

    print_centered(Fore.GREEN + "\nPortefeuille mis à jour :")
    for asset, allocation in portfolio.items():
        print_centered(f"{Fore.CYAN}{asset}: {Fore.GREEN}{allocation:.2f}%")

    input(Fore.CYAN + "\nAppuyez sur Entrée pour revenir au menu principal...")
    return portfolio

def compare_strategies():
    clear_screen()
    print_header()
    print_centered(Fore.YELLOW + "\nComparaison de différentes stratégies d'investissement :")
    
    initial_investment = get_initial_investment()
    monthly_contribution = get_monthly_contribution()
    years = int(input(Fore.YELLOW + "Sur combien d'années voulez-vous comparer les stratégies ? " + Fore.WHITE))

    strategies = {
        "Conservateur": {"Obligations": 70, "Actions": 25, "Or": 5},
        "Équilibré": {"Obligations": 50, "Actions": 40, "Or": 5, "REITs": 5},
        "Agressif": {"Actions": 70, "REITs": 15, "Crypto": 10, "Or": 5}
    }

    results = []
    for strategy_name, allocation in strategies.items():
        total_value = initial_investment
        yearly_values = [total_value]

        for _ in range(years):
            year_growth = 0
            for asset, alloc in allocation.items():
                if "obligations" in asset.lower():
                    growth = random.uniform(0.01, 0.05)
                elif "actions" in asset.lower() or "reits" in asset.lower():
                    growth = random.uniform(0.05, 0.12)
                elif "crypto" in asset.lower():
                    growth = random.uniform(-0.2, 0.5)
                elif "or" in asset.lower():
                    growth = random.uniform(0, 0.07)
                else:
                    growth = random.uniform(0.02, 0.08)
                year_growth += (growth * alloc / 100)
            
            total_value *= (1 + year_growth)
            total_value += monthly_contribution * 12
            yearly_values.append(total_value)

        results.append({
            "Stratégie": strategy_name,
            "Valeur finale": total_value,
            "Rendement total": (total_value - initial_investment) / initial_investment * 100
        })

    df_results = pd.DataFrame(results)
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x="Stratégie", y="Rendement total", data=df_results)
    plt.title("Comparaison des rendements totaux par stratégie")
    plt.ylabel("Rendement total (%)")
    plt.xticks(rotation=45)
    
    graph_path = os.path.join(os.getcwd(), "strategy_comparison.png")
    plt.savefig(graph_path)
    print_centered(f"\n{Fore.CYAN}Le graphique de comparaison a été sauvegardé ici : {graph_path}")

    print_centered(Fore.WHITE + "\nRésultats de la comparaison :")
    for _, row in df_results.iterrows():
        print_centered(f"{Fore.CYAN}{row['Stratégie']}: {Fore.GREEN}Valeur finale {row['Valeur finale']:.2f}€, {Fore.YELLOW}Rendement total {row['Rendement total']:.2f}%")

    input(Fore.CYAN + "\nAppuyez sur Entrée pour revenir au menu principal...")

def analyze_performance_history():
    clear_screen()
    print_header()
    print_centered(Fore.YELLOW + "\nAnalyse de l'historique des performances :")

    csv_path = os.path.join(os.getcwd(), "performance_history.csv")
    if not os.path.exists(csv_path):
        print_centered(Fore.RED + "Aucun historique de performance n'a été trouvé. Veuillez d'abord simuler la performance d'un portefeuille.")
        input(Fore.CYAN + "\nAppuyez sur Entrée pour revenir au menu principal...")
        return

    df = pd.read_csv(csv_path)
    
    print_centered(Fore.WHITE + "\nRésumé statistique :")
    print(df.describe().to_string())

    print_centered(Fore.WHITE + "\nAnalyse de la croissance annuelle :")
    annual_growth = df["Croissance"].mean()
    print_centered(f"Croissance annuelle moyenne : {annual_growth:.2f}%")

    print_centered(Fore.WHITE + "\nAnalyse des gains/pertes :")
    total_gain_loss = df["Gain/Perte"].iloc[-1]
    print_centered(f"Gain/Perte total : {total_gain_loss:.2f}€")

    # Créer un graphique de l'évolution de la valeur du portefeuille
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="Année", y="Valeur du portefeuille", data=df)
    plt.title("Évolution de la valeur du portefeuille")
    plt.xlabel("Année")
    plt.ylabel("Valeur du portefeuille (€)")
    
    graph_path = os.path.join(os.getcwd(), "portfolio_value_evolution.png")
    plt.savefig(graph_path)
    print_centered(f"\n{Fore.CYAN}Le graphique de l'évolution de la valeur du portefeuille a été sauvegardé ici : {graph_path}")

    # Analyse de la distribution des rendements annuels
    plt.figure(figsize=(12, 6))
    sns.histplot(df["Croissance"], kde=True)
    plt.title("Distribution des rendements annuels")
    plt.xlabel("Rendement annuel (%)")
    plt.ylabel("Fréquence")
    
    graph_path = os.path.join(os.getcwd(), "annual_returns_distribution.png")
    plt.savefig(graph_path)
    print_centered(f"\n{Fore.CYAN}Le graphique de la distribution des rendements annuels a été sauvegardé ici : {graph_path}")

    input(Fore.CYAN + "\nAppuyez sur Entrée pour revenir au menu principal...")

def calculate_volatility(portfolio, years):
    returns = []
    total_value = 1000  # Valeur initiale arbitraire

    for _ in range(years):
        year_return = 0
        for asset, allocation in portfolio.items():
            if "obligations" in asset.lower():
                growth = random.uniform(0.01, 0.05)
            elif "actions" in asset.lower() or "reits" in asset.lower():
                growth = random.uniform(0.05, 0.12)
            elif "crypto" in asset.lower():
                growth = random.uniform(-0.2, 0.5)
            elif "or" in asset.lower():
                growth = random.uniform(0, 0.07)
            else:
                growth = random.uniform(0.02, 0.08)
            year_return += (growth * allocation / 100)
        
        returns.append(year_return)
        total_value *= (1 + year_return)

    return np.std(returns) * 100  # Convertir en pourcentage

def main():
    portfolio = None
    while True:
        choice = get_user_choice()
        if choice == 1:
            risk = get_risk_profile()
            amount = get_investment_amount()
            portfolio = suggest_portfolio(risk, amount)
            display_disclaimer()
        elif choice == 2:
            if portfolio:
                portfolio = modify_existing_profile(portfolio)
            else:
                print_centered(Fore.RED + "Veuillez d'abord créer un profil d'investissement (option 1).")
                input(Fore.CYAN + "Appuyez sur Entrée pour continuer...")
        elif choice == 3:
            if portfolio:
                years = int(input(Fore.YELLOW + "Sur combien d'années voulez-vous simuler la performance ? " + Fore.WHITE))
                initial_investment = get_initial_investment()
                monthly_contribution = get_monthly_contribution()
                simulate_performance(portfolio, years, initial_investment, monthly_contribution)
                
                # Calculer et afficher la volatilité
                volatility = calculate_volatility(portfolio, years)
                print_centered(f"{Fore.YELLOW}Volatilité estimée du portefeuille : {volatility:.2f}%")
                print_centered(Fore.WHITE + "La volatilité mesure la variation des rendements. Une volatilité plus élevée indique un risque plus important.")
                
                input(Fore.CYAN + "Appuyez sur Entrée pour continuer...")
            else:
                print_centered(Fore.RED + "Veuillez d'abord créer un profil d'investissement (option 1).")
                input(Fore.CYAN + "Appuyez sur Entrée pour continuer...")
        elif choice == 4:
            if portfolio:
                portfolio = rebalance_portfolio(portfolio)
            else:
                print_centered(Fore.RED + "Veuillez d'abord créer un profil d'investissement (option 1).")
                input(Fore.CYAN + "Appuyez sur Entrée pour continuer...")
        elif choice == 5:
            compare_strategies()
        elif choice == 6:
            analyze_performance_history()
        elif choice == 7:
            display_help()
        else:
            clear_screen()
            print_header()
            print_centered(Fore.YELLOW + "\nMerci d'avoir utilisé le conseiller d'investissement DCA avancé. Au revoir !")
            break

if __name__ == "__main__":
    main()
