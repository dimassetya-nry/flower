import turtle
import random

# Setup layar
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Latar belakang biru muda
screen.title("Bunga untuk Pacar Sayang 💖")

# Buat objek turtle
flower = turtle.Turtle()
flower.speed(10)  # Kecepatan animasi

# Fungsi untuk menggambar petal (kelopak bunga)
def draw_petal():
    flower.color("pink")
    flower.begin_fill()
    flower.circle(50, 60)  # Bentuk petal
    flower.left(120)
    flower.circle(50, 60)
    flower.end_fill()
    flower.left(180)

# Gambar batang bunga
flower.penup()
flower.goto(0, -200)
flower.pendown()
flower.color("green")
flower.pensize(5)
flower.goto(0, -50)

# Gambar kelopak bunga
flower.penup()
flower.goto(0, 0)
flower.pendown()
for _ in range(6):  # 6 kelopak
    draw_petal()
    flower.right(60)

# Gambar pusat bunga
flower.penup()
flower.goto(0, 0)
flower.pendown()
flower.color("yellow")
flower.begin_fill()
flower.circle(20)
flower.end_fill()

# Tambahkan daun
flower.penup()
flower.goto(-30, -100)
flower.pendown()
flower.color("green")
flower.begin_fill()
flower.circle(30, 90)
flower.left(90)
flower.circle(30, 90)
flower.end_fill()

# Tambahkan pesan romantis
flower.penup()
flower.goto(-150, 150)
flower.pendown()
flower.color("red")
flower.write("Untuk Pacar Sayangku, Kamu Bunga Terindah! 💕", font=("Arial", 16, "bold"))

# Sembunyikan turtle dan tutup saat klik
flower.hideturtle()
screen.exitonclick()
