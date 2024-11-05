package main

import (
	"fmt"
	"math"
)

// Функция для решения квадратного уравнения
func solveQuadratic(a, b, c float64) (float64, float64, bool) {
	discriminant := b*b - 4*a*c

	if discriminant < 0 {
		return 0, 0, false
	}

	sqrtDisc := math.Sqrt(discriminant)
	x1 := (-b + sqrtDisc) / (2 * a)
	x2 := (-b - sqrtDisc) / (2 * a)
	return x1, x2, true
}

// Основная функция для решения биквадратного уравнения
func solveBiquadratic(a, b, c float64) {
	// Решаем квадратное уравнение относительно y: ay^2 + by + c = 0
	y1, y2, hasSolutions := solveQuadratic(a, b, c)

	if !hasSolutions {
		fmt.Println("Нет действительных решений")
		return
	}

	// Ищем x: x^2 = y
	var solutions []float64

	if y1 >= 0 {
		solutions = append(solutions, math.Sqrt(y1), -math.Sqrt(y1))
	}

	if y2 >= 0 {
		solutions = append(solutions, math.Sqrt(y2), -math.Sqrt(y2))
	}

	if len(solutions) == 0 {
		fmt.Println("Нет действительных решений")
	} else {
		fmt.Println("Решения биквадратного уравнения:")
		for _, sol := range solutions {
			fmt.Printf("x = %.4f\n", sol)
		}
	}
}

func main() {
	var a, b, c float64
	fmt.Println("Введите коэффициенты a, b и c для уравнения ax^4 + bx^2 + c = 0:")
	fmt.Scan(&a, &b, &c)

	solveBiquadratic(a, b, c)
}
