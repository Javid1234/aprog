from PIL import Image
gji = input("Скачайте нужную картинку в папку где находится этот фильтр!\nВведите имя файла с его форматом!!!Формат только jpg!!!")

im = Image.open(gji) 
pixels = im.load()
x, y = im.size
p = int(input("Введите на сколько хотите изменить красный цвет:"))
u = int(input("Введите на сколько хотите изменить зеленый цвет:"))
k = int(input("Введите на сколько хотите изменить синий цвет:"))

for i in range(x):
	for j in range(y):
		r, g, b = pixels[i, j]


		pixels[i, j] = r + p,g + u,b + k

		

im.show()
dol = input("Хотите сохранить картиночку?))))Ответ пишите большими буквами!!!")
if dol == "ДА":
	fol = input("Введите имя файла с форматом jpg !!!")
	im.show(fol)
if dol == "НЕТ":
	print("Ну как хочешь((((")