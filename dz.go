// package main

// import (
// 	"fmt"
// 	"net/http"
// )

// func handler(w http.ResponseWriter, r *http.Request) {
// 	fmt.Fprintln(w, "Hello, World!")
// }

// func main() {
// 	http.HandleFunc("/", handler)
// 	fmt.Println("Запуск сервера на порту 8080...")
// 	http.ListenAndServe(":8080", nil)
// }

package main

import (
	"fmt"
	"io"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	if r.Method == http.MethodPost {
		// Читаем данные из тела запроса
		body, err := io.ReadAll(r.Body)
		if err != nil {
			http.Error(w, "Не удалось прочитать данные", http.StatusInternalServerError)
			return
		}
		defer r.Body.Close()

		// Отправляем ответ с полученными данными
		fmt.Fprintf(w, "Данные получены: %s\n", string(body))
	} else {
		// Для других методов показываем приветствие
		fmt.Fprintln(w, "Hello, World! Отправьте данные через POST.")
	}
}

func main() {
	http.HandleFunc("/", handler)
	fmt.Println("Запуск сервера на порту 8080...")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Printf("Ошибка запуска сервера: %v\n", err)
	}
}
