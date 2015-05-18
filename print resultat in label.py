#!/usr/bin/env python
# -*- coding:Utf-8 -*-

#-------------------------------------------#
#          Importation des packages         #
#-------------------------------------------#
import Tkinter
from Tkinter import *
from threading import Thread
import ttk
import time
import os


#-------------------------------------------#
#         Declaration des variables         #
#-------------------------------------------#
arret_apache = 0
arret_tomcat = 0
arret_ndoutils = 0
arret_nagios = 0
arret_npcd = 0
demarrage_apache = 0
demarrage_tomcat = 0
demarrage_ndoutils = 0
demarrage_nagios = 0
demarrage_npcd = 0
phase_demarrage = 0
i = 0

 
#---------------------------------------------#
#  Declaration des fonctions d'incrementation #
#---------------------------------------------#
def mon_incrementation():
	global i 
	i = i+1
	
def ma_phase_de_demarrage():
	global phase_demarrage
	phase_demarrage = phase_demarrage + 1

def mon_incrementation_demarrage_apache():
	global demarrage_apache
	demarrage_apache = demarrage_apache + 1

def mon_incrementation_demarrage_tomcat():
	global demarrage_tomcat
	demarrage_tomcat = demarrage_tomcat + 1

def mon_incrementation_demarrage_ndoutils():
	global demarrage_ndoutils
	demarrage_ndoutils = demarrage_ndoutils + 1

def mon_incrementation_demarrage_nagios():
	global demarrage_nagios
	demarrage_nagios = demarrage_nagios + 1

def mon_incrementation_demarrage_npcd():
	global demarrage_npcd
	demarrage_npcd = demarrage_npcd + 1

def mon_incrementation_arret_apache():
	global arret_apache
	arret_apache = arret_apache + 1

def mon_incrementation_arret_tomcat():
	global arret_tomcat
	arret_tomcat = arret_tomcat + 1

def mon_incrementation_arret_ndoutils():
	global arret_ndoutils
	arret_ndoutils = arret_ndoutils + 1

def mon_incrementation_arret_nagios():
	global arret_nagios
	arret_nagios = arret_nagios + 1

def mon_incrementation_arret_npcd():
	global arret_npcd
	arret_npcd = arret_npcd + 1

	
#-------------------------------------------#
#       Declararation des fonctions         #
#-------------------------------------------#
def VerificationServices():

	# Démarrage des vérifications d'arrêt et de remontée des services de supervision
	#logger -t redundancy -p local0.info "POPUP : Lancement de la fenêtre graphique"

	# Ne sors pas de la boucle tant que les processus n'ont pas été redémarrés
	Boucle = True
	while Boucle == True:

		# Phase 1 : Arrêt des services
		if phase_demarrage == 0:
		
			# Raffraichissement de la fenètre graphique toutes les secondes
			time.sleep(1)

			apache = os.popen("pgrep apache")
			apache = apache.read()
			if apache == "" and arret_apache == 0:
				mon_incrementation_arret_apache()
				Application.Modif_Composants("apache_KO")
				Application.UpdateBarreProgression()

			tomcat = os.popen("pgrep java")
			tomcat = tomcat.read()
			if tomcat == "" and arret_tomcat == 0:
				mon_incrementation_arret_tomcat()
				Application.Modif_Composants("tomcat_KO")
				Application.UpdateBarreProgression()

			ndoutils = os.popen("pgrep ndo2")
			ndoutils = ndoutils.read()
			if ndoutils == "" and arret_ndoutils == 0:
				mon_incrementation_arret_ndoutils() 
				Application.Modif_Composants("ndoutils_KO")
				Application.UpdateBarreProgression()

			nagios = os.popen("pgrep nagios")
			nagios = nagios.read()
			if nagios == "" and arret_nagios == 0:
				mon_incrementation_arret_nagios()
				Application.Modif_Composants("nagios_KO")
				Application.UpdateBarreProgression()

			npcd = os.popen("pgrep npcd")
			npcd = npcd.read()
			if npcd == "" and arret_npcd == 0:
				mon_incrementation_arret_npcd()
				Application.Modif_Composants("npcd_KO")
				Application.UpdateBarreProgression()

			if (apache == "") and (tomcat == "") \
			and (ndoutils == "") and (nagios == "") \
			and (npcd == ""):
				ma_phase_de_demarrage()
				Application.Modif_Composants("services_arrêtés")
				Boucle=False


class MonThread(Thread):
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		# Vérification des services
		VerificationServices()
		time.sleep(3)
		
		# Fermeture automatique de la fenêtre graphique et de son thread
		#logger -t redundancy -p local0.info "POPUP : Fermeture du POPUP"
		Application.quit()
		self.stop()

	def stop(self):
		self.destroy(self)


class FenetreGraphique(Tk):
	# CONSTRUCTEUR
	def __init__(self):
		# Construction de la fenêtre graphique
		Tk.__init__(self)
		self.ProprieteFenetre()
		self.Composants()

	# Propriétés de la fenêtre
	def ProprieteFenetre(self):
	# TITRE
		self.title("Incident sur le serveur AUG-SRV-NP-2...")
		# Définition de la largeur et hauteur de la fenêtre graphique
		largeur = 400
		hauteur = 310
		# Calcul des coordonnées de centrage de la fenêtre graphique
		self.update_idletasks()
		x = (self.winfo_screenwidth() / 2) - (largeur / 2)
		y = (self.winfo_screenheight() / 2) - (hauteur / 2)
		# Positionnement de la fenêtre graphique
		self.geometry('{0}x{1}+{2}+{3}'.format(largeur, hauteur, x, y))
		# Désactivation de la fermeture et du redimensionnement
		#fenetre.protocol('WM_DELETE_WINDOW', lambda: None)
		self.resizable(0,0)

	# Ajout des composants
	def Composants(self):
		# LABELS
		self.LigneVide = Label(self,text="")
		self.LigneVide.pack()
		
		self.Message1 = Label(self,text="Pour des raisons techniques, le redémarrage",fg="red",font="Helvetica 12 bold italic")
		self.Message1.pack()
		self.Message2 = Label(self,text="des services de la supervision est necéssaire",fg="red",font="Helvetica 12 bold italic")
		self.Message2.pack()
		
		self.LigneVide = Label(self,text="")
		self.LigneVide.pack()
		
		self.Phase = Label(self,text="Phase d'arrêt des services",fg="orange",font="Helvetica 12 bold italic")
		self.Phase.pack()
		
		self.LigneVide = Label(self,text="")
		self.LigneVide.pack()
		
		self.Apache = Label(self,text="Arrêt du service APACHE en cours...",fg="black",font="Helvetica 11 bold")
		self.Apache.pack()
		self.Tomcat = Label(self,text="Arrêt du service TOMCAT en cours...",fg="black",font="Helvetica 11 bold")
		self.Tomcat.pack()
		self.Ndoutils = Label(self,text="Arrêt du service NDOUTILS en cours...",fg="black",font="Helvetica 11 bold")
		self.Ndoutils.pack()
		self.Nagios = Label(self,text="Arrêt du service NAGIOS en cours...",fg="black",font="Helvetica 11 bold")
		self.Nagios.pack()
		self.Ncpd = Label(self,text="Arrêt du Service NCPD en cours...",fg="black",font="Helvetica 11 bold")
		self.Ncpd.pack()
		
		self.LigneVide = Label(self,text="")
		self.LigneVide.pack()

		# Création de la barre de progression
		self.BarreProgression = ttk.Progressbar(self, length=350, mode='determinate')
		self.BarreProgression.pack()

	def Modif_Composants(self, message):
		# Logs et modifications des labels
		#if message == "services_arrêtés":
			#logger -t redundancy -p local0.info "POPUP : Phase d'arrêt des services OK"
		#if message == "services_redemarrés":
			#logger -t redundancy -p local0.info "POPUP : Phase de redémarrage des services OK"

		if message == "apache_KO":
			self.Apache.config(text="Service Apache arrêté",fg="grey")
			#logger -t redundancy -p local0.info "POPUP : Service APACHE arrêté"
		if message == "tomcat_KO":
			self.Tomcat.config(text="Service Tomcat arrêté",fg="grey")
			#logger -t redundancy -p local0.info "POPUP : Service TOMCAT arrêté"
		if message == "ndoutils_KO":
			self.Ndoutils.config(text="Service Ndoutils arrêté",fg="grey")
			#logger -t redundancy -p local0.info "POPUP : Service NDOUTILS arrêté"
		if message == "nagios_KO":
			self.Nagios.config(text="Service Nagios arrêté",fg="grey")
			#logger -t redundancy -p local0.info "POPUP : Service NAGIOS arrêté"
		if message == "npcd_KO":
			self.Ncpd.config(text="Service NPCD arrêté",fg="grey")
			#logger -t redundancy -p local0.info "POPUP : Service NCPD arrêté"


	def UpdateBarreProgression(self):
		self.BarreProgression.step(10)
	
	def quit(self):
		self.destroy()


#-------------------------------------------#
#                  MAIN                     #
#-------------------------------------------#
if __name__ == "__main__":
	Application=FenetreGraphique()
	MonThread().start()
	Application.mainloop()
