import ttkbootstrap as ttk
import tkinter.font as tkFont
from ttkbootstrap.constants import *
from math import comb
import webbrowser

# Dicionário de vendedores com seus itens e preços
vendors = {
    'Ziyad': {
	'Ancient Amulet': '500 gp',
	'Annihilation Bear': '150000 gp',
	'Aquamarine': '350 gp',
	'Arming Sword': '20000 gp',
	'Assassin Dagger': '1000 gp',
	'Bascinet': '24000 gp',
	'Blood Mace': '120000 gp',
	'Bone Shield': '100 gp',
	'Bone Sword': '220 gp',
	'Bright Sword': '8000 gp',
	'Castle Shield': '35000 gp',
	'Crescent Axe': '60000 gp',
	'Crescent Mace': '60000 gp',
	'Crescent Sword': '60000 gp',
	'Crystal Ring': '100 gp',
	'Crystallized Shield': '16000 gp',
	'Demon Shield': '30000 gp',
	'Devil Helmet': '1000 gp',
	'Dragon Scale Mail': '30000 gp',
	'Dragon Slayer': '40000 gp',
	'Elite Knight Armor': '80000 gp',
	'Elite Knight Boots': '40000 gp',
	'Elite Knight Helmet': '52000 gp',
	'Elite Knight Legs': '60000 gp',
	'Emerald Bangle': '400 gp',
	'Executioner\'s Sword': '130000 gp',
	'Frozen Shield': '29000 gp',
	'Gatecrasher': '4000 gp',
	'Gold Ring': '8000 gp',
	'Golden Amulet': '1600 gp',
	'Golden Armor': '20000 gp',
	'Grim Boots': '10000 gp',
	'Grim Legs': '30000 gp',
	'Guardian Halberd': '8000 gp',
	'Heavy Halberd': '35000 gp',
	'Heavy Machete': '130 gp',
	'Hellforged Shield': '36000 gp',
	'Holy Scepter': '50000 gp',
	'Huntsman Armor': '25000 gp',
	'Imperial Soldier Armor': '5500 gp',
	'Imperial Soldier Legs': '20000 gp',
	'Imperial Soldier Shield': '3000 gp',
	'Light Sword': '4500 gp',
	'Medusa Shield': '8000 gp',
	'Mercenary Sword': '45000 gp',
	'Mystic Turban': '1000 gp',
	'Nether Shield': '6600 gp',
	'Platinum Amulet': '1500 gp',
	'Ring of the Sky': '20000 gp',
	'Ruby Necklace': '900 gp',
	'Scarab Amulet': '500 gp',
	'Scarab Coin': '150 gp',
	'Scarab Shield': '1500 gp',
	'Shakirian Blade': '35000 gp',
	'Shakirian Mace': '80 gp',
	'Shakirian Shield': '11300 gp',
	'Shakirian Spellbook': '1350 gp',
	'Shakirian Wand': '6000 gp',
	'Shakirian Waraxe': '1000 gp',
	'Silver Brooch': '125 gp',
	'Silver Dagger': '500 gp',
	'Smoking Pipe': '600 gp',
	'Steel Boots': '30000 gp',
	'Stinger': '7000 gp',
	'Swinging Demolisher': '16000 gp',
	'Tortoise Boots': '3500 gp',
	'Venomous Mace': '75000 gp',
	'Wand of Light': '4000 gp',
	'Watcher Helmet': '2500 gp'
    },
    'Nah\'bob (Blue Djinn)': {
	'Broad Sword': '500 gp',
	'Obsidian Lance': '500 gp',
	'Noble Armor': '900 gp',
	'Ice Rapier': '1000 gp',
	'Spike Sword': '1000 gp',
	'War Hammer': '1200 gp',
	'Watcher Shield': '1200 gp',
	'Guardian Shield': '2000 gp',
	'Scorpid Hood': '2300 gp',
	'Crown Helmet': '2500 gp',
	'Dragon Shield': '4000 gp',
	'Fire Sword': '4000 gp',
	'Electric Helmet': '5000 gp',
	'Crusader Helmet': '6000 gp',
	'Electric Legs': '7000 gp',
	'Crown Shield': '8000 gp',
	'Fire Axe': '8000 gp',
	'Dragon Lance': '9000 gp',
	'Blue Robe': '10000 gp',
	'Electric Armor': '10000 gp',
	'Crown Armor': '12000 gp',
	'Crown Legs': '12000 gp',
	'Phoenix Shield': '16000 gp',
	'Boots of Haste': '30000 gp',
	'Royal Helmet': '30000 gp'
    },
    'Haroun (Blue Djinn)': {
	'Magic Lightwand': '35 gp',
	'Bronze Amulet': '50 gp',
	'Garlic Necklace': '50 gp',
	'Life Crystal': '50 gp',
	'Elven Amulet': '100 gp',
	'Melee Ring': '100 gp',
	'Mind Stone': '170 gp',
	'Stealth Ring': '200 gp',
	'Stone Skin Amulet': '500 gp',
	'Conjure Wand': '500 gp',
	'Orb': '750 gp',
	'Living Thunder': '1000 gp',
	'Golden Wand': '1500 gp',
	'Serpent Scepter': '1500 gp',
	'Fireweaver': '4000 gp',
	'Red Spellwand': '5000 gp',
	'Blue Spellwand': '5000 gp',
	'Green Spellwand': '5000 gp',
	'Staff of Might': '5000 gp',
	'Stormcaller': '8000 gp',
	'Shadowfall': '15000 gp',
	'Frostwarden': '30000 gp'
    },
    'Yaman (Green Djinn)': {
	'Strange Talisman': '30 gp',
	'Life Ring': '50 gp',
	'Mysterious Fetish': '50 gp',
	'Silver Amulet': '50 gp',
	'Spellbook': '75 gp',
	'Ankh': '100 gp',
	'Dragon Necklace': '100 gp',
	'Dwarven Ring': '100 gp',
	'Energy Ring': '100 gp',
	'Protection Amulet': '100 gp',
	'Ring of Healing': '100 gp',
	'Time Ring': '100 gp',
	'Might Ring': '200 gp'
    },
    'Alesar (Green Djinn)': {
	'Poison Dagger': '50 gp',
	'Scimitar': '150 gp',
	'Dark Shield': '166 gp',
	'Dark Helmet': '250 gp',
	'Dark Armor': '400 gp',
	'Strange Helmet': '500 gp',
	'Black Shield': '800 gp',
	'Ancient Shield': '900 gp',
	'Serpent Sword': '900 gp',
	'Mystic Turban': '1000 gp',
	'Curved Axe': '1200 gp',
	'Dwarven Axe': '1500 gp',
	'Naginata': '1500 gp',
	'Dragon Hammer': '2000 gp',
	'Knight Axe': '2000 gp',
	'Spider Silk Armor': '2000 gp',
	'Knight Helmet': '2300 gp',
	'Spiked Club': '3200 gp',
	'Knight Armor': '5000 gp',
	'Knight Legs': '5000 gp',
	'Warrior Helmet': '5000 gp',
	'Skull Staff': '6000 gp',
	'Tower Shield': '8000 gp',
	'Vampire Shield': '15000 gp',
	'The Sky Piercer': '16500 gp',
	'Giant Sword': '17000 gp'
    },
    'Wulkan': {
	'Albino Scale Mail': '230000 gp',
	'Ancient Armor': '75000 gp',
	'Ancient Boots': '5000 gp',
	'Ancient Helmet': '42000 gp',
	'Ancient Legs': '45000 gp',
	'Ancient Sword': '40000 gp',
	'Archlight Wand': '92000 gp',
	'Assassin Blade': '6300 gp',
	'Bone Basher': '5500 gp',
	'Chaos Shield': '500000 gp',
	'Chaos Sword': '300000 gp',
	'Corrupted Staff': '4000 gp',
	'Crown Boots': '12000 gp',
	'Demon Armor': '150000 gp',
	'Demon Helmet': '45000 gp',
	'Demonbone Armor': '40000 gp',
	'Demonbone Boots': '14000 gp',
	'Demonbone Helmet': '9000 gp',
	'Demonbone Legs': '60000 gp',
	'Drake Scale Helmet': '850 gp',
	'Fiery Armor': '7500 gp',
	'Fiery Helmet': '7500 gp',
	'Frostwind': '230000 gp',
	'Golden Legs': '50000 gp',
	'Hellforged Axe': '50000 gp',
	'Hellforged Shield': '36000 gp',
	'Helmet of the Fallen King': '40000 gp',
	'Hydra Scale Legs': '130000 gp',
	'Icebound Armor': '230000 gp',
	'Icebound Helmet': '60000 gp',
	'Icebound Legs': '230000 gp',
	'Light Armor': '13000 gp',
	'Magic Plate Armor': '200000 gp',
	'Magic Plate Boots': '80000 gp',
	'Magic Plate Legs': '120000 gp',
	'Magic Sword': '150000 gp',
	'Mastermind Shield': '50000 gp',
	'Red Scale Armor': '190000 gp',
	'Royal Plate Armor': '35000 gp',
	'Shield of the Heroes': '38000 gp',
	'Silver Mace': '16500 gp',
	'Soul Dagger': '200 gp',
	'Stonecutter Axe': '150000 gp',
	'Sulphira\'s Scale Mail': '300000 gp',
	'Torn Quicksand Boots': '10000 gp',
	'Unholy Halberd': '5500 gp',
	'Unholy Plate Armor': '15000 gp',
	'Vanadinite Armor': '90000 gp',
	'Vanadinite Helmet': '36000 gp',
	'Vanadinite Legs': '55000 gp',
	'Vanquisher': '100000 gp',
	'Venom Greataxe': '80000 gp',
	'Venom Greathammer': '80000 gp',
	'Venom Greatsword': '80000 gp',
	'Venom Wand': '80000 gp',
	'Void Mace': '150000 gp',
	'Wooden Maul': '2000 gp'
    },
    'Aremis': {
	'Assassin Hood': '6000 gp',
	'Assassin Legs': '8000 gp',
	'Assassin Tunic': '12000 gp',
	'Blazing Crossbow': '70000 gp',
	'Bow': '130 gp',
	'Crescent Bow': '60000 gp',
	'Crossbow': '160 gp',
	'Crystallized Bow': '40000 gp',
	'Crystallized Crossbow': '55000 gp',
	'Elven Bow': '500 gp',
	'Elven Crossbow': '7500 gp',
	'Enhanced Crossbow': '24000 gp',
	'Envenomed Crossbow': '65000 gp',
	'Fiery Bow': '46000 gp',
	'Flaming Bow': '18000 gp',
	'Hunting Bow': '1000 gp',
	'Ignited Bow': '5000 gp',
	'Illumination Ring': '100 gp',
	'Poisoned Bow': '16000 gp',
	'Shakirian Bow': '32000 gp',
	'Venom Crossbow': '80000 gp'
    },
    'Draculd': {
	'Alpha Wolf Tooth Chain': '1000 gp',
	'Corrupted Staff': '4000 gp',
	'Crystallized Axe': '11000 gp',
	'Crystallized Hammer': '13000 gp',
	'Crystallized Sword': '10000 gp',
	'Cursed Gold Coin': '250 gp',
	'Golden Staff': '20000 gp',
	'Fire Hammer': '20000 gp',
	'Frost Dagger': '800 gp',
	'Lich Lord Crown': '140000 gp',
	'Lightbringer Helmet': '40000 gp',
	'Necromantic Bloodrobe': '140000 gp',
	'Pendant of the Gods': '20000 gp',
	'Permafrost Crystal': '3000 gp',
	'Permafrost Longsword': '900 gp',
	'Permafrost Morningstar': '1600 gp',
	'Permafrost Robe': '26000 gp',
	'Permafrost Stone': '7000 gp',
	'Pirate Bandana': '15000 gp',
	'Pirate Captain\'s Hat': '30000 gp',
	'Pirate Eye Patch': '1000 gp',
	'Pirate Hat': '20000 gp',
	'Pirate Hand Hook': '1500 gp',
	'Pirate Sabre': '95 gp',
	'Pirate Skull Belt': '3000 gp',
	'Plaguespreader Robe': '26000 gp',
	'Plaguespreader Rod': '2000 gp',
	'Potion of Power': '60000 gp',
	'Red Skirt': '150 gp',
	'Red Tunic': '5000 gp',
	'Shield of Honour': '50000 gp',
	'Snow Ravager Amulet': '60000 gp',
	'Soul Amulet': '50000 gp',
	'Soul Reaper': '7500 gp',
	'Undead Dragon Trophy': '300000 gp',
	'Wendigo Staff': '900 gp',
	'Worn out Pirate Beater': '200 gp',
	'Worn out Pirate Cape': '250 gp',
	'Worn out Pirate Tabard': '100 gp',
	'Yellow Robe': '18000 gp'
    },
    'Jewelry Npcs': {
	'Small Diamond': '300 gp',
	'Small Sapphire': '250 gp',
	'Small Ruby': '250 gp',
	'Small Emerald': '250 gp',
	'Small Amethyst': '200 gp',
	'Small Topaz': '440 gp',
	'Small Onyx': '460 gp',
	'White Pearl': '160 gp',
	'Black Pearl': '280 gp',
	'Talon': '320 gp',
	'Polished Amethyst': '2500 gp',
	'Polished Emerald': '3000 gp',
	'Polished Ruby': '3000 gp',
	'Polished Sapphire': '3000 gp',
	'Polished Topaz': '5000 gp',
	'Red Gem': '1000 gp',
	'Yellow Gem': '2000 gp',
	'Blue Gem': '25000 gp',
	'Green Gem': '25000 gp',
	'Violet Gem': '50000 gp',
	'Aquamarine': '350 gp',
	'Scarab Coin': '150 gp',
	'Small Onyx': '460 gp',
	'Small Topaz': '440 gp',
	'Triangle Emerald': '400 gp',
	'Ancient Amulet': '500 gp',
	'Ancient Red Gem': '1300 gp',
	'Ancient Yellow Gem': '1300 gp',
	'Crystal Necklace': '200 gp',
	'Crystal Ring': '100 gp',
	'Elven Brooch': '250 gp',
	'Emerald Bangle': '400 gp',
	'Golden Mug': '1000 gp',
	'Ruby Necklace': '900 gp',
	'Scarab Amulet': '500 gp',
	'Silver Amulet': '50 gp',
	'Silver Brooch': '120 gp',
	'Wedding Ring': '100 gp'
    },
    'Potions and Runes Npcs': {
	'Vial': '5 gp',
	'Empty Vial': '30 gp',
	'Mind Stone': '170 gp',
	'Spellbook': '75 gp',
	'Conjure Wand': '500 gp',
	'Crystal Ball': '190 gp',
	'Golden Wand': '1500 gp',
	'Healing Crystal': '2000 gp',
	'Life Crystal': '85 gp',
	'Illumination Ring': '100 gp',
	'Magic Lightwand': '50 gp',
	'Mysterious Fetish': '300 gp',
	'Orb': '750 gp',
	'Strange Symbol': '600 gp'
    },
    'Equipment Trader Npcs (Eliane Eschen)': {
	'Black Tapestry': '4000 gp',
	'Blue Hood': '22000 gp',
	'Doll': '80 gp',
	'Mystic Turban': '1000 gp',
	'Nether Spider Doll': '8000 gp',
	'Rainbow Tapestry': '7000 gp',
	'Red Robe': '12000 gp',
	'Royal Dress': '20000 gp',
	'Simple Dress': '80 gp',
	'Spider Silk': '40 gp',
	'Wolf Tooth Chain': '50 gp'
    },
    'Drolgruth (Sheol)': {
	'Double Axe Head': '3000 gp',
	'Ritual Dagger': '6000 gp',
	'Webcrawler Shield': '12000 gp',
	'Angry Soul': '20000 gp',
	'Broken Whip': '23500 gp',
	'Tainted Soul':	'25000 gp',
	'Forgotten Soul': '30000 gp',
	'Arcane Shoes':	'35000 gp',
	'Ashlord Shield': '40000 gp',
	'Red Heels': '41500 gp',
	'Warlord Helmet': '42000 gp',
	'Arcane Cowl': '45000 gp',
	'Arcane Kilt': '50000 gp',
	'Webcrawler Boots': '53000 gp',
	'Arcane Robe': '64500 gp',
	'Observer Helmet': '67000 gp',
	'Skullbreaker': '78000 gp',
	'War Axe': '80000 gp',
	'Observer Shield': '82000 gp',
	'High Heels of Seduction': '84000 gp',
	'Watcher Boots': '85000 gp',
	'Angelic Boots': '95000 gp',
	'Virulent Clawboots': '100000 gp',
	'Lich Grimoire': '108000 gp',
	'Watcher Legs':	'110500 gp',
	'Arcane Tunic':	'125000 gp',
	'Watcher Armor': '125000 gp',
	'Virulent Helmet': '130000 gp',
	'Emberwake Tunic': '142000 gp',
	'Plague Mask':	'145000 gp',
	'Angelic Helmet': '152000 gp',
	'Jade Tear': '165000 gp',
	'Ruby Tear': '165000 gp',
	'Jadeite Boots': '178000 gp',
	'Deepshadow Boots': '200000 gp',
	'Shadowfall Crossbow': '200000 gp',
	'Demonic Axe': '215000 gp',
	'Soulstealer Armor': '218000 gp',
	'Fire Whip': '220000 gp',
	'Angelic Plate Armor': '222000 gp',
	'Angelic Platemail': '222000 gp',
	'Virulent Legs': '225000 gp',
	'The Deathraze': '235000 gp',
	'Deepshadow Mask': '245000 gp',
	'Artifact of Penance': '250000 gp',
	'The Bloodcurser': '280000 gp',
	'Deepshadow Legs': '285000 gp',
	'Blazing Greatsword': '300000 gp',
	'Heavy Truncheon': '300000 gp',
	'Hellforged Legs': '300000 gp',
	'Umbral Boots': '300000 gp',
	'Umbral Helmet': '300000 gp',
	'Mirror Shield': '310000 gp',
	'Virulent Armor': '320000 gp',
	'Deepshadow Robe': '325000 gp',
	'Umbral Legs': '335000 gp',
	'Deepshadow Amulet': '340000 gp',
	'Flaming Aegis': '375000 gp',
	'Emberwake Ring': '400000 gp',
	'Chaos Axe': '600000 gp',
	'Chaos Hammer': '600000 gp',
	'Chaos Sword': '600000 gp',
	'The Dawnbringer': '600000 gp',
	'The Lightbane': '600000 gp',
	'The Twilight': '600000 gp',
	'Dreadweave Robe': '600000 gp',
	'Hellforged Armor': '600000 gp',
	'The Ward of Sheol': '625000 gp',
	'Solar Amulet': '666000 gp',
	'Umbral Plate Armor': '688000 gp',
	'Umbral Platemail': '688000 gp',
	'Umbral Robe': '688000 gp',
	'Hallowed Flame': '145000 gp',
	'Abyssal Scriptures': '8000 gp',
	'Abysmor Claw':	'8000 gp',
	'Eyes of Abysmor': '6000 gp',
	'Hallowed Piece of Cloth': '6000 gp',
	'Prismatic Shard': '5000 gp',
	'Abyssal Fang':	'5000 gp',
	'Blazing Core': '80000 gp'
    },
    'Glechoma (Garrogat)': {
	'Heart of Fire':'50 gp',
	'Purple Tome': '3000 gp',
	'Red Tome': '2000 gp',
	'Dwarven Tome': '14000 gp',
	'Elven Tome': '6000 gp',
	'Human Tome': '4000 gp',
	'Minotaur Tome': '4000 gp',
	'Orcish Tome': '4000 gp'
    }
}

# ------------------- Funções -------------------
def parse_price(price_str):
    return int(price_str.split()[0])

item_to_vendor = {}
for vendor, items in vendors.items():
    for item, price in items.items():
        item_to_vendor[item] = (vendor, parse_price(price))

def find_item(item_name):
    return item_to_vendor.get(item_name, (None, None))

def probability_of_dropping(kind, n, k, p):
    p /= 100
    if kind == "exactly":
        return comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) * 100
    else:  # "at least"
        s = 0
        for i in range(k):
            s += comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
        return (1 - s) * 100

# ------------------- Classes -------------------
class MediviaToolsApp(ttk.Window):
    def __init__(self):
        super().__init__(themename="superhero")      # solar ou superhero
        self.title("Medivia Tools GUI")
        self.geometry("900x700")
        self.resizable(False, False)

        self.n_players = 0
        self.player_names = []
        self.supplies = []

        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12))
        style.configure("TRadiobutton", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12, "bold"))
        style.configure("My.Link.TButton", foreground="#2340c4", font=("Helvetica", 12, "italic"))
        style.map("My.Link.TButton", foreground=[("!disabled", "#a0a0a0"), ("active", "#e53935"), ("pressed", "#00ced1")])
        style.configure("CustomHeader.TLabel", foreground="#a0a0a0", font=("Helvetica", 8, "bold"))
        style.configure("CustomVersion.TLabel", foreground="#a0a0a0", font=("Helvetica", 12, "italic"))

        self.container = ttk.Frame(self, padding=10)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (MainMenu, SupplyCalc, ProfitDiv, ItemSearch, DropCalc):
            page = F(parent=self.container, controller=self)
            self.frames[F.__name__] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, name):
        self.frames[name].tkraise()

class MainMenu(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        frame_title = ttk.Frame(self)
        frame_title.pack(anchor="w", pady=20, padx=0)

        ttk.Label(frame_title, text="Medivia Tools", font=("Helvetica", 99, "bold"), bootstyle="info").pack(anchor="w", pady=(0, 0))

        btn = ttk.Button(frame_title, text='By Mathema "ri" cs', style="My.Link.TButton",
                         command=lambda: webbrowser.open("https://mediviathings.net/characters/search/?name=matematiico"),
                         cursor="hand2")
        btn.pack(anchor="w")

        frame_buttons = ttk.Frame(self)
        frame_buttons.pack(pady=(55, 0))

        ttk.Button(frame_buttons, text="Calculate Supplies", width=50, bootstyle="primary-outline",
                   command=lambda: controller.show_frame("SupplyCalc")).pack(pady=8)
        ttk.Button(frame_buttons, text="Divide Hunt Profit", width=50, bootstyle="warning-outline",
                   command=lambda: controller.show_frame("ProfitDiv")).pack(pady=8)
        ttk.Button(frame_buttons, text="Where to Buy/Sell Item", width=50, bootstyle="success-outline",
                   command=lambda: controller.show_frame("ItemSearch")).pack(pady=8)
        ttk.Button(frame_buttons, text="Drop Calculator", width=50, bootstyle="info-outline",
                   command=lambda: controller.show_frame("DropCalc")).pack(pady=8)
        ttk.Button(frame_buttons, text="Exit", width=50, bootstyle="danger-outline",
                   command=controller.destroy).pack(pady=(82, 0))

        ttk.Label(self, text='v2.8', style="CustomVersion.TLabel").pack(side="right", pady=100)

class SupplyCalc(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Calculate Supplies", font=("Helvetica", 60, "bold"), bootstyle="info").pack(pady=10)

        frame_n = ttk.Frame(self)
        frame_n.pack(pady=5)

        ttk.Label(frame_n, text="Number of Players ", font=("Helvetica", 14, "italic")).pack(side="left")

        self.entry_num = ttk.Entry(frame_n, width=8)
        self.entry_num.pack(side="left")
        self.entry_num.insert(0, "1")

        btn_set = ttk.Button(frame_n, text="Confirm", bootstyle="secondary", command=self.setup_player_entries)
        btn_set.pack(side="left", padx=1)

        self.players_frame = ttk.Frame(self)
        self.players_frame.pack(pady=10)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", pady=10)

        ttk.Button(btn_frame, text="Calculate", bootstyle="success", command=self.calculate_supplies).pack(side="left", padx=16)
        ttk.Button(btn_frame, text="Back", bootstyle="danger-outline", command=lambda: controller.show_frame("MainMenu")).pack(side="right", padx=16)

        # Label para mensagens embaixo da tabela
        self.message_label = ttk.Label(self, text="", font=("Helvetica", 12, "italic"))
        self.message_label.pack(pady=(0, 10))

        self.player_inputs = []

        self.setup_player_entries()

    def setup_player_entries(self):
        for widget in self.players_frame.winfo_children():
            widget.destroy()

        self.player_inputs = []

        try:
            n = int(self.entry_num.get())
            if n < 1 or n > 20:
                raise ValueError
        except ValueError:
            self.show_error("Provide a number of players between 1 and 20.")
            return

        # Cabeçalhos incluindo a coluna "Total gp"
        colh = ["Name", "UH", "Potion", "SD", "GFB", "Explo", "Smalls/Arrows", "Total"]
        colw = [14, 6, 6, 6, 6, 6, 13, 12]

        for c, w, head in zip(range(len(colh)), colw, colh):
            ttk.Label(self.players_frame, text=head, width=w, style="CustomHeader.TLabel").grid(row=0, column=c, padx=1, pady=2)

        for i in range(n):
            ent_name = ttk.Entry(self.players_frame, width=14)
            ent_uh = ttk.Entry(self.players_frame, width=6)
            ent_gm = ttk.Entry(self.players_frame, width=6)
            ent_sd = ttk.Entry(self.players_frame, width=6)
            ent_gfb = ttk.Entry(self.players_frame, width=6)
            ent_exp = ttk.Entry(self.players_frame, width=6)
            ent_sexp = ttk.Entry(self.players_frame, width=9)
            ent_total = ttk.Entry(self.players_frame, width=12, state="readonly")

            ent_name.insert(0, f"Player {i+1}")
            ent_uh.insert(0, "0")
            ent_gm.insert(0, "0")
            ent_sd.insert(0, "0")
            ent_gfb.insert(0, "0")
            ent_exp.insert(0, "0")
            ent_sexp.insert(0, "0")

            ent_name.grid(row=i+1, column=0, padx=1, pady=1)
            ent_uh.grid(row=i+1, column=1, padx=1, pady=1)
            ent_gm.grid(row=i+1, column=2, padx=1, pady=1)
            ent_sd.grid(row=i+1, column=3, padx=1, pady=1)
            ent_gfb.grid(row=i+1, column=4, padx=1, pady=1)
            ent_exp.grid(row=i+1, column=5, padx=1, pady=1)
            ent_sexp.grid(row=i+1, column=6, padx=1, pady=1)
            ent_total.grid(row=i+1, column=7, padx=1, pady=1)

            ent = [ent_name, ent_uh, ent_gm, ent_sd, ent_gfb, ent_exp, ent_sexp, ent_total]
            self.player_inputs.append(ent)

        self.message_label.config(text="")  # limpa mensagem

    def show_error(self, text):
        self.message_label.config(text=text, foreground="red")

    def calculate_supplies(self):
        self.message_label.config(text="", foreground="green")

        try:
            for entries in self.player_inputs:
                name = entries[0].get().strip()
                vals = [int(e.get()) for e in entries[1:-1]]  # exclui último que é o total
                if not name:
                    raise ValueError("Empty name")

                total = vals[0]*145 + vals[1]*850 + vals[2]*330 + vals[3]*195 + vals[4]*260 + vals[5]*55

                total_entry = entries[-1]
                total_entry.config(state="normal")
                total_entry.delete(0, "end")
                total_entry.insert(0, f"{total} gp")
                total_entry.config(state="readonly")

            # Guarda nomes e valores no controlador, para ser usado por outras abas
            self.controller.player_names = [e[0].get().strip() for e in self.player_inputs]
            self.controller.supplies = [int(e[-1].get().split()[0]) for e in self.player_inputs]

            self.message_label.config(text="Calculation done.", foreground="green")

        except Exception:
            self.message_label.config(text="Fill everything out correctly!", foreground="red")
            return

class ProfitDiv(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Divide Hunt Profit", font=("Helvetica", 60, "bold"), bootstyle="info").pack(pady=10)

        ttk.Button(self, text="Use calculated supplies", bootstyle="light-outline", command=self.use_supplies).pack(pady=4)
        ttk.Label(self, text="Or enter supplies spent manually", font=("Helvetica", 11, "italic")).pack(pady=5)

        frame_n = ttk.Frame(self)
        frame_n.pack(pady=5)

        ttk.Label(frame_n, text="Number of players ", font=("Helvetica", 14, "italic")).pack(side="left")

        self.entry_num = ttk.Entry(frame_n, width=8)
        self.entry_num.pack(side="left")
        self.entry_num.insert(0, "1")

        ttk.Button(frame_n, text="Confirm", bootstyle="secondary", command=self.setup_player_manual).pack(side="left", padx=1)

        self.players_frame = ttk.Frame(self)
        self.players_frame.pack(pady=8)

        loot_frame = ttk.Frame(self)
        loot_frame.pack()

        self.result_frame = ttk.Frame(self)
        self.result_frame.pack(pady=(12,0))

        ttk.Label(loot_frame, text="Total loot value ", font=("Helvetica", 12, "italic")).pack(side="left", padx=9)

        self.entry_loot = ttk.Entry(loot_frame, width=12)
        self.entry_loot.pack(side="left")

        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", pady=10)

        ttk.Button(btn_frame, text="Calculate Profit", bootstyle="success", command=self.calculate_profit).pack(side="left", padx=16)
        ttk.Button(btn_frame, text="Back", bootstyle="danger-outline", command=lambda: self.controller.show_frame("MainMenu")).pack(side="right", padx=16)

        self.player_inputs = []
        self.to_pay_entries = []

        self.setup_player_manual()

    def use_supplies(self):
        if not self.controller.supplies or not self.controller.player_names:
            for w in self.result_frame.winfo_children():
                w.destroy()
            ttk.Label(self.result_frame, text="No calculated supplies. Please calculate them first.", foreground="red").pack(anchor="w")
            return
        self.setup_from_supplies()

    def setup_from_supplies(self):
        for widget in self.players_frame.winfo_children():
            widget.destroy()

        self.player_inputs.clear()
        self.to_pay_entries.clear()

        self.entry_num.delete(0, "end")
        self.entry_num.insert(0, str(len(self.controller.supplies)))

        # Header
        header = ttk.Frame(self.players_frame)
        header.pack(anchor="w")

        ttk.Label(header, text="Player:", width=14, font=("Helvetica", 10, "bold")).pack(side="left")
        ttk.Label(header, text="Waste:", width=13, font=("Helvetica", 10, "bold")).pack(side="left")
        ttk.Label(header, text="To be Paid:", width=14, font=("Helvetica", 10, "bold")).pack(side="left")

        for name, spent in zip(self.controller.player_names, self.controller.supplies):
            frame = ttk.Frame(self.players_frame)
            frame.pack(anchor="w", pady=1)

            e_name = ttk.Entry(frame, width=15)
            e_name.pack(side="left")
            e_name.insert(0, name)

            e_spent = ttk.Entry(frame, width=12)
            e_spent.pack(side="left", padx=6)
            e_spent.insert(0, str(spent))

            e_topay = ttk.Entry(frame, width=13, justify="center", state="readonly")
            e_topay.pack(side="left", padx=6)

            self.player_inputs.append((e_name, e_spent))
            self.to_pay_entries.append(e_topay)

    def setup_player_manual(self):
        for widget in self.players_frame.winfo_children():
            widget.destroy()

        self.player_inputs = []
        self.to_pay_entries = []

        try:
            n = int(self.entry_num.get())
            if n < 1 or n > 20:
                raise ValueError
        except ValueError:
            for w in self.result_frame.winfo_children():
                w.destroy()
            ttk.Label(self.result_frame, text="Provide a number of players between 1 and 20.", foreground="red").pack(anchor="w")
            return

        # Header
        header = ttk.Frame(self.players_frame)
        header.pack(anchor="w")

        ttk.Label(header, text="Player:", width=14, font=("Helvetica", 10, "bold")).pack(side="left")
        ttk.Label(header, text="Waste:", width=13, font=("Helvetica", 10, "bold")).pack(side="left")
        ttk.Label(header, text="To be Paid:", width=14, font=("Helvetica", 10, "bold")).pack(side="left")

        for i in range(n):
            frame = ttk.Frame(self.players_frame)
            frame.pack(anchor="w", pady=1)

            e_name = ttk.Entry(frame, width=15)
            e_name.pack(side="left")
            e_name.insert(0, f"Player {i+1}")

            e_spent = ttk.Entry(frame, width=12)
            e_spent.pack(side="left", padx=6)

            e_topay = ttk.Entry(frame, width=13, justify="center", state="readonly")
            e_topay.pack(side="left", padx=6)

            self.player_inputs.append((e_name, e_spent))
            self.to_pay_entries.append(e_topay)

    def calculate_profit(self):
        for w in self.result_frame.winfo_children():
            w.destroy()

        player_names = []
        spent = []

        try:
            for name_e, spent_e in self.player_inputs:
                name = name_e.get().strip()
                value = int(spent_e.get())
                if not name:
                    raise ValueError("Empty name")
                player_names.append(name)
                spent.append(value)
            loot = int(self.entry_loot.get())
        except Exception:
            ttk.Label(self.result_frame, text="Fill everything out correctly!", foreground="red").pack()
            return

        profit = loot - sum(spent)
        n = len(player_names)
        profit_ind = profit // n if n > 0 else 0

        # Atualiza os campos 'a pagar' ao lado do campo 'Gasto'
        for i, val in enumerate(spent):
            e = self.to_pay_entries[i]
            e.config(state="normal")
            e.delete(0, "end")
            e.insert(0, f"{val + profit_ind} gp")
            e.config(state="readonly")

        # Só exibe o resumo geral na área de resultados embaixo
        ttk.Label(self.result_frame, text="Hunt Info", font=("Helvetica", 15, "bold")).pack()
        ttk.Label(self.result_frame, text=f"Waste Total: {sum(spent)} gp", font=("Helvetica", 12, "italic")).pack()
        ttk.Label(self.result_frame, text=f"Profit Total: {profit} gp",font=("Helvetica", 12, "italic")).pack()
        ttk.Label(self.result_frame, text=f"Profit per Player: {profit_ind} gp", font=("Helvetica", 12, "italic")).pack()

class ItemSearch(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Where to Buy/Sell Item", font=("Helvetica", 60, "bold"), bootstyle="info").pack(pady=20)

        frame_search = ttk.Frame(self)
        frame_search.pack(pady=15)

        ttk.Label(frame_search, text="Item name ", font=("Helvetica", 14)).pack(side="left")

        self.entry_item = ttk.Entry(frame_search, width=30)
        self.entry_item.pack(side="left", padx=1)

        ttk.Button(frame_search, text="Search", bootstyle="secondary", command=self.lookup_item).pack(side="left", padx=1)
        ttk.Button(self, text="Back", bootstyle="danger-outline", command=lambda: controller.show_frame("MainMenu")).pack(pady=15)

        self.result_frame = ttk.Frame(self)
        self.result_frame.pack(pady=16)

    def lookup_item(self):
        for w in self.result_frame.winfo_children():
            w.destroy()

        item = self.entry_item.get().strip()
        vendor, price = find_item(item)

        if not item:
            ttk.Label(self.result_frame, text="Enter the name of the item.", foreground="red").pack()
        elif vendor:
            ttk.Label(self.result_frame, text=f"Item: {item}", font=("Helvetica", 12, "bold")).pack(anchor="w")
            ttk.Label(self.result_frame, text=f"Vendor: {vendor}").pack(anchor="w")
            e = ttk.Entry(self.result_frame, width=15)
            e.insert(0, f"{price} gp")
            e.config(state="readonly")
            e.pack(anchor="w")
        else:
            ttk.Label(self.result_frame, text=f"Item '{item}' not found.", foreground="orange").pack()

class DropCalc(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Drop Calculator", font=("Helvetica", 60, "bold"), bootstyle="info").pack(pady=15)

        frame_type = ttk.Frame(self)
        frame_type.pack(pady=5)

        ttk.Label(frame_type, text="Drop type:").pack(side="left")

        self.type_var = ttk.StringVar(value="item")

        ttk.Radiobutton(frame_type, text="Item", variable=self.type_var, value="item", bootstyle="primary", command=self.build_fields).pack(side="left", padx=5)
        ttk.Radiobutton(frame_type, text="Skin", variable=self.type_var, value="skin", bootstyle="primary", command=self.build_fields).pack(side="left", padx=5)

        self.fields_frame = ttk.Frame(self)
        self.fields_frame.pack(pady=10)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Calculate", bootstyle="success", command=self.calculate_probability).pack(side="left", padx=14)
        ttk.Button(btn_frame, text="Back", bootstyle="danger-outline", command=lambda: controller.show_frame("MainMenu")).pack(side="left", padx=14)

        self.result_frame = ttk.Frame(self)
        self.result_frame.pack(pady=18)

        self.build_fields()

    def build_fields(self):
        for widget in self.fields_frame.winfo_children():
            widget.destroy()

        kind = self.type_var.get()

        if kind == "item":
            self.leg_var = ttk.StringVar(value="n")

            frame_legend = ttk.Frame(self.fields_frame)
            frame_legend.pack(anchor="w", pady=3)

            ttk.Label(frame_legend, text="Legendary monster?").pack(side="left")

            ttk.Radiobutton(frame_legend, text="Yes", variable=self.leg_var, value="y", bootstyle="primary", command=self.update_legend_fields).pack(side="left", padx=5)
            ttk.Radiobutton(frame_legend, text="No", variable=self.leg_var, value="n", bootstyle="primary", command=self.update_legend_fields).pack(side="left", padx=5)

            self.frame_inputs = ttk.Frame(self.fields_frame)
            self.frame_inputs.pack(pady=8)

            self.update_legend_fields()

        else:
            for child in self.fields_frame.winfo_children():
                if hasattr(child, 'destroy'):
                    child.destroy()

            frame_prob = ttk.Frame(self.fields_frame)
            frame_prob.pack(anchor="w", pady=3)
            ttk.Label(frame_prob, text="Drop probability (%)").pack(side="left")
            self.entry_prob = ttk.Entry(frame_prob, width=10)
            self.entry_prob.pack(side="left", padx=5)

            frame_tent = ttk.Frame(self.fields_frame)
            frame_tent.pack(anchor="w", pady=3)
            ttk.Label(frame_tent, text="Number of attempts (Kills)").pack(side="left")
            self.entry_tent = ttk.Entry(frame_tent, width=10)
            self.entry_tent.pack(side="left", padx=5)

            frame_qtd = ttk.Frame(self.fields_frame)
            frame_qtd.pack(anchor="w", pady=3)
            ttk.Label(frame_qtd, text="Quantity desired").pack(side="left")
            self.entry_qtd = ttk.Entry(frame_qtd, width=10)
            self.entry_qtd.pack(side="left", padx=5)

            frame_kind_calc = ttk.Frame(self.fields_frame)
            frame_kind_calc.pack(anchor="w", pady=3)
            ttk.Label(frame_kind_calc, text="Calculation type").pack(side="left")
            self.kind_calc_var = ttk.StringVar(value="exactly")
            ttk.Radiobutton(frame_kind_calc, text="Exactly", variable=self.kind_calc_var, value="exactly", bootstyle="primary").pack(side="left", padx=5)
            ttk.Radiobutton(frame_kind_calc, text="At least", variable=self.kind_calc_var, value="at least", bootstyle="primary").pack(side="left", padx=5)

    def update_legend_fields(self):
        for widget in self.frame_inputs.winfo_children():
            widget.destroy()

        if self.leg_var.get() == "y":
            # Legendary drop fields
            for label, attr in [
                 ("Monsters per legendary spawn", "entry_nm"),
                 ("Probability range (%) e.g. 0.5 to 1.0", None),
                 ("Number of kills", "entry_tent"),
                 ("Desired quantity", "entry_qtd")
            ]:
                frame = ttk.Frame(self.frame_inputs)
                frame.pack(anchor="w", pady=3)

                ttk.Label(frame, text=label).pack(side="left")

                if label.startswith("Probability range"):
                    entry_min = ttk.Entry(frame, width=7)
                    entry_min.pack(side="left", padx=(4, 2))
                    lbl_to = ttk.Label(frame, text="to")
                    lbl_to.pack(side="left")
                    entry_max = ttk.Entry(frame, width=7)
                    entry_max.pack(side="left", padx=(2, 4))
                    self.entry_prob_min = entry_min
                    self.entry_prob_max = entry_max
                else:
                    ent = ttk.Entry(frame, width=15)
                    ent.pack(side="left", padx=4)
                    setattr(self, attr, ent)

            frame_kind_calc = ttk.Frame(self.frame_inputs)
            frame_kind_calc.pack(anchor="w", pady=3)
            ttk.Label(frame_kind_calc, text="Calculation type").pack(side="left")
            self.kind_calc_var = ttk.StringVar(value="exactly")
            ttk.Radiobutton(frame_kind_calc, text="Exactly", variable=self.kind_calc_var, value="exactly", bootstyle="primary").pack(side="left", padx=5)
            ttk.Radiobutton(frame_kind_calc, text="At least", variable=self.kind_calc_var, value="at least", bootstyle="primary").pack(side="left", padx=5)

        else:
            # Non-legendary drop fields
            for label, attr in [
                 ("Probability range (%) e.g. 0.5 to 1.0", None),
                 ("Number of kills", "entry_tent"),
                 ("Desired quantity", "entry_qtd")
            ]:
                frame = ttk.Frame(self.frame_inputs)
                frame.pack(anchor="w", pady=3)

                ttk.Label(frame, text=label).pack(side="left")

                if label.startswith("Probability range"):
                    entry_min = ttk.Entry(frame, width=7)
                    entry_min.pack(side="left", padx=(4, 2))
                    lbl_to = ttk.Label(frame, text="to")
                    lbl_to.pack(side="left")
                    entry_max = ttk.Entry(frame, width=7)
                    entry_max.pack(side="left", padx=(2, 4))
                    self.entry_prob_min = entry_min
                    self.entry_prob_max = entry_max
                else:
                    ent = ttk.Entry(frame, width=15)
                    ent.pack(side="left", padx=4)
                    setattr(self, attr, ent)

            frame_kind_calc = ttk.Frame(self.frame_inputs)
            frame_kind_calc.pack(anchor="w", pady=3)
            ttk.Label(frame_kind_calc, text="Calculation type").pack(side="left")
            self.kind_calc_var = ttk.StringVar(value="exactly")
            ttk.Radiobutton(frame_kind_calc, text="Exactly", variable=self.kind_calc_var, value="exactly", bootstyle="primary").pack(side="left", padx=5)
            ttk.Radiobutton(frame_kind_calc, text="At least", variable=self.kind_calc_var, value="at least", bootstyle="primary").pack(side="left", padx=5)

    def calculate_probability(self):
        for w in self.result_frame.winfo_children():
            w.destroy()

        try:
            kind = self.type_var.get()

            if kind == "item":
                if self.leg_var.get() == "y":
                    nm = int(self.entry_nm.get())
                    p_min = float(self.entry_prob_min.get())
                    p_max = float(self.entry_prob_max.get())
                    attempts = int(self.entry_tent.get())
                    quantity = int(self.entry_qtd.get())
                    qtype = self.kind_calc_var.get()
                    attempts = attempts // nm
                    prob_min = probability_of_dropping(qtype, attempts, quantity, p_min)
                    prob_max = probability_of_dropping(qtype, attempts, quantity, p_max)
                    msg = (f"Chance to drop {qtype} {quantity} item(s) is between "
                           f"{prob_min:.2f}% and {prob_max:.2f}% (boss attempts: {attempts})")
                else:
                    p_min = float(self.entry_prob_min.get())
                    p_max = float(self.entry_prob_max.get())
                    attempts = int(self.entry_tent.get())
                    quantity = int(self.entry_qtd.get())
                    qtype = self.kind_calc_var.get()
                    prob_min = probability_of_dropping(qtype, attempts, quantity, p_min)
                    prob_max = probability_of_dropping(qtype, attempts, quantity, p_max)
                    msg = (f"Chance to drop {qtype} {quantity} item(s) is between "
                           f"{prob_min:.2f}% and {prob_max:.2f}%")
            else:
                p = float(self.entry_prob.get())
                attempts = int(self.entry_tent.get())
                quantity = int(self.entry_qtd.get())
                qtype = self.kind_calc_var.get()
                prob = probability_of_dropping(qtype, attempts, quantity, p)
                msg = f"Chance to get {qtype} {quantity} skin(s) is {prob:.2f}%"

            ttk.Label(self.result_frame, text=msg, wraplength=700, font=("Helvetica", 12)).pack(anchor="w")

        except Exception as e:
            ttk.Label(self.result_frame, text="Verifique os campos.\n" + str(e), foreground="red").pack()

# ----------------------

if __name__ == "__main__":
    app = MediviaToolsApp()
    app.mainloop()

## Calculate supplies (tudo ok)
## Divide hunt Profit (tudo ok)
## Where to buy/sell (tudo ok)
	## - atualizar o dicionário
 	## - Em um futuro não tão próximo, ver se é possível colocar o .png de cada item para aparecer junto com o nome
## Drop Calculator (tudo ok)
## pyinstaller --hidden-import "PIL._tkinter_finder" --onefile --windowed gui.py