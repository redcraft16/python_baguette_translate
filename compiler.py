entry = input("entrée> ")
with open(entry) as reader:
	file = reader.read()

define_value = []

line_num = 0

first_loop = True
for row in file.split("\n"):

	line_num += 1

	if first_loop:
		file = ""
		first_loop = False


	if "#" in row:
		if "inclure" in row:
			row = row.replace("\"", "")
			entry = entry.replace("\\", "/")
			if "/" in entry:
				i  = 0
				entry_split = entry.split("/")
				entry = ""
				for folder in entry_split:
					i += 1
					if i < len(entry_split):
						entry += folder + "/"
				with open(entry + row[9:]) as reader:
					ext_file = reader.read()
					file += "\n" + ext_file


			else:
				with open(row[9:]) as reader:
					ext_file = reader.read()
					print(ext_file)
					file += "\n" + reader.read()


		if "definir" in row:
			split_row = row.split(" ")
			define_value.append((split_row[1], split_row[2]))

	else:
		file += "\n" + row

for define in define_value:
	file = file.replace(define[0], define[1])

file = file.replace("taille ", "mode ")
file = file.replace("\"", "")
file = file.replace("$", "%")
file = file.replace("afficher ", "echo ")
file = file.replace("\n{", " {")
file = file.replace("\n\t{", " {")
file = file.replace("\n\t\t{", " {")
file = file.replace("\n\t\t\t{", " {")
file = file.replace("\n\t\t\t\t{", " {")
file = file.replace("\n\t\t\t\t\t{", " {")
file = file.replace("\n\t\t\t\t\t\t{", " {")
file = file.replace("{", "(")
file = file.replace("}", ")")
file = file.replace(" < ", " LSS ")
file = file.replace(" > ", " GTR ")
file = file.replace(" <= ", " LEQ ")
file = file.replace(" >= ", " GEQ ")
file = file.replace(" != ", " NEQ ")
file = file.replace(" == ", "==")
file = file.replace(" = ", "=")
file = file.replace("assigner_nombre ", "set /a ")
file = file.replace("assigner ", "set ")
file = file.replace("entree ", "set /p ")
file = file.replace("si ", "if ")
file = file.replace("attendre", "pause")
file = file.replace("aller_a ", "goto ")
file = file.replace("sinon ", "else ")
file = file.replace("pour ", "for ")
file = file.replace(" faire ", " do ")
file = file.replace(" dans ", " in ")
file = file.replace("effacer", "cls")
file = file.replace("titre ", "title ")
file = file.replace("%Aleatoire%", "%Random%")
file = file.replace("%Touche%", "%ERRORLEVEL%")
file = file.replace("afficher_ligne", "echo.")
file = file.replace("cls_fichier ", "echo. >")
file = file.replace(" /f ", " /f \"delims=\" ")
file = file.replace("arret", "exit")
file = file.replace("couleur ", "color ")
file = file.replace("fichier ", "type ")
file = file.replace("liste ", "dir ")
file = file.replace("tout", "/s")

file = file.split("\n")
first_loop = True
for line in file:

	if first_loop:
		file = ""

	elif "ecrire " in line:
		line = line.replace("ecrire ", "echo ")
		line = line.replace(" in ", ">")
		file += line + "\n"

	elif "ajouter " in line:
		line = line.replace("ajouter ", "echo ")
		line = line.replace(" in ", " >>\"")
		file += line + "\"\n"

	elif "choix " in line:
		line = line.replace("choix ", "choice /n /c ")
		line = line.replace(" ; ", " /m \"")
		file += line + "\"\n"

	elif "//" in line:
		line = line.split("//")
		line = line[0]
		file += line + "\n"

	else:
		file += line + "\n"
	first_loop = False

with open(input("sortie> ") + ".cmd", "w") as writer:
	writer.write("@echo off\n" + file)