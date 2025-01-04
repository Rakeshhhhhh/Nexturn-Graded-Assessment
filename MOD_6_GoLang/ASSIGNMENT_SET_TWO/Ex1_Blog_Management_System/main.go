package main

import (
	"blog_management/config"
	"blog_management/controller"
	"blog_management/repository"
	"blog_management/services"
	"fmt"
	"net/http"
)

func main() {
	db, err := config.InitializeDatabase()
	if err != nil {
		fmt.Println("Error in Initializing Database: ", err)
	}
	defer db.Close()

	blogRepo := repository.NewBlogRepository(db)
	blogService := services.NewBlogService(blogRepo)
	blogController := controller.BlogController{BlogService: blogService}

	http.HandleFunc("/blogs", blogController.GetAllBlogs)
	http.HandleFunc("/blog", func(w http.ResponseWriter, r *http.Request) {
		switch r.Method {
		case http.MethodPost:
			blogController.CreateBlog(w, r)
		case http.MethodGet:
			blogController.GetBlog(w, r)
		case http.MethodPut:
			blogController.UpdateBlog(w, r)
		case http.MethodDelete:
			blogController.DeleteBlog(w, r)
		default:
			http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		}
	})

	http.ListenAndServe(":8080", nil)
}
