package main

import (
	"Emm/application"
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	currentPath, err := os.Getwd()
	if err != nil {
		fmt.Println("This path is unreached")
		return
	}
	if len(os.Args) < 2 {
		fmt.Println("lack argument: path")
		return
	}
	wantedPath := os.Args[1]
	var path string
	if filepath.IsAbs(wantedPath) {
		path = wantedPath
	} else {
		path = currentPath + string(os.PathSeparator) + wantedPath
	}
	_, err = os.Stat(path)
	if err != nil {
		fmt.Println("Unknown Path")
		return
	}
	files, _ := application.GetFiles(path)

	result := make(map[string]application.FileDesc)
	for _, file := range files {
		arr := strings.Split(file.Name, ".")
		suffix := arr[len(arr)-1]
		desc, contains := result[suffix]
		if contains {
			desc.Blank += file.Blank
			desc.Line += file.Line
		} else {
			result[suffix] = application.FileDesc{
				Name:  suffix,
				Line:  file.Line,
				Blank: file.Blank,
			}
		}
	}
	fmt.Println(result)
}
