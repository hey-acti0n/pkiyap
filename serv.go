package main

import (
	"fmt"
	"io"
	"math"
	"net/http"
	"strconv"
	"strings"
)

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

func solveBiquadratic(a, b, c float64, w http.ResponseWriter) {

	y1, y2, hasSolutions := solveQuadratic(a, b, c)

	if !hasSolutions {
		fmt.Println("Нет действительных решений")
		return
	}

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
		processedText := fmt.Sprintf("Вы отправили: %s", string(solutions))
		// Ответ
		w.Header().Set("Content-Type", "text/plain")
		w.WriteHeader(http.StatusOK)
		fmt.Fprint(w, processedText)
	}

}

func main() {

	// Обработчик для главной страницы
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Добро пожаловать! Вы обратились к %s", r.URL.Path)
	})

	// Обработчик для текстового запроса
	http.HandleFunc("/process", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			http.Error(w, "Только POST запросы поддерживаются", http.StatusMethodNotAllowed)
			return
		}

		// Чтение тела запроса
		body, err := io.ReadAll(r.Body)
		if err != nil {
			http.Error(w, "Ошибка чтения тела запроса", http.StatusInternalServerError)
			return
		}
		defer r.Body.Close()

		parts := strings.Fields(string(body))

		// Преобразуем части в float64
		num1, err1 := strconv.ParseFloat(parts[0], 64)
		num2, err2 := strconv.ParseFloat(parts[1], 64)
		num3, err3 := strconv.ParseFloat(parts[2], 64)
		if err1 != nil || err2 != nil || err3 != nil {
			fmt.Println("Ошибка преобразования одного или нескольких чисел")
			return
		}
		solveBiquadratic(num1, num2, num3, w)
		// Обработка текста (например, делаем его заглавным)
		// processedText := fmt.Sprintf("Вы отправили: %s", string(body))

		// // Ответ
		// w.Header().Set("Content-Type", "text/plain")
		// w.WriteHeader(http.StatusOK)
		// fmt.Fprint(w, processedText)
	})

	// Запуск сервера
	port := ":8080"
	fmt.Printf("Сервер запущен на http://localhost%s\n", port)
	if err := http.ListenAndServe(port, nil); err != nil {
		fmt.Printf("Ошибка запуска сервера: %s\n", err)
	}
}
